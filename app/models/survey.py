from app.models import db
from sqlalchemy import String,  Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List,TYPE_CHECKING
from datetime import datetime
import enum

if TYPE_CHECKING:
    from .survey import Survey
    from .user import User
  
class survey_questions_type(enum.Enum):
    TEXT = "text"
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"

class Survey(db.Model):
    __tablename__="surveys"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    creator_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    title: Mapped[str] = mapped_column(String(120),nullable=False)
    description: Mapped[str] = mapped_column(String(120),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    creator: Mapped["User"] = relationship(back_populates="surveys")
    questions:Mapped[List["SurveyQuestion"]] = relationship(back_populates="survey")

class SurveyQuestion(db.Model):
    __tablename__= "survey_questions"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    survey_id : Mapped[int] = mapped_column(Integer(),ForeignKey("surveys.id",use_alter=True),nullable=False)
    question_text : Mapped[str] = mapped_column(String(120),nullable=False)
    type : Mapped[survey_questions_type] = mapped_column(Enum(survey_questions_type),nullable=False)
    survey: Mapped["Survey"] = relationship(back_populates="questions")
    answer: Mapped["SurveyAnswer"] = relationship(back_populates="question")

class SurveyAnswer(db.Model):
    __tablename__= "survey_answers"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    question_id: Mapped[int] = mapped_column(Integer(),ForeignKey("survey_questions.id",use_alter=True),nullable=False)
    answer_text: Mapped[str] = mapped_column(String(500),nullable=False)
    question: Mapped["SurveyQuestion"] = relationship(back_populates="answer")
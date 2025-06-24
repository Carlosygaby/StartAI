from main import db
from sqlalchemy import String, Boolean, Integer, DateTime, ForeignKey, Enum, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List,Optional
from datetime import datetime
import enum

class user_rol(enum.Enum):
    ENTERPRISE = "enterprise"
    ENTREPRENEUR= "entrepreneur"
    CONSUMER = "consumer"

class datasource_type(enum.Enum):
    SOCIAL = "social"
    ECONOMIC = "economic"
    STATISTICAL = "statistical"

class survey_questions_type(enum.Enum):
    TEXT = "text"
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"

class reactions_type(enum.Enum):
    LIKE = "like"
    DISLIKE = "dislike"
    SHARE = "share"
    REPORT = "report"
    SAVE = "save"

class User(db.Model):
    __tablename__:"users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable= False)
    email: Mapped[str] = mapped_column(String(120),nullable= False,unique=True)
    password: Mapped[str] = mapped_column(String(150),nullable= False)
    user_type: Mapped[user_rol] = mapped_column(Enum(user_rol),nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(),default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default= datetime.utcnow)
    last_login_at: Mapped[datetime] = mapped_column(DateTime(),nullable=False)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(120))
    email_verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime())
    bio: Mapped[Optional[str]] = mapped_column(String(500))
    products: Mapped[List["Product"]] = relationship(back_populates="owner")
    surveys: Mapped[List["Survey"]] = relationship(back_populates="creator")
    user1_chat: Mapped[List["Chat"]] = relationship("Chat",foreign_keys="[Chat.user1]",back_populates="user1")
    user2_chat: Mapped[List["Chat"]] = relationship("Chat",foreign_keys="[Chat.user2]",back_populates="user2")
    user_sended_messages: Mapped[List["ChatMenssage"]] = relationship(back_populates="sender")
    user_comentaries: Mapped[List["Comentary"]] = relationship(back_populates="creator")


class Product(db.Model):
    __tablename__:"products"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    description : Mapped[str] = mapped_column(String(500),nullable=False)
    purpose_market: Mapped[str] = mapped_column(String(120),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    owner: Mapped["User"] = relationship(back_populates="products")
    categories: Mapped["MarketCategory"] = relationship(secondary="product_categories",back_populates="products")
    trend_analysis: Mapped[List["TrendAnalysis"]] = relationship(back_populates="product")
    data_source: Mapped[List["ProductDataSource"]] = relationship(back_populates="product")
    product_comentaries: Mapped[List["Comentary"]] = relationship(back_populates="product")


class MarketCategory(db.Model):
    __tablename__: "market_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20),nullable=False)
    products: Mapped["Products"] = relationship(secondary="product_categories",back_populates="categories")


class ProductCategory(db.Model):
    __tablename__:"product_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"),nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

class TrendAnalysis(db.Model):
    __tablename__:"trend_analysis"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"),nullable=False)
    analysis_date: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    competition_score: Mapped[float] = mapped_column(Numeric(3,2),nullable=False)
    trend_score: Mapped[float] = mapped_column(Numeric(3,2),nullable=False)
    success_probability : Mapped[float] = mapped_column(Numeric(3,2), nullable=False)
    product: Mapped["Product"] = relationship(back_populates="trend_analysis")

class DataSource(db.Model):
    __tablename__:"data_sources"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    url: Mapped[str] = mapped_column(String(120),nullable=False)
    type: Mapped[datasource_type] = mapped_column(Enum(datasource_type),nullable=False)
    product_data_source: Mapped["ProductDataSource"] = relationship(back_populates="data_source")

class ProductDataSource(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"),nullable=False)
    data_source_id: Mapped[int] = mapped_column(ForeignKey("data_sources.id"),nullable=False)
    relevance_score: Mapped[float] = mapped_column(Numeric(3,2),nullable=False)
    data_source: Mapped[List["DataSource"]] = relationship(back_populates="product_data_source")
    product: Mapped["Product"] = relationship(back_populates="data_source")

class Survey(db.Model):
    __tablename__:"surveys"
    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    title: Mapped[str] = mapped_column(String(120),nullable=False)
    description: Mapped[str] = mapped_column(String(120),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    creator: Mapped["User"] = relationship(back_populates="surveys")
    questions:Mapped[List["SurveyQuestion"]] = relationship(back_populates="survey")

class SurveyQuestion(db.Model):
    __tablename__: "survey_questions"
    id: Mapped[int] = mapped_column(primary_key=True)
    survey_id : Mapped[int] = mapped_column(ForeignKey("surveys.id"),nullable=False)
    question_text : Mapped[str] = mapped_column(String(120),nullable=False)
    type : Mapped[survey_questions_type] = mapped_column(Enum(survey_questions_type),nullable=False)
    survey: Mapped["Survey"] = relationship(back_populates="questions")
    answer: Mapped["SurveyAnswer"] = relationship(back_populates="question")

class SurveyAnswer(db.Model):
    __tablename__: "survey_answers"
    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("survey_questions.id"),nullable=False)
    answer_text: Mapped[str] = mapped_column(String(500),nullable=False)
    question: Mapped["SurveyQuestion"] = relationship(back_populates="answer")

class Chat(db.Model):
    __tablename__:"chats"
    id: Mapped[int] = mapped_column(primary_key=True)
    user1_id : Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    user2_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(),dafault=datetime.utcnow)
    user1: Mapped["User"] = relationship("User", foreign_keys= [user1_id],back_populates="user1_chat")
    user2: Mapped["User"] = relationship("User",foreign_keys= [user2_id], back_populates="user2_chat")
    messages: Mapped[List["ChatMenssage"]] = relationship(back_populates="chat")

class ChatMenssage(db.Model):
    __tablename__:"chat_menssages"
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"),nullable=False)
    sender_id: Mapped[int] = mapped_colunm(ForeignKey("users.id"),nullable=False)
    content: Mapped[str] = mapped_column(String(500),nullable=False)
    sented_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    chat: Mapped["Chat"] = relationship(back_populates="messages")
    sender: Mapped["User"] = relationship(back_populates="user_sended_messages")

class Comentary(db.Model):
    __tablename__: "comentaries"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"),nullable=False)
    content: Mapped[str] = mapped_column(String(500),nullable=False)
    created_at: Maapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    creator: Mapped["User"] = relationship(back_populates="user_comentaries")
    product: Mapped["Product"] = relationship(back_populates="product_comentaries")

class Reaction(db.Model):
    __tablename__:"reactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"),nullable=False)
    type: Mapped[reactions_type] = mapped_column(Enum(reactions_type),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)


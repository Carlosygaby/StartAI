from app.models import db
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List,TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from .chat import Chat, ChatMenssage
    from .user import User
    

class Chat(db.Model):
    __tablename__="chats"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user1_id : Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    user2_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    user1: Mapped["User"] = relationship("User", foreign_keys= [user1_id],back_populates="user1_chat")
    user2: Mapped["User"] = relationship("User",foreign_keys= [user2_id], back_populates="user2_chat")
    messages: Mapped[List["ChatMenssage"]] = relationship(back_populates="chat")


class ChatMenssage(db.Model):
    __tablename__="chat_menssages"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    chat_id: Mapped[int] = mapped_column(Integer(),ForeignKey("chats.id",use_alter=True),nullable=False)
    sender_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    content: Mapped[str] = mapped_column(String(500),nullable=False)
    sented_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    chat: Mapped["Chat"] = relationship(back_populates="messages")
    sender: Mapped["User"] = relationship(back_populates="user_sended_messages")

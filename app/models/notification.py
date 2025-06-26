from app.models import db
from sqlalchemy import String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Notification(db.Model):
    __tablename__= "notifications"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    content: Mapped[str] = mapped_column(String(500),nullable=False)
    is_read: Mapped[bool] = mapped_column(Boolean(),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
from app.models import db
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from .product import Product
    from .user import User
    

class Comentary(db.Model):
    __tablename__= "comentaries"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    product_id: Mapped[int] = mapped_column(Integer(),ForeignKey("products.id",use_alter=True),nullable=False)
    content: Mapped[str] = mapped_column(String(500),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    creator: Mapped["User"] = relationship(back_populates="user_comentaries")
    product: Mapped["Product"] = relationship(back_populates="product_comentaries")
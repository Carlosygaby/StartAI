from app.models import db
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from .product import Product
    from .user import User
    


class Favorite(db.Model):
    __tablename__="favorites"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    product_id: Mapped[int] = mapped_column(Integer(),ForeignKey("products.id",use_alter=True),nullable=False)
    saved_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    user: Mapped["User"] = relationship(back_populates="user_favorites")
    product: Mapped["Product"] = relationship(back_populates="product_favorites")

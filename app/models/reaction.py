from app.models import db
from sqlalchemy import  Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime
import enum

if TYPE_CHECKING:
    from .product import Product
    from .user import User

class reactions_type(enum.Enum):
    LIKE = "like"
    DISLIKE = "dislike"
    SHARE = "share"
    REPORT = "report"
    SAVE = "save"

class Reaction(db.Model):
    __tablename__="reactions"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    product_id: Mapped[int] = mapped_column(Integer(),ForeignKey("products.id",use_alter=True),nullable=False)
    type: Mapped[reactions_type] = mapped_column(Enum(reactions_type),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    user: Mapped["User"] = relationship(back_populates="reactions")
    product: Mapped["Product"] = relationship(back_populates="product_reactions")

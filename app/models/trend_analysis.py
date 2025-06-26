from app.models import db
from sqlalchemy import Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from .product import Product


class TrendAnalysis(db.Model):
    __tablename__="trend_analysis"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer(),ForeignKey("products.id",use_alter=True),nullable=False)
    analysis_date: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    competition_score: Mapped[float] = mapped_column(Numeric(3,2),nullable=False)
    trend_score: Mapped[float] = mapped_column(Numeric(3,2),nullable=False)
    success_probability : Mapped[float] = mapped_column(Numeric(3,2), nullable=False)
    product: Mapped["Product"] = relationship(back_populates="trend_analysis")
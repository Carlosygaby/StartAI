from app.models import db
from sqlalchemy import String, Boolean, Integer, DateTime, ForeignKey, Enum, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List,TYPE_CHECKING
from datetime import datetime
import enum

if TYPE_CHECKING:
    from .suscription import Suscription,Payment
    from .user import User


class payment_status(enum.Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    FAILED = "failed"

class payment_methods(enum.Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    STRIPE = "stripe"


class Suscription(db.Model):
    __tablename__="suscriptions"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    plan : Mapped[str] = mapped_column(String(60),default="Free")
    start_date: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    end_date: Mapped[datetime] = mapped_column(DateTime(),nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean(),default=False)
    user: Mapped["User"] = relationship(back_populates="user_suscriptions")
    suscription_payments: Mapped[List["Payment"]] = relationship(back_populates="suscription")

class Payment(db.Model):
    __tablename__="payments"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    suscription_id : Mapped[int] = mapped_column(Integer(),ForeignKey("suscriptions.id",use_alter=True),nullable=False)
    amount: Mapped[int] = mapped_column(Numeric(10,2),nullable=False)
    payment_date: Mapped[datetime] = mapped_column(DateTime(),nullable=False)
    status: Mapped[payment_status] = mapped_column(Enum(payment_status),nullable=False)
    method: Mapped[payment_methods] = mapped_column(Enum(payment_methods),nullable=False)
    user: Mapped["User"] = relationship(back_populates="user_payments")
    suscription: Mapped["Suscription"] = relationship(back_populates="suscription_payments")




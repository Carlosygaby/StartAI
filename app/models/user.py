from app.models import db
from sqlalchemy import String, Boolean, Integer, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List,Optional,TYPE_CHECKING
from datetime import datetime
import enum

if TYPE_CHECKING:
    from .product import Product
    from .survey import Survey
    from .chat import Chat, ChatMenssage
    from .comentary import Comentary
    from .reaction import Reaction
    from .favorite import Favorite
    from .rating import Rating
    from .suscription import Suscription,Payment
    
class user_rol(enum.Enum):
    ENTERPRISE = "enterprise"
    ENTREPRENEUR= "entrepreneur"
    CONSUMER = "consumer"

class User(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable= False)
    email: Mapped[str] = mapped_column(String(120),nullable= False,unique=True)
    password: Mapped[str] = mapped_column(String(150),nullable= False)
    user_type: Mapped[user_rol] = mapped_column(Enum(user_rol),nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(),default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default= datetime.utcnow)
    last_login_at: Mapped[datetime] = mapped_column(DateTime(),nullable=False)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(120))
    email_verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime())
    bio: Mapped[Optional[str]] = mapped_column(String(500))
    products: Mapped[List["Product"]] = relationship("Product",back_populates="owner")
    surveys: Mapped[List["Survey"]] = relationship("Survey",back_populates="creator")
    user1_chat: Mapped[List["Chat"]] = relationship("Chat",foreign_keys="[Chat.user1]",back_populates="user1")
    user2_chat: Mapped[List["Chat"]] = relationship("Chat",foreign_keys="[Chat.user2]",back_populates="user2")
    user_sended_messages: Mapped[List["ChatMenssage"]] = relationship("ChatMessage",back_populates="sender")
    user_comentaries: Mapped[List["Comentary"]] = relationship("Comentary",back_populates="creator")
    reactions: Mapped[List["Reaction"]] = relationship("Reaction",back_populates="user")
    user_favorites: Mapped[List["Favorite"]] = relationship("Favorite",back_populates="user")
    user_ratings: Mapped[List["Rating"]] = relationship("Rating",back_populates="user")
    user_suscriptions: Mapped[List["Suscription"]] = relationship("Suscription",back_populates="user")
    user_payments: Mapped[List["Payment"]] = relationship("Payment",back_populates="user")
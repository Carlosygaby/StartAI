from app.models import db
from sqlalchemy import String, Boolean, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List,TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from .product import Product,ProductDataSource
    from .comentary import Comentary
    from .reaction import Reaction  
    from .favorite import Favorite
    from .rating import Rating
    from .user import User
    from .trend_analysis import TrendAnalysis
    from .data_source import DataSource
    

class Product(db.Model):
    __tablename__="products"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(),ForeignKey("users.id",use_alter=True),nullable=False)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    description : Mapped[str] = mapped_column(String(500),nullable=False)
    purpose_market: Mapped[str] = mapped_column(String(120),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    owner: Mapped["User"] = relationship(back_populates="products")
    categories: Mapped["MarketCategory"] = relationship(secondary="product_categories",back_populates="products")
    trend_analysis: Mapped[List["TrendAnalysis"]] = relationship(back_populates="product")
    data_source: Mapped[List["ProductDataSource"]] = relationship(back_populates="product")
    product_comentaries: Mapped[List["Comentary"]] = relationship(back_populates="product")
    product_reactions: Mapped[List["Reaction"]] = relationship(back_populates="product")
    product_images:Mapped[List["ProductImage"]] = relationship(back_populates="product")
    product_favorites: Mapped[List["Favorite"]] = relationship(back_populates="product")
    product_ratings: Mapped[List["Rating"]] = relationship(back_populates="product")

class ProductCategory(db.Model):
    __tablename__="product_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer(),ForeignKey("products.id",use_alter=True),nullable=False)
    category_id: Mapped[int] = mapped_column(Integer(),ForeignKey("market_categories.id",use_alter=True),nullable=False)

class ProductDataSource(db.Model):
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer(),ForeignKey("products.id",use_alter=True),nullable=False)
    data_source_id: Mapped[int] = mapped_column(Integer(),ForeignKey("data_sources.id",use_alter=True),nullable=False)
    relevance_score: Mapped[float] = mapped_column(Numeric(3,2),nullable=False)
    data_source: Mapped[List["DataSource"]] = relationship(back_populates="product_data_source")
    product: Mapped["Product"] = relationship(back_populates="data_source")

class ProductImage(db.Model):
    __tablename__="product_images"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer(),ForeignKey("products.id",use_alter=True),nullable=False)
    url: Mapped[str] = mapped_column(String(120),nullable=False)
    is_primary: Mapped[bool] = mapped_column(Boolean(),nullable=False)
    upload_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow)
    product: Mapped["Product"] = relationship(back_populates="product_images")

class MarketCategory(db.Model):
    __tablename__= "market_categories"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    name: Mapped[str] = mapped_column(String(20),nullable=False)
    products: Mapped["Product"] = relationship(secondary="product_categories",back_populates="categories")

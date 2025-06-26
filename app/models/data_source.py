from app.models import db
from sqlalchemy import String, Integer,  Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

import enum

if TYPE_CHECKING:
    from .product import ProductDataSource

class datasource_type(enum.Enum):
    SOCIAL = "social"
    ECONOMIC = "economic"
    STATISTICAL = "statistical"

class DataSource(db.Model):
    __tablename__="data_sources"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    url: Mapped[str] = mapped_column(String(120),nullable=False)
    type: Mapped[datasource_type] = mapped_column(Enum(datasource_type),nullable=False)
    product_data_source: Mapped["ProductDataSource"] = relationship(back_populates="data_source")

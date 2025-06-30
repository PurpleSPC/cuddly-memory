from typing import TYPE_CHECKING, Optional
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sale import Sale


class ProductLine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    commision_rate: float 
    sales: list[Sale] = Relationship(back_populates="productline")

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    catalog_no: str = Field(unique=True)
    description: str = Field(unique=True)
    product_line_id: int = Field(foreign_key="productline.id")

class AccountProductPrice(Sale, table=True):
    account_id: int = Field(foreign_key="account.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    unit_price: float



from typing import TYPE_CHECKING, Optional
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sale import Sale
    from .inventory import InventorySet

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    catalog_no: str = Field(unique=True)
    description: str = Field(unique=True)
    product_line_id: int = Field(foreign_key="productline.id")

class ProductLine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    commision_rate: float 
    sales: list[Sale] = Relationship(back_populates="productline")
    inventory_sets: list[InventorySet] = Relationship(back_populates="productline")
    products: list[Product] = Relationship(back_populates="productline")


class AccountProductPrice(Sale, table=True):
    account_id: int = Field(foreign_key="account.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    unit_price: float

class SaleItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_id: int = Field(foreign_key="sale.id")
    product_id: int = Field(foreign_key="product.id")
    qty: int = Field(default=1, gt=0)
    unit_price: float = Field(default=0.00, ge=0.00)
    line_total: float = Field(default=0.00)
    # computes line_total
    def __init__(self, **data):
        super().__init__(**data)
        self.line_total = self.qty * self.unit_price




from typing import TYPE_CHECKING, Optional
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sale import Sale
    from .inventory import InventorySet
    from .account_product_price import AccountProductPrice

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    catalog_no: str = Field(unique=True)
    description: str = Field(unique=True)
    product_line_id: int = Field(foreign_key="productline.id")
    account_prices: list["AccountProductPrice"] = Relationship(back_populates="product")
    product_line: "ProductLine" = Relationship(back_populates="products")

class ProductLine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    commision_rate: float 
    sales: list["Sale"] = Relationship(back_populates="product_line")
    inventory_sets: list["InventorySet"] = Relationship(back_populates="product_line")
    products: list["Product"] = Relationship(back_populates="product_line")







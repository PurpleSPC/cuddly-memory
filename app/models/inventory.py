from typing import TYPE_CHECKING, Optional
from datetime import date
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .product import ProductLine, Product
    from .sale import Sale


class InventorySet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    set_code: str = Field(unique=True)
    description: str
    prod_lin_id: int = Field(foreign_key="productline.id")
    product_line: ProductLine = Relationship(back_populates="inventoryset")
    products: list["Product"] = Relationship(back_populates="inventoryset")
    home_loc_id: int = Field(foreign_key="location.id")
    current_loc_id: int = Field(foreign_key="location.id")
    sales: list ["Sale"] = Relationship(back_populates="inventoryset")
    

class InventoryMovement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    set_id: int = Field(foreign_key="inventoryset.id")
    req_date: date 
    sale_id: Optional[int] = Field(foreign_key="sale.id")
    from_loc_id: int = Field(foreign_key="location.id")
    to_loc_id: int = Field(foreign_key="location.id")
    return_due_date: date

class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str= Field(unique=True)
    address: str
    inventory_sets: list["InventorySet"] = Relationship(back_populates="location")
from typing import TYPE_CHECKING, Optional
from datetime import date
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from product import ProductLine
    from sale import Sale

class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str= Field(unique=True)
    address: str

class InventorySet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    set_code: str = Field(unique=True)
    description: str
    prod_lin_id: int = Field(foreign_key="productline.id")
    home_loc_id: int = Field(foreign_key="location.id")
    current_loc_id: int = Field(foreign_key="location.id")

class InventoryMovement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    set_id: int = Field(foreign_key="inventoryset.id")
    req_date: date 
    sale_id: Optional[int] = Field(foreign_key="sale.id")
    from_loc_id: int = Field(foreign_key="location.id")
    to_loc_id: int = Field(foreign_key="location.id")
    return_due_date: date

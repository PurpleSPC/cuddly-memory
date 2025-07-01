from typing import TYPE_CHECKING, Optional
from app.models.common import SQLModel, Field, Relationship
from app.models.links import SurgeonAccountLink

if TYPE_CHECKING:
    from .sale import Sale
    from .surgeon import Surgeon

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    address: Optional[str]

    sales: list["Sale"] = Relationship(back_populates="account")
    surgeons: list["Surgeon"] = Relationship(
        back_populates="accounts", 
        link_model=SurgeonAccountLink
        )
    
class PurchaseOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    po_number: str
    account_id: int = Field(foreign_key="account.id")
    sale_id: int = Field(foreign_key="sale.id")
    is_pending: bool

class SurgeonAccountLink(SQLModel, table=True):
    surgeon_id: int = Field(foreign_key="surgeon.id", primary_key=True)
    account_id: int = Field(foreign_key="account.id", primary_key=True)

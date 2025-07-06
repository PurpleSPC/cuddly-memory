from typing import TYPE_CHECKING, Optional, List
from app.models.common import SQLModel, Field, Relationship
from app.models.links import SurgeonAccountLink

if TYPE_CHECKING:
    from .sale import Sale
    from .surgeon import Surgeon

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    address: Optional[str]

    sales: List["Sale"] = Relationship(back_populates="account")
    surgeons: List["Surgeon"] = Relationship(
        back_populates="accounts", 
        link_model=SurgeonAccountLink
        )
    
class PurchaseOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    po_number: str
    account_id: int = Field(foreign_key="account.id")
    is_pending: bool


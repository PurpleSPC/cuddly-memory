from typing import TYPE_CHECKING, Optional
from datetime import date
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .account import Account, PurchaseOrder
    from .product import SaleItem
    from .rep import SalesTeam, Rep
    from .inventory import Location
    from .surgeon import Surgeon

class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_date: date = Field(default_factory=lambda: date.today())
    received_date: date = Field(default_factory=lambda: date.today())
    account_id: int = Field(foreign_key="account.id")
    account: Optional["Account"] = Relationship(back_populates="sale")
    surgeon_id: int = Field(foreign_key="surgeon.id")
    surgeon: Surgeon = Relationship(back_populates="sale")
    rep_id: int = Field(foreign_key="rep.id")
    sales_team: SalesTeam = Relationship(back_populates="sale")
    sales_rep: Rep = Relationship(back_populates="sale")
    po_id: Optional[int] = Field(foreign_key="purchaseorder.id")
    purchase_order: PurchaseOrder = Relationship(back_populates="sale")
    rstck_loc_id: int = Field(foreign_key="location.id")
    restock_loc: Location = Relationship(back_populates="sale")
    total_amt: float
    items: list["SaleItem"] = Relationship(back_populates="sale")





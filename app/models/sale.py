from typing import TYPE_CHECKING, Optional
from datetime import date
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .account import Account, PurchaseOrder
    from .product import ProductLine
    from .rep import SalesTeam, Rep
    from .inventory import Location
    from .surgeon import Surgeon
    from .sale_item import SaleItem

class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_date: date = Field(default_factory=lambda: date.today())
    received_date: date = Field(default_factory=lambda: date.today())
    account_id: int = Field(foreign_key="account.id")
    account: Optional["Account"] = Relationship(back_populates="sales")
    procuct_line_id: Optional[int] = Field(foreign_key="productline.id")
    product_line: Optional["ProductLine"] = Relationship(back_populates="sales")
    surgeon_id: Optional[int] = Field(foreign_key="surgeon.id")
    surgeon: Optional["Surgeon"] = Relationship(back_populates="surgeries")
    rep_id: int = Field(foreign_key="rep.id")
    po_id: Optional[int] = Field(foreign_key="purchaseorder.id")
    rstck_loc_id: int = Field(foreign_key="location.id")
    total_amt: float
    items: list["SaleItem"] = Relationship(back_populates="sale")
    sales_team_id: Optional[int] = Field(foreign_key="salesteam.id")
    sales_team: Optional["SalesTeam"] = Relationship(back_populates="sales")
    rep: Optional["Rep"] = Relationship(back_populates="sales")




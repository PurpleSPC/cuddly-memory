from typing import TYPE_CHECKING, Optional
from datetime import date
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .account import Account
    from .product import SaleItem

class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_date: date = Field(default_factory=lambda: date.today())
    received_date: date = Field(default_factory=lambda: date.today())
    account_id: int = Field(foreign_key="account.id")
    account: Account = Relationship(back_populates="sale")
    surgeon_id: int = Field(foreign_key="surgeon.id")
    rep_id: int = Field(foreign_key="rep.id")
    po_id: Optional[int] = Field(foreign_key="purchaseorder.id")
    rstck_loc_id: int = Field(foreign_key="location.id")
    total_amt: float
    items: list[SaleItem] = Relationship(back_populates="sale")

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




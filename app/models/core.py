from sqlmodel import SQLModel, Field, create_engine
from typing import Optional
from datetime import date

###############################################
# Create tables

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    address: Optional[str]

class Surgeon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    npi_no: Optional[int] = Field(unique=True)

class SurgeonAccount(SQLModel, table=True):
    surgeon_id: int = Field(foreign_key="surgeon.id", primary_key=True)
    account_id: int = Field(foreign_key="account.id", primary_key=True)
    __table_args__ = (
        {"primary_key": ("surgeon_id", "account_id")}
    )

class SalesTeam(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

class Rep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    team_id: int = Field(foreign_key="salesteam.id")

class ProductLine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    commision_rate: float 

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    catalog_no: str = Field(unique=True)
    description: str = Field(unique=True)
    product_line_id: int = Field(foreign_key="productline.id")

class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_date: date
    received_date: date = Field(default_factory=date.today)
    account_id: int = Field(foreign_key="account.id")
    surgeon_id: int = Field(foreign_key="surgeon.id")
    rep_id: int = Field(foreign_key="rep.id")
    po_id: Optional[int] = Field(foreign_key="purchaseorder.id")
    rstck_loc_id: int = Field(foreign_key="location.id")
    total_amt: float

class SaleItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_id: int = Field("sale.id")
    product_id: int = Field("product.id")
    qty: int
    unit_price: float
    line_total: float 

class PurchaseOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    po_number: str
    account_id: int = Field(foreign_key="account.id")
    sale_id: int = Field(foreign_key="sale.id")
    is_pending: bool

class AccountProductPrice(SQLModel, table=True):
    account_id: int = Field(foreign_key="account.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    unit_price: float
    __table_args__ = (
        {"primary_key": ("account_id", "product_id")}
    )


class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str= Field(unique=True)
    address: str

class InventorySet(SQLModel, Table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    set_code: str = Field(unique=True)
    description: str
    prod_lin_id: int = Field(foreign_key="productline.id")
    home_loc_id: int = Field(foreign_key="location.id")
    current_loc_id: int = Field(foreign_key="location.id")

class InventoryMovement(SQLModel, Table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    set_id: int = Field(foreign_key="inventoryset.id")
    req_date: date 
    sale_id: Optional[int] = Field(foreign_key="sale.id")
    from_loc_id: int = Field(foreign_key="location.id")
    to_loc_id: int = Field(foreign_key="location.id")
    return_due_date: date




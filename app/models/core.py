from sqlmodel import SQLModel, Field, create_engine
from typing import Optional
from datetime import date

###############################################
# Create tables

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: Optional[str]

class Surgeon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    npi_no: Optional[int]

class SurgeonAccounts(SQLModel, table=True):
    surgeon_id: int = Field(foreign_key="surgeon.id", primary_key=True)
    account_id: int = Field(foreign_key="account.id", primary_key=True)
    __table_args__ = (
        {"primary_key": ("surgeon_id", "account_id")}
    )

class SalesTeam(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Rep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    team_id: int = Field(foreign_key="salesteam.id")

class ProductLine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    commision_rate: float 

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    catalog_no: str
    description: str
    product_line_id: int = Field(foreign_key="productline.id")

class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_date: date
    received_date: date = Field(default_factory=date.today)
    account_id: int = Field(foreign_key="account.id")
    surgeon_id: int = Field(foreign_key="surgeon.id")
    rep_id: int = Field(foreign_key="rep.id")
    po_id: Optional[int] = Field(foreign_key="purchase_orders.id")
    rstck_loc_id: int = Field(foreign_key="location.id")
    total_amt: float

class SaleItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_id: int = Field("sale.id")
    product_id: int = Field("product.id")
    qty: int
    unit_price: float

class PurchaseOrder(SQLModel, table=True):
    ...

class AccountProductPrices(SQLModel, table=True):
    ...
## account_id
## product_id
## unit_price
## composite PK (account_id,product_id)

class Location(SQLModel, table=True):
    ...
## id
## name

#########################
# creating db

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
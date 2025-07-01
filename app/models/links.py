from typing import TYPE_CHECKING, Optional
from .common import SQLModel, Field, Relationship



class SurgeonAccountLink(SQLModel, table=True):
    surgeon_id: int = Field(foreign_key="surgeon.id", primary_key=True)
    account_id: int = Field(foreign_key="account.id", primary_key=True)

class AccountProductPrice(SQLModel, table=True):
    account_id: int = Field(foreign_key="account.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    unit_price: float


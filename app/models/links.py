from typing import TYPE_CHECKING, Optional
from .common import SQLModel, Field, Relationship




class SurgeonAccountLink(SQLModel, table=True):
    surgeon_id: int = Field(foreign_key="surgeon.id", primary_key=True)
    account_id: int = Field(foreign_key="account.id", primary_key=True)


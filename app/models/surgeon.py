from typing import TYPE_CHECKING, Optional
from .common import SQLModel, Field, Relationship
from .links import SurgeonAccountLink


if TYPE_CHECKING:
    from .sale import Sale
    from .account import Account


class Surgeon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    npi_no: Optional[int] = Field(unique=True)
    surgeries = list["Sale"] = Relationship(back_populates="surgeon")
    accounts: list["Account"] = Relationship(
        back_populates="surgeons", 
        link_model=SurgeonAccountLink
        )



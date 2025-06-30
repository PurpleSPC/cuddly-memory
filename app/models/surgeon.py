from typing import TYPE_CHECKING, Optional
from .common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sale import Sale


class Surgeon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    npi_no: Optional[int] = Field(unique=True)
    surgeries = list[Sale] = Relationship(back_populates="surgeon")

class SurgeonAccount(SQLModel, table=True):
    surgeon_id: int = Field(foreign_key="surgeon.id", primary_key=True)
    account_id: int = Field(foreign_key="account.id", primary_key=True)

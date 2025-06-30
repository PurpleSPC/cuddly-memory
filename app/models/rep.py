from typing import TYPE_CHECKING, Optional
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sale import Sale
    



class SalesTeam(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    sales: list[Sale] = Relationship(back_populates="salesteam")


class Rep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    team_id: int = Field(foreign_key="salesteam.id")
    team: SalesTeam = Relationship(back_populates="rep")
    sales: list[Sale] = Relationship(back_populates="rep")
    


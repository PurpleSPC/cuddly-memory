from typing import TYPE_CHECKING
from pydantic import BaseModel
from app.models.common import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .sale import Sale


class SaleItem(SQLModel, table=True):
    sale_id: int = Field(foreign_key="sale.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    
    qty: int = Field(default=1, gt=0)
    unit_price: float = Field(default=0.00, ge=0.00)
    line_total: float = Field(default=0.00, ge=0.00)
    
    sale: "Sale" = Relationship(back_populates="items")

    def compute_line_total(self) -> float:
        return round(self.qty * self.unit_price, 2)


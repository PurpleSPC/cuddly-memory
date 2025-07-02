from .common import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models import Product

class AccountProductPrice(SQLModel, table=True):
    account_id: int = Field(foreign_key="account.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    unit_price: float
    product: "Product" = Relationship(back_populates="account_prices")

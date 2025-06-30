from typing import List, Optional
from sqlmodel import Session, select

from app.db.database import get_session
from app.models import Account, Sale, SaleItem, Product


#
# ACCOUNT
# 

def create_account(name: str, address: Optional[str] = None)-> Account:
    with get_session() as session:
        acct = Account(name=name, address=address)
        session.add(acct)
        session.commit()
        session.refresh(acct)
        return acct

def list_accounts() -> List[Account]:
    with get_session() as session:
        return session.exec(select(Account)).all()
    
def update_account(account_id: int, name: Optional[str] = None, address: Optional[str] = None) -> Optional[Account]:
    with get_session() as session:
        acct = session.get(Account, account_id)
        if not acct:
            return None
        if name is not None:
            acct.name = name
        if address is not None:
            acct.address = address
        session.add(acct)
        session.commit()
        session.refresh(acct)
        return acct
    
def delete_account(account_id: int) -> bool:
    with get_session() as session:
        acct = session.get(Account, account_id)
        if not acct:
            return False
        session.delete(acct)
        session.commit()
        return True
    
# 
# SALE
# 

def create_sale(account_id: int, sale_date, total_amt: float) -> Sale:
    with get_session() as session:
        sale = Sale(account_id=account_id, sale_date=sale_date, total_amt=total_amt)
        session.add(sale)
        session.commit()
        session.refresh(sale)
        return sale
    
def get_sale(sale_id: int) -> Optional[Sale]:
    with get_session() as session:
        return session.get(Sale, sale_id)
    
def list_sales() -> List[Sale]:
     with get_session() as session:
            return session.exex(select(Sale)).all()
     
def update_sale(sale_id: int, **fields) -> Optional[Sale]:
        with get_session() as session:
            sale = session.get(Sale,sale_id)
            if not sale:
                return None
            for key, val in fields.items():
                setattr(sale, key, val)
            session.add(sale)
            session.commit()
            session.refresh(sale)
            return sale

def delete_sale(sale_id:int) -> bool:
        with get_session() as session:
            sale = session.get(Sale, sale_id)
            if not sale:
                 return False
            session.delete(sale)
            session.commit()
            return True
        
# 
# SALE ITEM
# 

# need to integrate product and/or account_prod_price 
def add_item_to_sale(sale_id: int, product_id: int, qty: int, unit_price: float) -> List[SaleItem]:
         with get_session() as session:
            item = SaleItem(sale_id=sale_id, product_id=product_id, qty=qty, unit_price=unit_price)
            session.add(item)
            session.commit()
            session.refresh(item)
            return item
def list_items_for_sale(sale_id: int) -> List[SaleItem]:
    with get_session() as session:
        statement = select(SaleItem).where(SaleItem.sale_id == sale_id)
        return session.exec(statement).all()

def delete_sale_item(item_id: int) -> bool:
    with get_session() as session:
        item = session.get(SaleItem, item_id)
        if not item:
            return False
        session.delete(item)
        session.commit()
        return True

#
# PRODUCT
#
def list_products() -> List[Product]:
    with get_session() as session:
        return session.exec(select(Product)).all()

def get_product(product_id: int) -> Optional[Product]:
    with get_session() as session:
        return session.get(Product, product_id)

from typing import List, Optional, Dict, Any
from sqlmodel import select

from app.db.database import get_session
from app.models import (
    Account,
    Sale, 
    SaleItem, 
    Product, 
    Surgeon, 
    SurgeonAccountLink, 
    AccountProductPrice)



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
    
def get_account_by_name(name:str) -> Optional[Account]:
    with get_session() as session:
        statement = select(Account).where(Account.name == name)
        return session.exec(statement).first()
    
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

def create_sale_with_items(
        account_id: int, 
        sale_date, 
        items:List[Dict[str, Any]],
        ) -> Optional[Sale]:
    """
    items: [{"catalog_no":str,"qty":int}, ...]
    """
    with get_session() as session:
        # create sale with a 0.0 total
        sale = Sale(account_id=account_id, sale_date=sale_date, total_amt=0.0)
        session.add(sale)
        session.flush()  # assigns a sale.id

        # iterate items to get Product and AccountProductPrice
        total = 0.0
        for row in items:
            product = session.exec(select(Product).where(Product.catalog_no == row["catalog_no"])).first()
            if not product:
                session.rollback()
                raise ValueError(f"Unknown catalog number: {row['catalog_no']}")
            
            price = get_account_product_price(account_id, product.id)
            if price is None:
                session.rollback()
                raise ValueError(f"No pricing for account: {account_id}, product: {product.id}")
            
            item = SaleItem(
                sale_id=sale.id,
                product_id=product.id,
                qty=row["qty"],
                unit_price=price,
            )
            item.line_total = round(item.qty * item.unit_price, 2)
            total += item.line_total
            session.add(item)

            sale.total_amt = round(total, 2)
            session.add(sale)
            session.commit()
            session.refresh(sale)
            return sale
            

         
    
    
def get_sale(sale_id: int) -> Optional[Sale]:
    with get_session() as session:
        return session.get(Sale, sale_id)
    
def list_sales() -> List[Sale]:
     with get_session() as session:
            return session.exec(select(Sale)).all()
     
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
def add_item_to_sale(sale_id: int, product_id: int, qty: int, unit_price: float) -> SaleItem:
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
    
def get_account_product_price(account_id:int, product_id:int) -> Optional[float]:
    with get_session() as session:
        statement = select(AccountProductPrice).where(
            (AccountProductPrice.account_id == account_id) &
            (AccountProductPrice.product_id == product_id)
        )
        result = session.exec(statement).first()
        return result.unit_price if result else None

#
# PRODUCT
#
def list_products() -> List[Product]:
    with get_session() as session:
        return session.exec(select(Product)).all()

def get_product(product_id: int) -> Optional[Product]:
    with get_session() as session:
        return session.get(Product, product_id)
    
def get_product_by_catalog_no(catalog_no:str)-> Optional[Product]:
    with get_session() as session:
        statement = select(Product).where(Product.catalog_no == catalog_no)
        return session.exec(statement).first()
    
def get_product_by_description(desc_term:str):
    with get_session as session:
        statement = select(Product).where(Product.description.contains(desc_term))
        return session.exec(statement).all()


# 
# Surgeon
# 

def create_surgeon(name: str, npi_no: Optional[int]):
    with get_session() as session:
        surgeon = Surgeon(name=name, npi_no=npi_no)
        session.add(surgeon)
        session.commit()
        session.refresh(surgeon)
        return surgeon
    
def assign_surgeon_account(surgeon_id: int, account_id: int):
    with get_session() as session:
        surgeon_account = SurgeonAccountLink(surgeon_id=surgeon_id, account_id=account_id)
        session.add(surgeon_account)
        session.commit()
        session.refresh(surgeon_account)
        return surgeon_account
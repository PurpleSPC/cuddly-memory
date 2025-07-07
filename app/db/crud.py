from typing import List, Optional, Dict, Any
from datetime import date
from sqlmodel import select
from sqlalchemy.exc import IntegrityError

from app.db.database import get_session
from app.models import (
    Account,
    Sale, 
    SaleItem, 
    ProductLine,
    Product, 
    Surgeon, 
    SurgeonAccountLink, 
    AccountProductPrice,
    SalesTeam,
    Rep,
    Location
    )



#
# ACCOUNT
# 

def create_account(name: str, address: Optional[str] = None)-> Account:
    with get_session() as session:
        acct = Account(name=name, address=address)
        try:
            session.add(acct)
            session.commit()
            session.refresh(acct)
            return acct
        except IntegrityError:
            session.rollback()
            raise ValueError(f"Account {acct.name} already exists in db")
        
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
            raise ValueError(f"No account exists in db with id: {account_id}")
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

def get_account(account_id: int) -> Optional[Account]:
       with get_session() as session:
           account = session.get(Account, account_id)
           if account == None:
               raise ValueError(f"No account exists for id: {account_id}")
           else:
               return account

def update_account_price(account_id:int, product_id:int, new_price:float)->AccountProductPrice:
    with get_session() as session:
        statement = select(AccountProductPrice).where((AccountProductPrice.product_id== product_id) & (AccountProductPrice.account_id==account_id))
        acct_prod_price = session.exec(statement).one_or_none()
        if acct_prod_price is None:
            raise ValueError(f"No pricing found for account: {account_id}, catalog#: {product_id} ")
        acct_prod_price.unit_price = new_price
        session.add(acct_prod_price)
        session.commit()
        session.refresh(acct_prod_price)
        return acct_prod_price
        
def set_account_prices_to_list(account_id:int, prod_line_id:int)-> List[AccountProductPrice]:
    with get_session() as session:
        product_prices = session.exec(select(AccountProductPrice)
                                      .join(Product, AccountProductPrice.product)
                                      .where(
                                          (AccountProductPrice.account_id==account_id)&
                                          (AccountProductPrice.product_id==prod_line_id))).all()
        product_line = session.get(ProductLine, prod_line_id)
        products = session.exec(select(Product)
                                .where(Product.product_line_id==prod_line_id)).all()
        if products == None:
            raise ValueError(
                f"No Products found for product line: {product_line.name}"
            )
        for product in products:
            acct_price = AccountProductPrice(account_id=account_id,product_id=product.id,unit_price=product.list_price)
            session.add(acct_price)
        session.commit()

        for price in product_prices:
            session.refresh(price)
        return session.exec(select(AccountProductPrice)
                                      .join(Product, AccountProductPrice.product)
                                      .where(
                                          (AccountProductPrice.account_id==account_id)&
                                          (AccountProductPrice.product_id==prod_line_id))).all()
        

# 
# SALE
# 

# def create_sale(account_id: int, sale_date, total_amt: float) -> Sale:
    # with get_session() as session:
    #     sale = Sale(account_id=account_id, sale_date=sale_date, total_amt=total_amt)
    #     session.add(sale)
    #     session.commit()
    #     session.refresh(sale)
    #     return sale

def create_sale( 
        sale_date, 
        received_date: Optional[date],
        account_id: int,
        product_line_id: Optional[int],
        surgeon_id: int,
        rep_id: int,
        team_id: Optional[int],
        po_id: Optional[str],
        rstck_loc_id: int,
        items:List[Dict[str, Any]],
        ) -> Optional[Sale]:
    """
    items: [{"catalog_no":str,"qty":int}, ...]
    """
    with get_session() as session:
        # create sale with a 0.0 total
        sale = Sale(sale_date=sale_date, received_date=received_date,account_id=account_id, procuct_line_id=product_line_id, surgeon_id=surgeon_id, rep_id=rep_id, po_id=po_id, rstck_loc_id=rstck_loc_id, total_amt=0.0)
        session.add(sale)
        session.commit()
        session.refresh(sale)  # assigns a sale.id

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
                raise ValueError(f"No pricing for account: {account_id}, product: {product.catalog_no}")
            
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

def create_product(catalog_no: str, description:str, list_price: float, product_line_id: int) -> Product:
    with get_session() as session:
        product = Product(catalog_no=catalog_no, description=description, list_price=list_price, product_line_id=product_line_id)
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

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

def get_surgeon(surgeon_id:int) -> Surgeon:
    with get_session() as session:
        surgeon = session.get(Surgeon, surgeon_id)
        if surgeon is not None:
            return surgeon
        else:
            raise ValueError(f"No surgeon exists in db with id: {surgeon_id}")
    
def create_surgeon(name: str, npi_no: Optional[int]) -> Surgeon:
    with get_session() as session:
        surgeon = Surgeon(name=name, npi_no=npi_no)
        try:
            session.add(surgeon)
            session.commit()
            session.refresh(surgeon)
            return surgeon
        except IntegrityError:
            session.rollback()
            raise ValueError(f"Surgeon {surgeon.name} already exists in db")

def assign_surgeon_account(surgeon_id: int, account_id: int) -> SurgeonAccountLink:
    with get_session() as session:
        surgeon = get_surgeon(surgeon_id)
        account = get_account(account_id)
        surgeon_acct = SurgeonAccountLink(surgeon_id=surgeon_id,account_id=account_id)
        try:    
            session.add(surgeon_acct)
            session.commit()
            session.refresh(surgeon_acct)
            return surgeon_acct
        except IntegrityError:
            raise ValueError(f"Surgeon {surgeon.name} is already linked with account {account.name}")
    
def assign_surgeon_npi(surgeon_id:int, npi_no: int) -> Surgeon:
    with get_session() as session:
        surgeon = get_surgeon(surgeon_id)
        if surgeon == None:
            raise ValueError(f"No surgeon exists in db with id: {surgeon_id}")
        if npi_no is not None:
            try:
                surgeon.npi_no = npi_no
                session.add(surgeon)
                session.commit()
                session.refresh(surgeon)
                return surgeon
            except IntegrityError:
                session.rollback()
                raise ValueError(f"NPI Number {npi_no} is already assigned to surgeon {surgeon.id}")
        else:
            raise ValueError("Invalid NPI # entry, try again")

def list_surgeon_accounts(surgeon_id:int) -> List[Account]:
    with get_session() as session:
        surgeon = session.get(Surgeon, surgeon_id)
        if surgeon is not None:
            return surgeon.accounts
        else:
            raise ValueError((f"No surgeon exists in db with id: {surgeon_id}"))
        


#       
# SalesTeam
# 

def create_sales_team(name: str) -> SalesTeam:
    with get_session() as session:
        team = SalesTeam(name=name)
        session.add(team)
        session.commit()
        session.refresh(team)
        return team

# 
# Rep
# 

def create_rep(name: str, team_id: Optional[int])-> Rep:
    with get_session() as session:
        rep = Rep(name=name, team_id=team_id)
        session.add(rep)
        session.commit()
        session.refresh(rep)
        return rep

# 
# ProductLine
# 
def create_product_line(name: str, commision_rate:Optional[float])-> ProductLine:
    with get_session() as session:
        product_line = ProductLine(name=name, commision_rate=commision_rate)
        session.add(product_line)
        session.commit()
        session.refresh(product_line)
        return product_line
    
# 
# Location
# 

def create_location(name: str, address: str)-> Location:
    with get_session() as session:
        location = Location(name=name, address=address)
        session.add(location)
        session.commit()
        session.refresh(location)
        return location
from sqlmodel import SQLModel, create_engine, Session, select, col
from app.models.core import Account, Sale, SaleItem, Product, InventoryMovement, InventorySet, PurchaseOrder, SurgeonAccount, Surgeon, AccountProductPrice
from datetime import date
from app.db.database import engine




# create instance of Sale
def create_sale():
    sale_1 = Sale(sale_date= date(2025,1,1), account_id=1, surgeon_id=1,rep_id=1,rstck_loc_id=1,total_amt=100.00) 
    sale_2 = Sale(sale_date=date(2025,2,2), account_id=2, surgeon_id=2,rep_id=2,rstck_loc_id=2,total_amt=200.00) 
    # session.add stores records in memory, staged to be saved to db
    with Session(engine) as session:
        session.add(sale_1)
        session.add(sale_2)
        # session.commit stored the staged values in the db
        session.commit()

def select_sales():
    with Session(engine) as session:
        # select runs SQL SELECT on Sale table
        # session executes the statement in db 
        # select returns an iterable object
        # .all returns a list of results objects
        # sales = session.exec(select(Sale)).all()
        # print(sales)   

        # using .get() to select a row by id shortcut
        # sale = session.get(Sale, 1)
        # print(sale)
        ...
def update_sales():
    with Session(engine) as session:
        # start by selecting instance from table
        statement = select(Sale).where(Sale.sale_date == date(2025,1,1))
        results = session.exec(statement)
        sale = results.one()
        # update by setting the value (in memory)
        sale.account_id = 123456
        # use session.add and .commit to save change to db
        session.add(sale)
        session.commit()
        #  .refresh the newly saved in db object into memory
        session.refresh(sale)
        print("updated sale id: ", sale.id, "Account id to:", sale.account_id)

def delete_sale(): 
    with Session(engine) as session:
        statement = select(Sale).where(Sale.account_id == 123456)
        results = session.exec(statement)
        sale = results.one()
        print(f"deleting saleID# {sale.id}.......")
        session.delete(sale)
        session.commit()
        # deleted object sill exists in memory but not in db
        print(f"Deleted Sale: {sale}")
        



def main():
    create_sale()
    select_sales()
    update_sales()
    delete_sale()

if __name__ == "__main__":
    main()


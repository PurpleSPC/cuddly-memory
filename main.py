from sqlmodel import SQLModel, create_engine, Session
from app.models.core import Account, Sale, SaleItem, Product, InventoryMovement, InventorySet, PurchaseOrder, SurgeonAccount, Surgeon, AccountProductPrice

# creating db
sqlite_file_name = "database.db"
DATABASE_URL = f"sqlite:///{sqlite_file_name}"

engine = create_engine(DATABASE_URL, echo=True)

# initialize tables
def init_db():
    SQLModel.metadata.create_all(engine)

# create instance of Sale
def create_sale():
    sale_1 = Sale(sale_date=(2025,1,1), account_id=1, surgeon_id=1,rep_id=1,rstck_loc_id=1,total_amt=100.00) 
    sale_2 = Sale(sale_date=(2025,2,2), account_id=2, surgeon_id=2,rep_id=2,rstck_loc_id=2,total_amt=200.00) 
    # session.add stores records in memory, staged to be saved to db
    with Session(engine) as session:
        session.add(sale_1)
        session.add(sale_2)
        # session.commit stored the staged values in the db
        session.commit()

def main():
    init_db()
    create_sale()

if __name__ == "__main__":
    main()


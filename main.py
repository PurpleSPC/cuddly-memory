from sqlmodel import SQLModel, create_engine, Session
from app.models.core import Account, Sale, SaleItem, Product, InventoryMovement, InventorySet, PurchaseOrder, SurgeonAccount, Surgeon, AccountProductPrice

#########################
# creating db

sqlite_file_name = "database.db"
DATABASE_URL = f"sqlite:///{sqlite_file_name}"

engine = create_engine(DATABASE_URL, echo=True)

# initialize tables
def init_db():
    SQLModel.metadata.create_all(engine)

# simple session
def get_session():
    return Session(engine)

    
if __name__ == "__main__":
    init_db()
    print("success")
    


# db utilities and session management
from sqlmodel import SQLModel, create_engine, Session

# creating db
sqlite_file_name = "database.db"
DATABASE_URL = f"sqlite:///{sqlite_file_name}"
engine = create_engine(DATABASE_URL, echo=True)

# initialize tables
def init_db():
    SQLModel.metadata.create_all(engine)

# get session
def get_session():
    return Session(engine)
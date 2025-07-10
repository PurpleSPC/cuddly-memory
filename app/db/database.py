# db utilities and session management
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()
# creating db
DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL, echo=True)

# initialize tables
def init_db():
    SQLModel.metadata.create_all(engine)

# get session
def get_session():
    with Session(engine) as session:
        yield session
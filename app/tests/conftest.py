import pytest
import os
import sys
from sqlmodel import SQLModel, create_engine, Session
from app.db import database as db_module
from app.models import *

root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root not in sys.path:
    sys.path.insert(0,root)

@pytest.fixture(scope="session")
def engine():
    url = "sqlite:///:memory:"
    eng = create_engine(url, connect_args={"check_same_thread":False})
    SQLModel.metadata.create_all(eng)
    return eng

@pytest.fixture
def session(engine):
    with Session(engine) as sess:
        yield sess

@pytest.fixture(autouse=True)
def override_get_session(session, monkeypatch):
    """
    monkey patch get_session so tests use test session
    """
    monkeypatch.setattr(
        db_module,
        "get_session",
        lambda: session
    )

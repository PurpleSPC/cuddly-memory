from app.db.crud import create_account

def test_create_account(session):
    acct = create_account("Test Hospital", "123 Health St")
    assert acct.id is not None
    assert acct.name == "Test Hospital"
    assert acct.address == "123 Health St"
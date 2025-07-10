import pytest
from datetime import date

from app.db.crud import (
    create_account, 
    get_account,
    list_accounts,
    update_account,
    delete_account,
    get_account_by_name
    
)
from app.models import( Account,
                        Product, 
                        AccountProductPrice,
                        )

# 

def test_account_crud(session):

    # create
    acct = create_account("Test Hospital", "36 Mafia St")

    assert acct.id is not None
    assert acct.name == "Test Hospital"

    # read
    fetched = get_account(acct.id)
    assert fetched.id == acct.id
    assert fetched.address == "36 Mafia St"

    name_fetch = get_account_by_name("Test Hospital")
    assert name_fetch.id == acct.id

    # list
    all_accts = list_accounts()
    assert any(a.id == acct.id for a in all_accts)

    # update

    updated = update_account(acct.id, name="Renamed Correctly")
    assert updated.name == "Renamed Correctly"

    # delete

    delete_account(acct.id)
    with pytest.raises(ValueError) as exc_info:
        get_account(acct.id) 
    
    assert "No account exists" in str(exc_info.value)



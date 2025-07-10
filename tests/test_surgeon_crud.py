import pytest

def test_surgeon_crud(session):
    from app.db.crud import (
        create_surgeon,
        get_surgeon,
        assign_surgeon_account,
        assign_surgeon_npi,
        list_surgeon_accounts,
        create_account
    )

    # create surgeons correctly
    surgeon1 = create_surgeon("Sir Thomas Swinton", None)
    surgeon2 = create_surgeon("James Harthrop", 123456)

    assert surgeon1.id is not None
    assert surgeon1.name == "Sir Thomas Swinton"
    assert surgeon2.npi_no == 123456

    # create duplicate surgeon check for raised error
    with pytest.raises(ValueError) as exc_info:
        create_surgeon("Sir Thomas Swinton",None)

    assert "already exists" in str(exc_info.value)

    # test get_surgeon for known
    fetch_surgeon = get_surgeon(surgeon1.id)

    assert fetch_surgeon.id == surgeon1.id

    # test get_srugeon for invlaid id
    with pytest.raises(ValueError) as exc_info:
        wrong_surgeon = get_surgeon(789789789789789)

    assert "No surgeon exists" in str(exc_info)

    # assign surgeon to account correctly
    acct = create_account("Ortho Specialists of Uranus", "123 Devils Ave")
    acct2 = create_account("Venus Health Specialists", None)

    surg_account = assign_surgeon_account(surgeon1.id,acct.id)
    surg_account2 = assign_surgeon_account(surgeon1.id, acct2.id)

    assert surg_account.surgeon_id==surgeon1.id
    assert surg_account.account_id==acct.id
    assert surg_account2.surgeon_id==surgeon1.id
    assert surg_account2.account_id==acct2.id

    # assign surgeon invalid account id
    with pytest.raises(ValueError) as exc_info:
        inv_acct = assign_surgeon_account(surgeon2.id, 99999)

    assert "No account exists" in str(exc_info.value)


    # test list_surgeon_accounts
    surg_acct_list = list_surgeon_accounts(surgeon1.id)

    assert len(surg_acct_list) == 2        

    # assing npi correctly
    surg_npi = assign_surgeon_npi(surgeon1.id, 456)

    assert surg_npi.npi_no == 456

    # assign duplicate npi 
    with pytest.raises(ValueError) as exc_info:
        dup_npi = assign_surgeon_npi(surgeon2.id, 456)

    assert "already assigned" in str(exc_info.value)





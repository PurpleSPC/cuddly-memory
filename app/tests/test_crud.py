import pytest
from datetime import date
from sqlmodel import select

from app.db.crud import (
    create_account, list_accounts, get_account_by_name,
    create_sale_with_items, list_sales
)
from app.models import( Account,
                        Product, 
                        AccountProductPrice,
                        )

def test_create_and_list_accounts(session):
    # Create two accounts
    a1 = create_account("Alpha", "123 St")
    a2 = create_account("Beta", "456 Rd")

    all_accts = list_accounts()
    assert len(all_accts) == 2
    assert any(a.name == "Alpha" for a in all_accts)
    assert any(a.name == "Beta" for a in all_accts)

def test_get_account_by_name(session):
    acct = create_account("Gamma", None)
    found = get_account_by_name("Gamma")
    assert found.id == acct.id

def test_create_sale_with_items(session):
    # create account and product data
    acct = create_account("Delta", None)
    product = Product(catalog_no="SKU1", description="Test Item")
    session.add(product)
    session.commit()

    price_link = AccountProductPrice(
        account_id=acct.id, product_id=product.id, unit_price=9.99
    )
    session.add(price_link)
    session.commit()

    # create a sale with the data just created
    items = [
        {"catalog_no": "SKU1", "qty": 2},
    ]
    sale = create_sale_with_items(
        account_id=acct.id, sale_date=date.today(), items=items
    )

    # verify
    assert sale.id is not None
    assert len(list(sale.items)) == 2  # relationship populated
    assert sale.total_amt == round(5 * 9.99, 2)

def test_list_sales(session):
    # Ensure list_sales() returns at least the one created above
    sales = list_sales()
    assert isinstance(sales, list)
    assert any(sale.total_amt > 0 for sale in sales)
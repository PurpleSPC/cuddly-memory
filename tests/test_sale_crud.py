import pytest
from datetime import date

from app.db.crud import (
    create_sale,
    create_account,
    create_surgeon,
    create_sales_team,
    create_rep,
    create_location,
    create_product_line,
    create_product,
    update_account_price,
    add_item_to_sale,
    update_sale_total,
    list_sales,
    )

def test_create_sale(session):
    # create sample records
    
    acct   = create_account("Demo Hosp", "1 Clinic Rd")

    assert acct.id is not None
    assert acct.name == "Demo Hosp"

    surgeon   = create_surgeon("Dr. Who", None)

    assert surgeon.id is not None
    assert surgeon.name == "Dr. Who"
    
    team = create_sales_team("West Side Sharks")

    assert team.id is not None
    assert team.name == "West Side Sharks"
    
    rep = create_rep("Foo Bar", None)

    assert rep.id is not None
    assert rep.name == "Foo Bar"

    prod_line     = create_product_line("Devices", None)

    assert prod_line.id is not None
    assert prod_line.name == "Devices"

    prod1  = create_product("DEV100", "Widget A", 4.20, prod_line.id)
    prod2  = create_product("DEV200", "Widget B", 69, prod_line.id)

    assert prod1.id is not None
    assert prod1.catalog_no == "DEV100"
    assert prod2.description == "Widget B"
    assert prod2.product_line_id is not None
    assert prod1.list_price == 4.20
    
    # create pricing for account and product
    # pricing = set_account_prices_to_list(acct.id,prod_line.id)

    # assert pricing is not None
    # assert pricing[0].account_id == acct.id
    # assert pricing[0].unit_price == 4.20
    
    # update pricing for account and product
    price2 = update_account_price(acct.id, prod2.id, 123.32)

    assert price2.unit_price == 123.32

    loc = create_location("Hideout", "420 High St")

    assert loc.id is not None
    assert loc.address == "420 High St"

        
    # test create_sale function

    sale = create_sale(
        sale_date=date.today(),
        received_date=date.today(),
        account_id=acct.id,
        product_line_id=prod_line.id,
        surgeon_id=surgeon.id,
        rep_id=rep.id,
        rstck_loc_id=loc.id,
    )

    assert sale.id is not None

    # test list_sales
    sales = list_sales()

    assert sales[0].id is not None

# test add items to sale

    sale_item = add_item_to_sale(1, 1, 2)

    assert sale_item.qty == 2

# test update sale total

    assert sale.total_amt != 0.0



import streamlit as st
from sqlmodel import select
from app.db.database import get_session
from app.models.core import Sale

def view_sales_page():
    st.header("Sales Records")
    session = get_session()
    sales = session.exec(select(Sale).limit(10)).all()

    for sale in sales:
        st.write(f"📅 Sale Date: {sale.sale_date} | Account: {sale.account_id} | Surgeon: {sale.surgeon_id} | 💰 Total: ${sale.total_amt}")
import streamlit as st
from datetime import date
from sqlmodel import select
from app.db.database import get_session
from app.models.core import Sale, Account, Surgeon

def add_sale_page():
    st.header("Record a new Case")
    session = get_session()
    # looks up account name by account id 
    account_options = {account.id : account.name for account in session.exec(select(Account)).all()}
    selected_account = st.selectbox("Select Account", list(account_options.values()))
   
    surgeon_options = {surgeon.id : surgeon.name for surgeon in session.exec(select(Surgeon)).all()}
    selected_surgeon = st.selectbox("Select Surgeon", list(surgeon_options.values()))

    sale_date = st.date_input("Sale Date",value=date.today())
    received_date = st.date_input("Received Date",value=date.today())
    total_amt = st.number_input("Total Amount",value=420.69, min_value=0.0, )
    
    if st.button("Submit Sale"):
        new_sale = Sale(
            sale_date=sale_date,
            received_date=received_date,
            account_id=list(account_options.keys())[list(account_options.values().index(selected_account))],
            surgeon_id=list(surgeon_options.keys())[list(surgeon_options.values().index(selected_surgeon))],
            total_amt=total_amt
        )
        session.add(new_sale)
        session.commit()
        st.success("Sale Recorded")

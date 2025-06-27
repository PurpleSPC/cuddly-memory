# StreamLit UI entry point
import streamlit as st
from app.ui.pages import view_sales_page
from app.ui.pages.add_sale import add_sale_page
from app.ui.pages.manage_accounts import manage_accounts_page


# sidebar nav
menu = st.sidebar.selectbox("Choose an Option",["View Sales", "Add Sale", "Manage Accounts"])

if menu == "View Sales":
    view_sales_page()
elif menu == "Add Sale":
    add_sale_page()
elif menu == "Manage Accounts":
    manage_accounts_page()
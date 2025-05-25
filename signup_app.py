import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Path to your Excel file (must match actual file in repo)
excel_file = "isd_signup_data.xlsx"

# Load existing data if file exists
if os.path.exists(excel_file):
    df = pd.read_excel(excel_file)
else:
    df = pd.DataFrame(columns=[
        "Full Name", "Phone Number", "Residential Address", "Shop Name",
        "Employee Category", "Employee ID", "Bank Name", "Account Number",
        "IFSC Code", "UPI ID", "Password"
    ])

st.title("ISD Registration - Incentive Portal")

with st.form("signup_form"):
    full_name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    address = st.text_area("Residential Address")
    shop = st.text_input("Shop Name")
    category = st.selectbox("Employee Category", ["Hafele ISD", "Outlet Promoter"])
    emp_id = ""
    if category == "Hafele ISD":
        emp_id = st.text_input("Employee ID")
    bank = st.text_input("Bank Name")
    acc_no = st.text_input("Bank Account Number")
    ifsc = st.text_input("IFSC Code")
    upi = st.text_input("UPI ID")
    password = st.text_input("Create Password", type="password")
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        if not full_name or not phone or not address or not shop or not bank or not acc_no or not ifsc or not upi or not password:
            st.warning("Please fill in all the required fields.")
        else:
            new_entry = {
                "Full Name": full_name,
                "Phone Number": phone,
                "Residential Address": address,
                "Shop Name": shop,
                "Employee Category": category,
                "Employee ID": emp_id,
                "Bank Name": bank,
                "Account Number": acc_no,
                "IFSC Code": ifsc,
                "UPI ID": upi,
                "Password": password
            }
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            df.to_excel(excel_file, index=False)
            st.success("Registration submitted successfully!")

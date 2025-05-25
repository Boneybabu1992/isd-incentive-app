import streamlit as st
import pandas as pd
import os

# Title of the App
st.title("ISD Signup Portal – Häfele")

# Intro text
st.markdown("Please fill in your details below to register for the Häfele ISD Incentive Program.")

# Input fields
full_name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
address = st.text_area("Full Residential Address")
shop_name = st.text_input("Shop Name")
employee_category = st.selectbox("Employee Category", ["Select", "Häfele ISD", "Outlet Promoter"])

# Conditional field
employee_id = ""
if employee_category == "Häfele ISD":
    employee_id = st.text_input("Employee ID")

bank_name = st.text_input("Bank Name")
account_number = st.text_input("Bank Account Number")
ifsc_code = st.text_input("IFSC Code")
upi_id = st.text_input("UPI ID")
password = st.text_input("Create Password", type="password")

# Submit button
if st.button("Submit"):
    if (
        full_name and phone and address and shop_name and employee_category != "Select"
        and bank_name and account_number and ifsc_code and upi_id and password
    ):
        # Create a new row with the data
        new_data = {
            "Full Name": full_name,
            "Phone Number": phone,
            "Residential Address": address,
            "Shop Name": shop_name,
            "Employee Category": employee_category,
            "Employee ID": employee_id,
            "Bank Name": bank_name,
            "Account Number": account_number,
            "IFSC Code": ifsc_code,
            "UPI ID": upi_id,
            "Password": password
        }

        file_path = "isd_signup_data.xlsx"

        # Load existing file or create new
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            df = df.append(new_data, ignore_index=True)
        else:
            df = pd.DataFrame([new_data])

        # Save back to Excel
        df.to_excel(file_path, index=False)

        st.success("🎉 Registration Successful!")
    else:
        st.error("⚠️ Please fill all the required fields.")

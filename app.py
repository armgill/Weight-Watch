from datetime import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Weight Watch")
st.subheader("Log New Weight")

# Inputs
entryDate = st.date_input("Select Date")

entryWt = st.number_input("Enter Weight (lbs.)", min_value=0.0, step=0.1)
logBut = st.button("Log")

if logBut:
    entryDateTime = datetime.now()
    try:
        df = pd.read_csv("weight_log.csv")
        df["DateTime"] = pd.to_datetime(df["DateTime"])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["DateTime", "Weight"])

    new_entry = {"DateTime": entryDateTime, "Weight": entryWt}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

    df = df.sort_values("DateTime")
    df.to_csv("weight_log.csv", index=False)
    st.success("Weight logged successfully!")

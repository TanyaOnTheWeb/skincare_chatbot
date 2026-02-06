import streamlit as st
import pandas as pd

data = pd.read_csv("ingredients.csv")

st.title("🧴 Skincare Ingredient Chatbot")

problem = st.selectbox("Choose your skin problem:", data["Problem"])

used_before = st.radio(
    "Have you used skincare products before?",
    ["No", "Yes"]
)

product = ""
reaction = ""

if used_before == "Yes":
    product = st.text_input("Which product did you use?")
    reaction = st.radio("Did you face any reaction?", ["No", "Yes"])

if st.button("Get Advice"):
    row = data[data["Problem"] == problem]

    st.subheader("✅ Good ingredients")
    for col in ["Good_1", "Good_2", "Good_3", "Good_4"]:
        if pd.notna(row[col].values[0]):
            st.write("•", row[col].values[0])

    st.subheader("⚠ Avoid ingredients")
    for col in ["Avoid_1", "Avoid_2", "Avoid_3", "Avoid_4"]:
        if pd.notna(row[col].values[0]):
            st.write("•", row[col].values[0])

    if used_before == "Yes":
        if reaction == "Yes":
            st.warning("Noted! We'll be gentle with your routine.")
        else:
            st.success("Great! That product worked fine for you.")

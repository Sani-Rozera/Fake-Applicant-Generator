import streamlit as st
import pandas as pd
from faker import Faker

fake = Faker()

st.title("Fake Applicant Generator")

# Function to generate fake data
def generate_data(n):
    data = []
    for _ in range(n):
        data.append({
            "Name": fake.name(),
            "Email": fake.email(),
            "Phone": fake.phone_number(),
            "City": fake.city(),
            "Experience": fake.random_int(min=0, max=10),
            "Skills": ", ".join(fake.words(nb=5)),
            "Resume": fake.text(max_nb_chars=100)
        })
    return pd.DataFrame(data)

# Sidebar
st.sidebar.header("Controls")
num = st.sidebar.slider("Number of Applicants", 5, 50, 10)

if st.sidebar.button("Generate"):
    st.session_state["data"] = generate_data(num)

# Show table
if "data" in st.session_state:
    df = st.session_state["data"]

    st.subheader("Applicant Table")

    # Filter
    city = st.selectbox("Filter by City", ["All"] + list(df["City"].unique()))

    if city != "All":
        df = df[df["City"] == city]

    st.dataframe(df)

    # Download
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "Download CSV",
        csv,
        "applicants.csv",
        "text/csv"
    )
else:
    st.write("Click Generate to create applicants")
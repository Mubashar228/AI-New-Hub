import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI News Hub", layout="wide")
st.title("📰 AI News Hub — Latest News (Health, Tech, BBC)")

# Load combined CSV (3 sources)
@st.cache_data
def load_data():
    return pd.read_csv("combined_news.csv")  # df_all ka CSV

df = load_data()

# Sidebar - Category filter
st.sidebar.header("Filter News")
categories = df["category"].unique().tolist()
selected_category = st.sidebar.selectbox("Select Category", ["All"] + categories)

# Apply category filter
if selected_category != "All":
    filtered_df = df[df["category"] == selected_category]
else:
    filtered_df = df.copy()

# Search box
search = st.sidebar.text_input("Search Headlines")
if search:
    filtered_df = filtered_df[filtered_df["headline"].str.contains(search, case=False, na=False)]

# Display news
st.write(f"### Showing {len(filtered_df)} articles")
for idx, row in filtered_df.iterrows():
    st.markdown(f"#### [{row['headline']}]({row['url']})")
    st.caption(f"📰 Source: {row['source']} | 📂 Category: {row['category']}")
    st.markdown("---")

st.sidebar.info("Created by Mubashar Ul Hassan 🚀")

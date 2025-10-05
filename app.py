import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="AI News Hub", layout="wide")
st.title("📰 AI News Hub — Latest Daily News")

# Load combined news CSV
@st.cache_data
def load_data():
    return pd.read_csv("all_news_combined.csv")

df = load_data()

# Sidebar - filters
st.sidebar.header("Filters 🔍")
categories = df["category"].dropna().unique().tolist()
selected_category = st.sidebar.multiselect("Select Category", categories, default=categories)

# Keyword search
search_keyword = st.sidebar.text_input("Search Headlines / Keywords")

# Filter by category
filtered_df = df[df["category"].isin(selected_category)]

# Filter by search
if search_keyword:
    filtered_df = filtered_df[filtered_df["headline"].str.contains(search_keyword, case=False, na=False)]

# Sort by published date if available
if 'published' in filtered_df.columns:
    filtered_df = filtered_df.sort_values(by='published', ascending=False)

# Display news in cards
st.write(f"### Showing {len(filtered_df)} articles")

for idx, row in filtered_df.iterrows():
    with st.container():
        st.markdown(f"#### [{row['headline']}]({row['url']})")
        st.markdown(f"📰 Source: {row['source']} | 📂 Category: {row['category']} | 📅 Published: {row.get('published', 'N/A')}")
        st.markdown("---")

# Optional: show total articles count
st.sidebar.info(f"Total Articles: {len(filtered_df)}")

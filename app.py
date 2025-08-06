import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Zimbabwe News Clusters", layout="wide")

# Load data
df = pd.read_csv('clustered_articles.csv')

# Inject custom CSS for theme and navbar
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar {
            background-color: #0e1117;
            padding: 1rem 2rem;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .navbar h1 {
            color: white;
            font-size: 2rem;
            margin: 0;
        }
        .category-section {
            padding: 1.5rem;
            margin-bottom: 2rem;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .article-link {
            font-size: 1rem;
            color: #007bff;
        }
        .article-link:hover {
            text-decoration: underline;
        }
        .search-bar {
            padding: 10px 16px;
            width: 100%;
            font-size: 16px;
            border: 2px solid #ccc;
            border-radius: 10px;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
    <div class="navbar">
        <h1>📰 Zimbabwe🗞💥 News Clustered by Topic</h1>
    </div>
""", unsafe_allow_html=True)

# Search bar
search = st.text_input("🔍 Search Articles", "").lower()

# Group and show
for label in sorted(df['category'].unique()):
    filtered_df = df[df['category'] == label]

    if search:
        filtered_df = filtered_df[filtered_df['url'].str.lower().str.contains(search)]

    if not filtered_df.empty:
        st.markdown(f'<div class="category-section"><h3>📌 {label}</h3>', unsafe_allow_html=True)
        for _, row in filtered_df.iterrows():
            st.markdown(f"<a href='{row['url']}' class='article-link' target='_blank'>🔗 {row['url']}</a><br>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

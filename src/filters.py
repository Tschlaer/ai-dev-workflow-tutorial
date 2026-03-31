import pandas as pd
import streamlit as st


def render_sidebar(df: pd.DataFrame) -> dict:
    st.sidebar.header("Filters")

    min_date = df["date"].dt.date.min()
    max_date = df["date"].dt.date.max()
    start_date, end_date = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    all_categories = sorted(df["category"].unique().tolist())
    categories = st.sidebar.multiselect(
        "Category", options=all_categories, default=all_categories
    )

    all_regions = sorted(df["region"].unique().tolist())
    regions = st.sidebar.multiselect(
        "Region", options=all_regions, default=all_regions
    )

    return {
        "start_date": start_date,
        "end_date": end_date,
        "categories": categories,
        "regions": regions,
    }

import pandas as pd
import streamlit as st


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/sales-data.csv")
    df["date"] = pd.to_datetime(df["date"])
    required = {"date", "order_id", "category", "region", "total_amount"}
    missing = required - set(df.columns)
    if missing:
        st.error(f"Missing columns: {missing}")
        st.stop()
    return df


def filter_data(
    df: pd.DataFrame,
    start_date,
    end_date,
    categories: list,
    regions: list,
) -> pd.DataFrame:
    mask = df["date"].dt.date.between(start_date, end_date)
    df = df[mask]
    if categories:
        df = df[df["category"].isin(categories)]
    if regions:
        df = df[df["region"].isin(regions)]
    return df

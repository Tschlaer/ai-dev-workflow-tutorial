import pandas as pd
import streamlit as st


def render_kpis(df: pd.DataFrame) -> None:
    total_sales = df["total_amount"].sum()
    total_orders = df["order_id"].nunique()
    avg_order_value = total_sales / total_orders if total_orders else 0
    top_category = df.groupby("category")["total_amount"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Total Orders", f"{total_orders:,}")
    col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")
    col4.metric("Top Category", top_category)

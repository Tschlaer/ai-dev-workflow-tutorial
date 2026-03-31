import pandas as pd
import plotly.express as px
import streamlit as st

from src.theme import THEME


def render_trend(df: pd.DataFrame) -> None:
    granularity = st.radio("Granularity", ["Monthly", "Daily"], horizontal=True)
    rule = "ME" if granularity == "Monthly" else "D"

    trend = (
        df.set_index("date")["total_amount"]
        .resample(rule)
        .sum()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="date",
        y="total_amount",
        labels={"date": "Date", "total_amount": "Sales ($)"},
        title="Sales Trend",
        **THEME,
    )
    st.plotly_chart(fig, use_container_width=True)


def render_breakdowns(df: pd.DataFrame) -> None:
    col1, col2 = st.columns(2)

    by_category = (
        df.groupby("category")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    by_region = (
        df.groupby("region")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    with col1:
        fig_cat = px.bar(
            by_category,
            x="category",
            y="total_amount",
            labels={"category": "Category", "total_amount": "Sales ($)"},
            title="Sales by Category",
            **THEME,
        )
        st.plotly_chart(fig_cat, use_container_width=True)

    with col2:
        fig_reg = px.bar(
            by_region,
            x="region",
            y="total_amount",
            labels={"region": "Region", "total_amount": "Sales ($)"},
            title="Sales by Region",
            **THEME,
        )
        st.plotly_chart(fig_reg, use_container_width=True)

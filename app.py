import streamlit as st

from src.charts import render_breakdowns, render_trend
from src.data import filter_data, load_data
from src.filters import render_sidebar
from src.kpis import render_kpis

st.set_page_config(layout="wide", page_title="ShopSmart Sales Dashboard")
st.title("ShopSmart Sales Dashboard")

df = load_data()
filters = render_sidebar(df)
filtered_df = filter_data(df, **filters)

render_kpis(filtered_df)
render_trend(filtered_df)
render_breakdowns(filtered_df)

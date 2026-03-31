# Tasks: E-Commerce Analytics Dashboard

---

## ECOM-1 · Phase 1: Project Skeleton + Theme

**Task 1.1 — Initialize project with uv**
`ECOM-1`
Run `uv init` in the repo root. Add dependencies: `uv add streamlit pandas plotly`. Confirm `pyproject.toml` lists all three.
*Done when:* `uv run streamlit run app.py` launches without import errors.

**Task 1.2 — Create requirements.txt**
`ECOM-1`
Mirror pinned deps from uv into `requirements.txt` for Streamlit Cloud. Include `streamlit`, `pandas`, `plotly` with pinned versions.
*Done when:* `pip install -r requirements.txt` succeeds in a clean environment.

**Task 1.3 — Scaffold src/ package**
`ECOM-1`
Create `src/__init__.py` and empty module files: `data.py`, `filters.py`, `kpis.py`, `charts.py`, `theme.py`.
*Done when:* `from src import data` imports without error.

**Task 1.4 — Implement src/theme.py**
`ECOM-1` / `ECOM-7`
```python
import plotly.express as px
THEME = dict(
    template="plotly_white",
    color_discrete_sequence=px.colors.qualitative.Set2,
    font_family="sans-serif",
)
```
*Done when:* `from src.theme import THEME` returns a dict with the three keys.

**Task 1.5 — Create app.py stub**
`ECOM-1`
Set up page config and section placeholders:
```python
st.set_page_config(layout="wide", page_title="ShopSmart Sales Dashboard")
st.title("ShopSmart Sales Dashboard")
```
*Done when:* App opens in browser with title visible and no errors.

---

## ECOM-2 · Phase 2: Data Layer

**Task 2.1 — Implement load_data() in src/data.py** [X]
`ECOM-2`
Prescriptive:
```python
@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/sales-data.csv")
    df["date"] = pd.to_datetime(df["date"])
    required = {"date","order_id","category","region","total_amount"}
    missing = required - set(df.columns)
    if missing:
        st.error(f"Missing columns: {missing}")
        st.stop()
    return df
```
*Done when:* Returns DataFrame with 1,000 rows and correct dtypes; `st.stop()` fires if CSV is renamed.

**Task 2.2 — Implement filter_data() in src/data.py** [X]
`ECOM-2`
Prescriptive — apply filters in order:
1. Date: `df["date"].dt.date.between(start_date, end_date)`
2. Category: `df["category"].isin(categories)` (skip if list is empty)
3. Region: `df["region"].isin(regions)` (skip if list is empty)

*Done when:* Passing full date range + all categories + all regions returns the unmodified DataFrame. Passing a single category returns only rows for that category.

---

## ECOM-6 · Phase 3: Filters

**Task 3.1 — Implement render_sidebar() in src/filters.py**
`ECOM-6`
Descriptive: Build a sidebar with three controls using min/max values derived from the passed DataFrame. Return a dict: `{"start_date", "end_date", "categories", "regions"}`. Defaults show all data.
*Done when:* Sidebar renders with three controls; returned dict has correct keys and types; defaults produce no filtering.

**Task 3.2 — Wire filters into app.py**
`ECOM-6`
Call `load_data()`, pass to `render_sidebar()`, pass filter state to `filter_data()`, store result as `filtered_df`. Add temporary `st.write(filtered_df.shape)` to verify.
*Done when:* Narrowing the date range reduces the row count shown on screen. Remove the temporary `st.write` after verifying.

---

## ECOM-3 · Phase 4: KPI Cards

**Task 4.1 — Implement render_kpis() in src/kpis.py** [X]
`ECOM-3`
Prescriptive calculations:
- Total Sales: `df["total_amount"].sum()` → `f"${val:,.0f}"`
- Total Orders: `df["order_id"].nunique()` → `f"{val:,}"`
- Avg Order Value: Total Sales / Total Orders → `f"${val:,.2f}"`
- Top Category: `df.groupby("category")["total_amount"].sum().idxmax()`

Layout: `st.columns(4)`, one `st.metric` per column.
*Done when:* Unfiltered data shows Total Sales ~$650–700K, Total Orders 482. Filtering to one region changes all four values.

---

## ECOM-4 · Phase 5: Trend Chart

**Task 5.1 — Implement render_trend() in src/charts.py**
`ECOM-4`
Descriptive: Line chart of `total_amount` aggregated by date. Add a `st.radio(["Monthly", "Daily"])` toggle above the chart. Use `df.resample()` on the `date` column. Pass `**THEME` to `px.line()`.
*Done when:* Monthly view shows ~12 data points; Daily view shows ~365. Toggle switches between them without page error. Chart updates when filters change.

---

## ECOM-5 · Phase 5: Bar Charts

**Task 5.2 — Implement render_breakdowns() in src/charts.py**
`ECOM-5`
Descriptive: Two vertical `px.bar` charts in `st.columns(2)` — sales by category (sorted descending) and sales by region (sorted descending). Both use `**THEME`.
*Done when:* Both charts render side by side. Electronics or Audio is the top category. Bars re-sort correctly when filters reduce the data. Hover shows exact dollar values.

---

## ECOM-8 · Phase 6: Deploy

**Task 6.1 — Wire all components into app.py**
`ECOM-8`
Replace stubs with real calls in render order:
```python
df = load_data()
filtered_df = filter_data(df, **render_sidebar(df))
render_kpis(filtered_df)
render_trend(filtered_df)
render_breakdowns(filtered_df)
```
*Done when:* Full dashboard renders locally with no errors.

**Task 6.2 — Deploy to Streamlit Community Cloud**
`ECOM-8`
Push to GitHub. Connect repo in Streamlit Community Cloud. Set main file to `app.py`.
*Done when:* Public URL loads the dashboard; filters work; all charts render without errors in the cloud logs.

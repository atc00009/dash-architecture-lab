import os
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Dash & Multi-Library Master Lab", page_icon="⚡", layout="wide"
)

st.title("⚡ Dash Architecture, Flow, Multi-Library Lab & EcoMove Cockpit")
st.markdown(
    "Complete 7-tab interactive lab covering HTML vs Dash, hidden JS/React,"
    " Pandas/Plotly, JSON wire loop, multi-library line-by-line deep dive,"
    " EcoMove interactive design challenge, managerial justification guide, and"
    " 15-question mastery quiz."
)


# Safe data loader for EcoMove dataset with synthetic fallback
@st.cache_data
def load_ecomove_data():
  filename = "[5442] EcoMoveMobility.xlsx"
  if os.path.exists(filename):
    try:
      return pd.read_excel(filename)
    except Exception:
      pass
  # Fallback synthetic frame if excel not in root dir matching exact brief schema
  np.random.seed(42)
  dates = pd.date_range("2026-01-01", periods=60, freq="D")
  cities = ["Berlin", "Paris", "Madrid", "Amsterdam"]
  modes = ["Bus", "Metro", "Bike", "Tram"]
  rows = []
  for d in dates:
    for c in cities:
      for m in modes:
        rows.append({
            "Date": d,
            "City": c,
            "Transport_Mode": m,
            "Route_Type": (
                "Urban Core" if m in ["Metro", "Tram"] else "Suburban/Perimeter"
            ),
            "Passengers": np.random.randint(50, 400),
            "Trips": np.random.randint(5, 40),
            "Delay_Minutes": max(0, np.random.normal(12, 8)),
            "On_time_percentage": np.clip(np.random.normal(86, 7), 60, 100),
            "Ticket_Revenue": np.random.randint(800, 3500),
            "Operating_Cost": np.random.randint(700, 3000),
            "CO2_saved": np.random.randint(150, 900),
            "Energy_consumption": np.random.randint(400, 1800),
            "Customer_Rating": round(np.random.uniform(3.2, 5.0), 1),
            "Accessibility_complaints": np.random.randint(0, 8),
        })
  return pd.DataFrame(rows)


df = load_ecomove_data()

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "1. 🧩 HTML vs Dash & UI Components",
    "2. 📦 Hidden JS & Server (`app.run`)",
    "3. 🐼 Pandas & 📈 Plotly Roles",
    "4. 🔄 Complete Workflow & JSON Wire",
    "5. 🏛️ Dash vs St vs Bokeh vs Panel (Deep Dive)",
    "6. 🎯 EcoMove Challenge, Live Board & Justifications",
    "📝 7. 15-Question Master Quiz",
])

# --- TAB 1: HTML vs DASH & COMPONENTS ---
with tab1:
  st.header("1. HTML vs. Dash Comparison")
  st.markdown("""
| Feature / Behavior | HTML | Dash |
| :--- | :--- | :--- |
| **Primary Purpose** | Creates webpage structure | Creates interactive data applications |
| **UI Elements** | Headings, text, boxes, tables | Graphs, dropdowns, sliders, filters |
| **Data Analysis** | Doesn't analyse data | Can use Python to analyse data |
| **Python Execution** | Doesn't run Python | Connects the browser to Python |
| **Interactivity** | Interaction needs JavaScript | Dash provides much of the interaction for you |
""")
  st.divider()
  st.subheader("2. `dcc.Dropdown` & `dcc.Graph` Code Snippet")
  st.code(
      """
dcc.Dropdown(id="stock", options=[{"label": "Apple", "value": "AAPL"}], value="AAPL")
dcc.Graph(id="chart") # Empty container slot waiting for JSON figure
""",
      language="python",
  )
  st.info(
      '💡 **dcc.Graph meaning:** *"Dash, make a space for an interactive'
      ' graph."* Flow: `dcc.Graph()` → slot → Plotly math figure → Browser'
      ' JS paints pixels.'
  )

# --- TAB 2: HIDDEN JS & SERVER ---
with tab2:
  st.header("Where is JavaScript / React? (Hidden Background)")
  st.write(
      "When you run `pip install dash`, Plotly downloads pre-built"
      " React/JavaScript bundles into Python's `site-packages/dash`. You never"
      " write manual `.js` files."
  )
  st.code(
      """
from dash import Dash
app = Dash(__name__)
if __name__ == "__main__":
    app.run(debug=True, port=8050)
""",
      language="python",
  )
  st.markdown(
      "- **`app = Dash(__name__)`** initializes app core.\n- **`app.run()`**"
      " starts local Python HTTP web server waiting for browser requests."
  )

# --- TAB 3: PANDAS & PLOTLY ROLES ---
with tab3:
  st.header("What Pandas and Plotly Do Inside Python")
  c1, c2 = st.columns(2)
  with c1:
    st.subheader("🐼 Pandas Role")
    st.write(
        "Reads/downloads table rows/columns, filters dates, cleans"
        " multi-index/missing data."
    )
  with c2:
    st.subheader("📈 Plotly (`px`) Role")
    st.write(
        "Takes clean Pandas table, computes coordinate geometry (lines, axes,"
        " colors) into a `fig` object."
    )
  st.code(
      """
df = yf.download(selected_stock) # Pandas
fig = px.line(df, x="Date", y="Close") # Plotly
return fig
""",
      language="python",
  )

# --- TAB 4: COMPLETE WORKFLOW & JSON WIRE ---
with tab4:
  st.header("The Complete Loop: User Click → JSON → Python → JS Display")
  st.markdown("""
1. **User Action**: User clicks `MSFT` in dropdown.
2. **Hidden JS Event**: Browser's built-in Dash React/JS catches click, packages `{"stock": "MSFT"}` as light text JSON.
3. **HTTP Post**: Light JSON payload sent to local Python server port.
4. **Callback Trigger**: `@app.callback(Output("chart", "figure"), Input("stock", "value"))` runs Python function.
5. **Python Processing**: Pandas cleans table -> Plotly creates `fig`.
6. **Return JSON**: Python serializes `fig` to JSON and sends back over network wire.
7. **JS Display**: Browser's hidden React/Plotly-JS engine reads JSON and repaints graph pixels inside `dcc.Graph(id="chart")`. **No full page refresh!**
""")

# --- TAB 5: MULTI-LIBRARY DEEP DIVE (MATRIX + LINE-BY-LINE MEANINGS) ---
with tab5:
  st.header("🏛️ Architecture Matrix: Dash, Streamlit, Bokeh, Panel")
  st.markdown("""
| Feature / Concept | **Dash** | **Streamlit** | **Bokeh** | **Panel** |
| :--- | :--- | :--- | :--- | :--- |
| **Required Imports** | `dash`, `dash.html`, `dash.dcc`, `dash.Input/Output` | `streamlit as st` | `bokeh.plotting.figure`, `bokeh.models.*` | `panel as pn` |
| **App Creation** | `app = Dash(__name__)`, `app.layout = html.Div([...])`, `app.run()` | Top-to-bottom script execution (`st.title()`, `st.selectbox()`) | Create `p = figure()`, add glyphs `p.line()`, root doc | Build UI container `pn.Column/Row()`, embed widgets/panes |
| **Reactivity Model** | Explicit decorator `@app.callback(Output, Input)` matching component IDs | **No callbacks!** Entire script reruns top-to-bottom on widget change | Event listener subscription (`slider.on_change('value', fn)`) or `CustomJS` | Functional binding (`pn.bind(func, widget)`) or decorator (`@pn.depends`) |
""")

  st.divider()
  st.subheader("Code Snippets + Plain-English Line Meanings")

  col_d, col_s = st.columns(2)
  with col_d:
    st.markdown("### 1. Dash")
    st.code(
        """
app.layout = html.Div([dcc.Dropdown(id='s'), dcc.Graph(id='c')])
@app.callback(Output('c', 'figure'), Input('s', 'value'))
def update(val): return px.line(...)
app.run()
""",
        language="python",
    )
    st.markdown("""
    **Line-by-Line Meaning:**
    * `app.layout = ...`: Build HTML container + dropdown + graph slot.
    * `@app.callback(Output('c', 'figure'), Input('s', 'value'))`: Listen to dropdown id `'s'`, feed choice into `update()`, send output to graph id `'c'`.
    * `def update(val): ...`: Python function that computes new figure.
    * `app.run()`: Start local server port 8050.
    """)

  with col_s:
    st.markdown("### 2. Streamlit")
    st.code(
        """
val = st.selectbox('Choose', ['AAPL', 'MSFT'])
fig = px.line(...)
st.plotly_chart(fig)
# Changing dropdown reruns whole script from line 1
""",
        language="python",
    )
    st.markdown("""
    **Line-by-Line Meaning:**
    * `val = st.selectbox(...)`: Create dropdown UI and store user choice in `val`.
    * `fig = px.line(...)`: Create Plotly figure using current `val`.
    * `st.plotly_chart(fig)`: Render figure on page.
    * *Rerun rule*: Changing selection restarts Python script from **Line 1**. No separate callback code needed!
    """)

  st.divider()

  col_b, col_p = st.columns(2)
  with col_b:
    st.markdown("### 3. Bokeh")
    st.code(
        """
p = figure()
slider = Slider(start=1, end=10, value=5)
slider.on_change('value', lambda attr, old, new: update_glyph())
curdoc().add_root(column(slider, p))
""",
        language="python",
    )
    st.markdown("""
    **Line-by-Line Meaning:**
    * `p = figure()`: Give me an empty graph canvas.
    * `slider = Slider(...)`: Put an interactive slider widget.
    * `slider.on_change('value', lambda ...)`: Watch slider value; on change, run single-line lambda passing `(attr, old, new)` to `update_glyph()`.
    * `curdoc().add_root(column(slider, p))`: Put slider + graph vertically onto current page document.
    * *Glyph*: Visual mark (circle, line) representing data on chart.
    """)

  with col_p:
    st.markdown("### 4. Panel")
    st.code(
        """
select = pn.widgets.Select(options=['AAPL', 'MSFT'])
def plot(s): return px.line(...)
dashboard = pn.Column(select, pn.bind(plot, select))
dashboard.servable()
""",
        language="python",
    )
    st.markdown("""
    **Line-by-Line Meaning:**
    * `select = pn.widgets.Select(...)`: Create a dropdown widget.
    * `def plot(s): return px.line(...)`: Function taking selected stock string `s`.
    * `pn.bind(plot, select)`: Connect dropdown `select` output directly into `plot()` function.
    * `pn.Column(select, ...)`: Arrange select box and bound plot vertically.
    * `.servable()`: Make app deployable/displayable as a web service.
    """)

  st.divider()
  st.subheader("⚡ Quick Pattern Memory Guide")
  st.markdown("""
- **Dash**: `Dropdown → @app.callback → function → update graph`
- **Panel**: `Select → pn.bind() → function → update graph`
- **Bokeh**: `Slider → on_change() → function → update chart`
- **Streamlit**: `Widget changes → whole Python script reruns → new output`
""")

# --- TAB 6: ECOMOVE INTERACTIVE CHALLENGE, BOARD & JUSTIFICATIONS ---
with tab6:
  st.header(
      "🎯 EcoMove Assessment Challenge, Live Dashboard & Managerial Justifications"
  )
  st.markdown("Target Audience: **Senior Managers at EcoMove**.")

  if "unlocked_ecomove" not in st.session_state:
    st.session_state["unlocked_ecomove"] = False

  with st.form("challenge_step1"):
    st.subheader("Step 1: Test Your Planning Logic")
    sel_v = st.multiselect(
        "Select your 6 non-redundant chart types:",
        [
            "Time-series trend (demand/volume over time)",
            "Comparison chart (by city, country, or mode revenue/volume)",
            "Relationship scatter plot / correlation heatmap",
            "Distribution box plot / violin plot (delay spread)",
            "Performance indicator KPI bar/card summary",
            "Combined multi-view dashboard with interactive filter",
        ],
    )
    sel_kpi = st.multiselect(
        "Select core management KPIs:",
        [
            "Net Operating Margin (Revenue - Cost)",
            "Cost-to-Revenue Ratio",
            "Fleet On-Time %",
            "Mean Delay Minutes",
            "Total CO2 Abatement Saved",
            "Accessibility Complaints Index",
        ],
    )
    sub_btn = st.form_submit_button("Check Planning & Unlock Complete Board")

  if sub_btn:
    st.session_state["unlocked_ecomove"] = True

  if st.session_state["unlocked_ecomove"]:
    st.success(
        "🔓 **Blueprint Unlocked!** Complete interactive dashboard + Academic"
        " Managerial Justification Framework:"
    )

    selected_city = st.selectbox(
        "Filter Dashboard by City:",
        options=["All Cities"] + list(df["City"].unique()),
    )
    dff = (
        df
        if selected_city == "All Cities"
        else df[df["City"] == selected_city]
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    net_m = dff["Ticket_Revenue"].sum() - dff["Operating_Cost"].sum()
    c1.metric("Net Margin", f"€{net_m:,.0f}")
    c2.metric("On-Time %", f"{dff['On_time_percentage'].mean():.1f}%")
    c3.metric("Total CO2 Saved", f"{dff['CO2_saved'].sum():,.0f} kg")
    c4.metric(
        "Access Complaints", f"{dff['Accessibility_complaints'].sum():.0f}"
    )
    c5.metric("Total Passengers", f"{dff['Passengers'].sum():,.0f}")

    st.divider()

    st.subheader("📊 Live 6-Visualisation Composite Dashboard")
    g1, g2 = st.columns(2)
    with g1:
      ts = dff.groupby("Date")["Passengers"].sum().reset_index()
      st.plotly_chart(
          px.line(ts, x="Date", y="Passengers", title="1. Time-Series Trend"),
          use_container_width=True,
      )
    with g2:
      comp = (
          dff.groupby("Transport_Mode")["Ticket_Revenue"].sum().reset_index()
      )
      st.plotly_chart(
          px.bar(
              comp,
              x="Transport_Mode",
              y="Ticket_Revenue",
              title="2. Comparison: Revenue by Mode",
          ),
          use_container_width=True,
      )

    g3, g4 = st.columns(2)
    with g3:
      st.plotly_chart(
          px.scatter(
              dff.sample(min(200, len(dff))),
              x="Delay_Minutes",
              y="Customer_Rating",
              color="Transport_Mode",
              title="3. Relationship: Delay vs CSAT",
          ),
          use_container_width=True,
      )
    with g4:
      st.plotly_chart(
          px.box(
              dff,
              x="Transport_Mode",
              y="Delay_Minutes",
              title="4. Distribution: Delay Spread",
          ),
          use_container_width=True,
      )

    g5, g6 = st.columns(2)
    with g5:
      city_rev = dff.groupby("City")["Ticket_Revenue"].mean().reset_index()
      st.plotly_chart(
          px.bar(
              city_rev,
              x="City",
              y="Ticket_Revenue",
              title="5. Performance Indicator: Mean Revenue per City",
          ),
          use_container_width=True,
      )
    with g6:
      st.plotly_chart(
          px.histogram(
              dff,
              x="Delay_Minutes",
              color="Transport_Mode",
              title="6. Combined Multi-View: Delay Histogram",
          ),
          use_container_width=True,
      )

    st.divider()
    st.subheader(
        "📝 Managerial Justification & Design Rationale Guide (Task 2 Ready)"
    )
    st.markdown("""
| Visual / Component | Selected Encapsulation | Decision Pillar Addressed | Managerial Action Justification |
| :--- | :--- | :--- | :--- |
| **1. Time-Series Line** | Aggregated daily `Passengers` sum over `Date` with OLS trendline | Route Planning & Demand Forecasting | Exposes macro growth vs contraction curves; identifies whether seasonal shifts require fleet capacity expansion. |
| **2. Mode Comparison Bar** | Categorical aggregation of `Ticket_Revenue` by `Transport_Mode` | Investment Priorities | Highlights commercial viability; flags revenue-negative shared modes that require structural public operating subsidies. |
| **3. Relationship Scatter** | Multivariate mapping (`Delay_Minutes` vs `Customer_Rating`, color=mode) | Service Reliability & UX | Proves non-linear satisfaction decay when schedule delays exceed 15-minute thresholds on commuter corridors. |
| **4. Distribution Boxplot** | Quartile/interquartile spread of `Delay_Minutes` across modes | Service Reliability SLA Audit | Identifies tail-risk schedule unreliability (e.g., high variance on bus transit vs tight clustering on metro tracks). |
| **5. Performance Indicator Bar** | Mean revenue footprint broken down by `City` asset | Investment / Asset Allocation | Guides multi-city capital budgeting; reallocates CapEx from underperforming urban asset footprints to high-density hubs. |
| **6. Composite / Multi-View Filter** | Cross-filtering global city selector driving frequency distribution | Accessibility & Operational Equity | Enables cross-jurisdictional triage for low-performing transit links flagged with accessibility complaints. |
""")

# --- TAB 7: 15-QUESTION QUIZ ---
with tab7:
  st.header("📝 15-Question Mastery Check")
  with st.form("master_15q"):
    q1 = st.radio(
        "1. Where does JavaScript live in Dash?",
        [
            "Written manually in script.js",
            "Pre-packaged inside Python's dash package via pip install",
            "Compiled by browser OS",
        ],
    )
    q2 = st.radio(
        "2. What does pip install dash download?",
        [
            "Only math equations",
            "Dash framework + hidden React/JS frontend bundles",
            "An .exe desktop file",
        ],
    )
    q3 = st.radio(
        "3. What does app = Dash(__name__) do?",
        ["Deletes cache", "Initializes Dash app application core", "Opens Edge"],
    )
    q4 = st.radio(
        "4. What does app.run(port=8050) do?",
        [
            "Starts local Python web server waiting for browser requests",
            "Compiles C++",
            "Syncs Google Drive",
        ],
    )
    q5 = st.radio(
        "5. What is dcc.Graph(id='chart')?",
        [
            "Static PNG file",
            "Empty container slot in webpage waiting for chart JSON",
            "Database table",
        ],
    )
    q6 = st.radio(
        "6. Does Python draw graph pixels on screen?",
        [
            "Yes via GPU",
            "No, browser JavaScript/Plotly-JS reads JSON and paints pixels",
            "Yes matplotlib GUI",
        ],
    )
    q7 = st.radio(
        "7. What carries 'user picked MSFT' to Python?",
        ["Pickle binary", "Lightweight JSON text format message", "USB cable"],
    )
    q8 = st.radio(
        "8. What is Pandas' main job in a callback?",
        ["Animate CSS", "Clean, filter, and reshape table/stock rows", "Render H1"],
    )
    q9 = st.radio(
        "9. What is Plotly's main job in a callback?",
        [
            "Turn table numbers into chart coordinate/figure objects",
            "Connect Wi-Fi",
            "Parse JWT",
        ],
    )
    q10 = st.radio(
        "10. What format does Python return to browser for the graph figure?",
        ["Memory pointer", "JSON text format", "MP4 video"],
    )
    q11 = st.radio(
        "11. Does the whole web page refresh when a callback updates a graph?",
        [
            "Yes full reload like PHP",
            "No, only target component updates via async JSON loop",
            "Yes white flash",
        ],
    )
    q12 = st.radio(
        "12. Where does @app.callback Python code execute?",
        ["Chrome V8 engine", "On the Python server / backend computer", "Wi-Fi router"],
    )
    q13 = st.radio(
        "13. Why aren't JS files visible in your project folder?",
        ["Dash packages JS inside Python site-packages", "Browsers block JS", "Forgot import js"],
    )
    q14 = st.radio(
        "14. What matches Output('chart', 'figure') to UI?",
        ["Timestamp", "Component id='chart' defined in app.layout", "Username"],
    )
    q15 = st.radio(
        "15. What format is the network wire payload between browser and server?",
        ["Text-based JSON", "Magnetic audio", "Radio frequency"],
    )

    submitted = st.form_submit_button("Submit 15-Question Quiz")
    if submitted:
      ans_key = [
          (
              q1,
              "Pre-packaged inside Python's dash package via pip install",
          ),
          (
              q2,
              "Dash framework + hidden React/JS frontend bundles",
          ),
          (q3, "Initializes Dash app application core"),
          (
              q4,
              "Starts local Python web server waiting for browser requests",
          ),
          (
              q5,
              "Empty container slot in webpage waiting for chart JSON",
          ),
          (
              q6,
              (
                  "No, browser JavaScript/Plotly-JS reads JSON and paints"
                  " pixels"
              ),
          ),
          (q7, "Lightweight JSON text format message"),
          (q8, "Clean, filter, and reshape table/stock rows"),
          (
              q9,
              "Turn table numbers into chart coordinate/figure objects",
          ),
          (q10, "JSON text format"),
          (
              q11,
              "No, only target component updates via async JSON loop",
          ),
          (q12, "On the Python server / backend computer"),
          (
              q13,
              "Dash packages JS inside Python site-packages",
          ),
          (q14, "Component id='chart' defined in app.layout"),
          (q15, "Text-based JSON"),
      ]
      score = sum(1 for u, c in ans_key if u == c)
      st.markdown(f"### Score: **{score} / 15**")
      for i, (u, c) in enumerate(ans_key, 1):
        if u == c:
          st.success(f"Q{i}: ✅ Correct")
        else:
          st.error(f"Q{i}: ❌ Selected '{u}' | Expected '{c}'")
      if score == 15:
        st.balloons()

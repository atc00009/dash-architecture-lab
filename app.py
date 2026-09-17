import streamlit as st

st.set_page_config(
    page_title="Dash Master Flow & Lab", page_icon="⚡", layout="wide"
)

st.title("⚡ Dash Architecture, Flow & Multi-Library Matrix")
st.markdown(
    "Super simple guide connecting HTML vs. Dash, UI components, hidden"
    " React/JS, JSON wire carrier, Pandas/Plotly, full library comparison,"
    " complete workflow, and 15-question mastery quiz."
)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. 🧩 HTML vs Dash & UI Components",
    "2. 📦 Hidden JS & Server (`app.run`)",
    "3. 🐼 Pandas & 📈 Plotly Roles",
    "4. 🔄 Complete Workflow & JSON Wire",
    "5. 🏛️ Dash vs St vs Bokeh vs Panel",
    "📝 6. 15-Question Master Quiz",
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
  st.subheader("2. `dcc.Dropdown` — Very Simple")
  st.code(
      """
dcc.Dropdown(
    id="stock",
    options=[
        {"label": "Apple", "value": "AAPL"},
        {"label": "Microsoft", "value": "MSFT"}
    ],
    value="AAPL"
)
""",
      language="python",
  )
  st.text("Visual Preview:\nSelect a stock ▼\n────────────────\nApple\nMicrosoft")
  st.markdown(
      "- **`dcc`** → Dash Core Components\n- **`Dropdown`** → creates a dropdown"
      " menu\n- **`id=\"stock\"`** → gives the dropdown an ID so Dash can track"
      " it\n- **`options`** → choices available to the user"
  )

  st.divider()
  st.subheader("3. `dcc.Graph` — Very Simple")
  st.code('dcc.Graph(id="chart")', language="python")
  st.info(
      '💡 **Meaning:** *"Dash, please create a space on my webpage where I can'
      ' display an interactive graph."*\n\nFlow: `dcc.Graph()` → Dash creates'
      ' component slot → Plotly provides math figure → Browser JavaScript'
      ' displays pixels.'
  )

# --- TAB 2: HIDDEN JS & SERVER ---
with tab2:
  st.header("Where is JavaScript / React? (Hidden Background)")
  st.write(
      "When you run `pip install dash`, Plotly downloads pre-built"
      " React/JavaScript bundles into Python's `site-packages/dash`. You never"
      " write manual `.js` files."
  )

  st.subheader("Server & `localhost:8050` Snippet")
  st.code(
      """
from dash import Dash
app = Dash(__name__)
# ... layout & callbacks ...
if __name__ == "__main__":
    app.run(debug=True, port=8050)
""",
      language="python",
  )
  st.markdown(
      "- **`app = Dash(__name__)`** creates the app framework.\n- **`app.run()`"
      "** starts a local Python web server (`http://127.0.0.1:8050`).\n-"
      " **Server meaning:** A running Python process waiting for HTTP requests"
      " from your browser."
  )

# --- TAB 3: PANDAS & PLOTLY ROLES ---
with tab3:
  st.header("What Pandas and Plotly Do Inside Python")

  c1, c2 = st.columns(2)
  with c1:
    st.subheader("🐼 Pandas Role")
    st.markdown("""
- Reads tabular data (dates, open/close prices).
- Cleans, filters, reindexes, flattens multi-index columns.
- **Output:** Clean data rows (DataFrame).
""")
  with c2:
    st.subheader("📈 Plotly (`px`) Role")
    st.markdown("""
- Takes clean Pandas data table.
- Calculates visual geometry (line path, axis ranges, marker colors, title).
- **Output:** Plotly Figure object (`fig`).
""")

  st.code(
      """
# Inside a callback snippet:
df = yf.download(selected_stock) # Pandas downloads/cleans
fig = px.line(df, x="Date", y="Close") # Plotly computes chart figure
return fig
""",
      language="python",
  )

# --- TAB 4: COMPLETE WORKFLOW & JSON WIRE ---
with tab4:
  st.header("The Complete Loop: User Click → JSON → Python → JS Display")
  st.markdown("""
1. **User Action:** User clicks `MSFT` in `dcc.Dropdown`.
2. **Hidden JS Event:** Browser's built-in Dash React/JS catches the click.
3. **JSON Carrier Packet:** Browser packages payload `{"stock": "MSFT"}` as light text JSON over HTTP/port to Python server.
4. **Callback Trigger:** `@app.callback(Output("chart", "figure"), Input("stock", "value"))` runs Python function `update_chart("MSFT")`.
5. **Python Processing:** Pandas cleans table → Plotly creates `fig`.
6. **Return JSON:** Python serializes `fig` to JSON and sends back over network wire.
7. **JS Display:** Browser's hidden React/Plotly-JS engine receives JSON and repaints graph pixels inside `dcc.Graph(id="chart")`.
8. **No Page Refresh:** Whole page stays put; only the target component updates!
""")

  st.code(
      """
@app.callback(Output("chart", "figure"), Input("stock", "value"))
def update_chart(stock):
    # Python computes figure object...
    return fig # Serialized to JSON wire payload -> browser JS displays
""",
      language="python",
  )

# --- TAB 5: DASH VS STREAMLIT VS BOKEH VS PANEL MATRIX ---
with tab5:
  st.header("🏛️ Architecture Comparison: Dash, Streamlit, Bokeh, Panel")
  st.write(
      "Detailed breakdown of **Required Components**, **App Creation**, and"
      " **Callback / Reactivity** model for each tool:"
  )

  st.markdown("""
| Feature / Concept | **Dash** | **Streamlit** | **Bokeh** | **Panel** |
| :--- | :--- | :--- | :--- | :--- |
| **Required Components / Imports** | `dash`, `dash.html`, `dash.dcc`, `dash.Input/Output` | `streamlit as st` | `bokeh.plotting.figure`, `bokeh.models.*` | `panel as pn`, plotting panes |
| **How Creation is Done** | `app = Dash(__name__)`, assign `app.layout = html.Div([...])`, run via `app.run()` | Top-to-bottom script execution (`st.title()`, `st.selectbox()`) | Create `p = figure()`, add glyphs `p.line()`, display with `show()` or `curdoc()` | Build UI container `pn.Column/Row()`, embed widgets/panes |
| **Callback / Reactivity Model** | Explicit decorator `@app.callback(Output, Input)` tracking component IDs | **No callbacks!** Entire script reruns top-to-bottom on widget change | Event listener subscription (`slider.on_change('value', fn)`) or `CustomJS` | Functional binding (`pn.bind(func, widget)`) or decorator (`@pn.depends`) |
""")

  st.divider()
  st.subheader("Quick Snippet Comparison (Input → Chart Update)")

  col_d, col_s = st.columns(2)
  with col_d:
    st.markdown("**Dash (ID-Targeted Event Loop)**")
    st.code(
        """
app.layout = html.Div([dcc.Dropdown(id='s'), dcc.Graph(id='c')])
@app.callback(Output('c', 'figure'), Input('s', 'value'))
def update(val): return px.line(...)
app.run()
""",
        language="python",
    )
  with col_s:
    st.markdown("**Streamlit (Top-to-Bottom Rerun)**")
    st.code(
        """
val = st.selectbox('Choose', ['AAPL', 'MSFT'])
fig = px.line(...)
st.plotly_chart(fig)
# Changing dropdown reruns whole script from line 1
""",
        language="python",
    )

  col_b, col_p = st.columns(2)
  with col_b:
    st.markdown("**Bokeh (Plot-First + Observer)**")
    st.code(
        """
p = figure()
slider = Slider(...)
slider.on_change('value', lambda attr, old, new: update_glyph())
curdoc().add_root(column(slider, p))
""",
        language="python",
    )
  with col_p:
    st.markdown("**Panel (Widget-to-Func Binding)**")
    st.code(
        """
select = pn.widgets.Select(options=['AAPL', 'MSFT'])
def plot(s): return px.line(...)
dashboard = pn.Column(select, pn.bind(plot, select))
dashboard.servable()
""",
        language="python",
    )

# --- TAB 6: 15-QUESTION QUIZ ---
with tab6:
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
        ["Turn table numbers into chart coordinate/figure objects", "Connect Wi-Fi", "Parse JWT"],
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

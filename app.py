import streamlit as st

st.set_page_config(
    page_title="Dash Architecture Lab (Pure Python)",
    page_icon="⚡",
    layout="wide",
)

st.title("⚡ Dash Architecture & Flow Learning Lab")
st.markdown(
    "Explore how Python, Dash, React/JS, JSON, and the browser talk to each other—built with native Streamlit."
)

# Create native Streamlit tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "1. 📦 pip install dash",
        "2. 🌐 Server & localhost:8050",
        "3. 🌳 Layout → JSON → DOM",
        "4. 🔄 The Click Roundtrip & Analogy",
        "🔮 5. Knowledge Check Challenge",
    ]
)

# --- TAB 1 ---
with tab1:
  st.header("Step 1: What happens on pip install dash?")
  st.write(
      "Dash is a Python framework by Plotly. When you run `pip install dash`,"
      " you aren't just downloading code—you are downloading pre-compiled"
      " React/JavaScript bundles."
  )

  col1, col2 = st.columns(2)
  with col1:
    st.code(
        """
site-packages/
 └── dash/
      ├── dash_renderer/
      │    └── bundle.js  ← Pre-compiled React engine!
      └── dcc/
           └── dash_core_components.js  ← Dropdown/Graph React code
    """,
        language="text",
    )
  with col2:
    st.info(
        "💡 **Key Takeaway:** You don't write JavaScript because Plotly already"
        " compiled React/JS components and shipped them *inside* the Python"
        " package folder."
    )

# --- TAB 2 ---
with tab2:
  st.header("Step 2: Server Startup & Browser Handover")
  st.write(
      "When you write `app = Dash(__name__)` and `app.run()`, Python starts a"
      " local web server (Flask under the hood) on `http://127.0.0.1:8050`."
  )

  st.markdown("""
    ```text
    Browser goes to: [http://127.0.0.1:8050](http://127.0.0.1:8050)
          │
          ▼
    Python Server responds with:
     1. Empty HTML shell (<div id="react-root"></div>)
     2. Streamed pre-packaged Dash React/JS bundles (.js files) over HTTP!
          │
          ▼
    Browser memory now holds the live React/JS runtime engine.
    ```
    """)

# --- TAB 3 ---
with tab3:
  st.header("Step 3: Where does html.Div fit into React?")
  st.write("You write Pythonic structural objects instead of HTML files:")

  st.code(
      """
app.layout = html.Div([
    html.H1("Stock Dashboard"),
    dcc.Dropdown(id="stock", options=["AAPL", "MSFT"])
])
""",
      language="python",
  )

  st.markdown("""
    * **Python Side**: Evaluates `html.H1` into Python component objects.
    * **The Bridge**: Dash serializes that Python tree into a lightweight **JSON blueprint**.
    * **Browser/React Side**: React (which arrived in Tab 2) reads the JSON blueprint, calls `React.createElement('h1', ...)`, and mutates the browser DOM.
    """)

# --- TAB 4 ---
with tab4:
  st.header("Step 4: User clicks 'MSFT' & The Restaurant Analogy")
  st.write(
      "When a user picks `MSFT`, browser JS packages `{'stock': 'MSFT'}` as"
      " JSON and sends it to the Python server callback."
  )

  st.warning("""
    🍽️ **The Restaurant Analogy:**
    * **Browser = Customer** ("I want MSFT data!")
    * **Python Server Port = Waiter** (carries the JSON order ticket)
    * **Python Callback / Pandas / Plotly = Kitchen** (fetches data, cooks graph figure)
    * **JSON = Order/Food Tray** (lightweight text data format crossing the wire)
    * **Browser JavaScript = Food Presenter** (paints fresh chart pixels into `dcc.Graph` SVG slot without refreshing the page!)
    """)

# --- TAB 5 ---
with tab5:
  st.header("🔮 Interactive Knowledge Check")

  q1 = st.radio(
      "1. Why don't you write raw JavaScript for a Dash dropdown?",
      [
          "Because Python compiles directly to WebAssembly bytecode",
          "Because Dash pre-packages compiled React/JS bundles inside the Python package",
          "Because web browsers block JavaScript inside Python environments",
      ],
  )

  q2 = st.radio(
      "2. What payload format travels between Python Server and Browser during a callback?",
      ["Pickle binary bytes", "JSON text format", "Raw .py files"],
  )

  if st.button("Check Answers"):
    score = 0
    if (
        q1
        == "Because Dash pre-packages compiled React/JS bundles inside the Python package"
    ):
      score += 1
    if q2 == "JSON text format":
      score += 1

    st.success(f"You scored {score}/2!")
    if score == 2:
      st.balloons()
      st.write("🎉 Mastered! You understand the full architectural boundary.")

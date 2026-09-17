import streamlit as st

st.set_page_config(
    page_title="Super Simple Dash Flow & 15-Q Quiz", page_icon="⚡", layout="wide"
)

st.title("⚡ Dash Made Super Simple: Under the Hood & Interactive Lab")
st.markdown(
    "**Goal:** Understand how Dash talks, where hidden JavaScript lives, what Pandas/Plotly do, and test your knowledge with 15 questions!"
)

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. 📦 The Hidden Magic",
    "2. 🧱 Core Dash Code",
    "3. 🐼 Pandas & 📈 Plotly Roles",
    "4. 🔄 The Click & JSON Loop",
    "📝 5. Master Quiz (15 Qs)",
])

# --- TAB 1: HIDDEN MAGIC ---
with tab1:
  st.header("Step 1: What happens when you do pip install dash?")
  st.write(
      "When you run `pip install dash`, Python downloads a big box of tools."
      " **Hidden inside that box** are pre-written JavaScript and React files."
  )

  col1, col2 = st.columns(2)
  with col1:
    st.info("🧠 **The Big Secret**\nYou **do not** write HTML, CSS, or"
            " JavaScript.\nDash already installed the browser-side JavaScript"
            " engine *for* you inside Python's storage folder.")
  with col2:
    st.code(
        """
Python hard drive folder after pip install dash:
site-packages/
 └── dash/
      ├── render.js  (Hidden React/JS engine)
      └── dcc/
           └── dropdown.js (Hidden dropdown JS)
""",
        language="text",
    )

# --- TAB 2: CORE DASH CODE ---
with tab2:
  st.header("Step 2: The Main Steps to Create a Dash App")
  st.write(
      "Here is the tiny core skeleton of a Dash app using `dcc.Graph`, layouts,"
      " and callbacks:"
  )

  st.code(
      """
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. Create app & start server
app = Dash(__name__)

# 2. Build layout (HTML & dcc.Graph slots)
app.layout = html.Div([
    html.H1("My Stock App"),
    dcc.Dropdown(["AAPL", "MSFT"], "AAPL", id="stock-box"),
    dcc.Graph(id="my-chart") # Empty visual container slot
])

# 3. Connect user action to Python calculation via Callback
@app.callback(
    Output("my-chart", "figure"),
    Input("stock-box", "value")
)
def update_chart(chosen_stock):
    # Python does work here...
    pass

# 4. Run the web server
if __name__ == "__main__":
    app.run(debug=True, port=8050)
""",
      language="python",
  )

# --- TAB 3: PANDAS & PLOTLY ---
with tab3:
  st.header("Step 3: What do Pandas and Plotly do inside Python?")
  st.write("When a user picks a stock, Python runs your callback function.")

  colA, colB = st.columns(2)
  with colA:
    st.subheader("🐼 Pandas Role")
    st.write(
        "- Fetches or reads table rows/columns (Dates, Prices).\n- Cleans"
        " empty rows, renames columns, or filters by date.\n- Output:"
        " **A clean table (DataFrame)**."
    )
  with colB, colb if 'colb' in locals() else st.container():
    st.subheader("📈 Plotly (`px`) Role")
    st.write(
        "- Takes the clean Pandas table.\n- Computes math coordinates:"
        " *Where do lines go? What color is the axis? What is the title?*\n-"
        " Output: **A Plotly Figure object**."
    )

# --- TAB 4: THE CLICK & JSON LOOP ---
with tab4:
  st.header("Step 4: The Complete Roundtrip (Click to Screen)")
  st.markdown("""
1. **User clicks `MSFT`** in the dropdown on the webpage.
2. **Hidden JavaScript (in browser)** catches the click. JS says: *"User picked MSFT!"*
3. **JSON carrier packet** wraps info: `{"stock": "MSFT"}` and sends it over local network/port to Python server.
4. **Python Server Callback wakes up**, runs Pandas + Plotly, makes a new chart figure object.
5. **Python packs figure to JSON**, sends it *back* to browser over the network wire.
6. **Hidden JavaScript (in browser)** receives the JSON, reads the coordinates, and **draws/paints the graph pixels** inside `dcc.Graph`.
7. **No page refresh!** Only the graph updates smoothly.
""")

# --- TAB 5: 15-QUESTION QUIZ ---
with tab5:
  st.header("📝 15-Question Master Knowledge Check")
  st.write(
      "Test your understanding of Dash hidden mechanics, JSON, Pandas, Plotly,"
      " and code structure."
  )

  with st.form("master_quiz_form"):
    q1 = st.radio(
        "1. Where does JavaScript live when using Dash?",
        [
            "You write it in a separate script.js file",
            "Pre-packaged inside the Python dash library via pip install",
            "Generated live by your web browser operating system",
        ],
    )

    q2 = st.radio(
        "2. What does pip install dash download?",
        [
            "Only plain Python math functions",
            "Dash framework plus hidden React/JavaScript frontend bundles",
            "A compiled .exe desktop application",
        ],
    )

    q3 = st.radio(
        "3. What does app = Dash(__name__) do?",
        [
            "Deletes old cache files",
            "Initializes the Dash app application core",
            "Opens Microsoft Edge browser automatically",
        ],
    )

    q4 = st.radio(
        "4. What does app.run(debug=True, port=8050) do?",
        [
            "Starts a local Python web server waiting for browser requests",
            "Compiles Python into C++ machine code",
            "Uploads your code to Google Drive",
        ],
    )

    q5 = st.radio(
        "5. What is dcc.Graph(id='my-chart') in the layout?",
        [
            "An image file stored on your desktop",
            "An empty container slot in the web page waiting for chart JSON",
            "A database connection string",
        ],
    )

    q6 = st.radio(
        "6. Does Python draw the graph pixels on your computer screen?",
        [
            "Yes, Python GPU draws the SVG pixels directly",
            "No, browser JavaScript/Plotly-JS reads JSON and paints pixels",
            "Yes, via matplotlib GUI windows",
        ],
    )

    q7 = st.radio(
        "7. What carries the message 'user picked MSFT' from browser to Python?",
        [
            "Raw Python pickle binary code",
            "Lightweight JSON text format message",
            "A USB serial cable signal",
        ],
    )

    q8 = st.radio(
        "8. What is Pandas' main job inside a callback?",
        [
            "Animate CSS page transitions",
            "Clean, filter, and reshape table/stock data rows",
            "Render HTML <h1> headings",
        ],
    )

    q9 = st.radio(
        "9. What is Plotly's main job inside a callback?",
        [
            "Turn table numbers into chart coordinate/figure objects",
            "Connect to Wi-Fi routers",
            "Parse JSON web tokens",
        ],
    )

    q10 = st.radio(
        "10. What format does Python return to the browser for the graph figure?",
        ["Raw python object memory pointer", "JSON text format", "An MP4 video file"],
    )

    q11 = st.radio(
        "11. Does the whole web page refresh when a callback updates a graph?",
        [
            "Yes, browser reloads full HTML like traditional PHP/Flask apps",
            "No, only the target component updates via async JSON loop",
            "Yes, screen flashes white every time",
        ],
    )

    q12 = st.radio(
        "12. Where does @app.callback Python code execute?",
        [
            "Inside Google Chrome V8 engine",
            "On the Python server / backend computer",
            "Inside the Wi-Fi router firmware",
        ],
    )

    q13 = st.radio(
        "13. Why don't you see JavaScript files in your project directory?",
        [
            "Because Dash hides/packages JS inside the Python site-packages",
            "Because browsers don't support JavaScript anymore",
            "Because you forgot to write import js",
        ],
    )

    q14 = st.radio(
        "14. What matches an Output('my-chart', 'figure') to the UI?",
        [
            "The file creation timestamp",
            "The component id='my-chart' defined in app.layout",
            "The computer login username",
        ],
    )

    q15 = st.radio(
        "15. What format is the network wire payload between browser and server?",
        ["Text-based JSON", "Magnetic tape audio", "Bluetooth radio frequency"],
    )

    submitted = st.form_submit_button("Submit Answers & Check Score")

    if submitted:
      score = 0
      answers = [
          (
              q1,
              "Pre-packaged inside the Python dash library via pip install",
          ),
          (
              q2,
              "Dash framework plus hidden React/JavaScript frontend bundles",
          ),
          (q3, "Initializes the Dash app application core"),
          (
              q4,
              "Starts a local Python web server waiting for browser requests",
          ),
          (
              q5,
              "An empty container slot in the web page waiting for chart JSON",
          ),
          (
              q6,
              (
                  "No, browser JavaScript/Plotly-JS reads JSON and paints"
                  " pixels"
              ),
          ),
          (q7, "Lightweight JSON text format message"),
          (q8, "Clean, filter, and reshape table/stock data rows"),
          (
              q9,
              "Turn table numbers into chart coordinate/figure objects",
          ),
          (q10, "JSON text format"),
          (
              q11,
              "No, only the target component updates via async JSON loop",
          ),
          (q12, "On the Python server / backend computer"),
          (
              q13,
              (
                  "Because Dash hides/packages JS inside the Python"
                  " site-packages"
              ),
          ),
          (q14, "The component id='my-chart' defined in app.layout"),
          (q15, "Text-based JSON"),
      ]

      for i, (user_ans, correct_ans) in enumerate(answers, 1):
        if user_ans == correct_ans:
          score += 1
          st.success(f"Q{i}: ✅ Correct!")
        else:
          st.error(
              f"Q{i}: ❌ Your answer: '{user_ans}' | **Correct answer:**"
              f" '{correct_ans}'"
          )

      st.markdown(f"### Final Score: **{score} / 15**")
      if score == 15:
        st.balloons()
        st.success("🏆 Mastered! You know the complete Dash architecture flow!")

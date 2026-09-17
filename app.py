import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id="kpi-indicator-graph"),
        dcc.Dropdown(
            id="city-filter",
            options=["All", "Berlin", "Paris"],
            value="All",
        ),
    ]
)


@app.callback(
    Output("kpi-indicator-graph", "figure"), Input("city-filter", "value")
)
def update_indicator(city):
  val = 45000 if city == "All" else 12000
  ref = 40000

  fig = go.Figure(
      go.Indicator(
          mode="number+delta",
          value=val,
          delta={"reference": ref, "relative": True, "valueformat": ".1%"},
          title={"text": "Net Operating Margin"},
      )
  )
  fig.update_layout(height=200, margin=dict(t=20, b=20, l=20, r=20))
  return fig

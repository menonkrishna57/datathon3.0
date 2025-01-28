import datetime
import yfinance as yf
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
app = dash.Dash()
app.title = "Stock Visualisation"
app.layout = html.Div(children=[
    html.H1("Stock Visualisation Dashboard"),
    html.H4("Please enter the stock name"),
    dcc.Input(id='input', value='AAPL', type='text'),
    html.Div(id='output-graph')
])
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from dash.dependencies import Input, Output

# function which gives data
from server import return_data, return_volatility_data

# initialising the app
app = dash.Dash(__name__)


app.layout =html.Div([

    html.H1("Volatility", style={'text-align': 'center'}),

    dcc.Dropdown(id="select_stock", 
                options=[
                    {"label": 'RELIANCE', "value":738561},
                    {"label":"NIFTY 50", "value":256265},
                    {"label": 'WIPRO', "value":969473}],
                multi=False, 
                placeholder="Select the stock",
                value=256265,
                # style={"width":"40%"},
                ),

    html.Div(id="volatility_info", children=[]),

    dcc.Graph(id="line_graph")


])

@app.callback(
    [dash.dependencies.Output("line_graph", "figure"),dash.dependencies.Output("volatility_info", "children")],
    [dash.dependencies.Input("select_stock", "value")]
)
def update_volatility(option_selected):
    # data=kite.historical_data(option_selected,"2015-01-01", "2015-06-01", "15minute")
    # # print(data)
    # df=pd.DataFrame.from_dict(data)
    df, daily_std=return_volatility_data(option_selected)

    container=" The Daily Volatility of the selected stock is:{} % ".format(round(daily_std,2))

    figure=px.line(df, x="date", y="close")


    return figure, container


if __name__ == "__main__":
    app.run_server(debug=True)
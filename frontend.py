import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

from dash.dependencies import Input, Output

# function which gives data
from server import return_data

# initialising the app
app = dash.Dash()


layout = go.Layout(
    title=dict(
        text="Reliance",
        font_family="Arial",
        font_size=30,
        x=0.07,  # x placement of title
        y=0.88,  # y placement of title
    ),
    #size of the chart
    width=1920,
    height=1080,
    xaxis=dict(
        # type="category",
        # showgrid=False,
        zeroline=False,
        gridwidth=0.1,
        gridcolor="#242424",
        rangeslider=dict(visible=False,),
        nticks=10,
        tickfont=dict(size=20),
        tickcolor="black",
        linewidth=15,  # width of the xaxis
        ticks="outside",
        # tickcolor="#59d91e",
        # tickwidth=55,
        # ticklen=60
        # type="date"
        # showspikes=True, #vertical line to the axis like how they have in kite
        # range=["2021-04-25", "2021-05-30"]
        rangebreaks=[
        dict(bounds=[16,9], pattern="hour"), #hide hours outside of 9am-5pm
    ]
    

    ),
    yaxis=dict(
        # showgrid=False,
        zeroline=False,
        gridwidth=0.1,
        gridcolor="#242424",
        nticks=25,
        tickfont=dict(size=20),
        linewidth=15,
        tickcolor="black",
        ticks="outside",
        # showspikes=True,
    ),
    paper_bgcolor="white",  # sets the colour behind the plot
    plot_bgcolor="#181818",
    hovermode=False, #can turn the hover false too,
    margin= {
      "b": 300,
      }
)


# accessing the data
df = return_data()





trace1 = {
    "x": df["date"],
    "open": df["open"],
    "high": df["high"],
    "low": df["low"],
    "close": df["close"],
    "type": "candlestick",
    "increasing_line_color": "#53b987",
    "increasing_fillcolor": "#53b987",
    "decreasing_line_color": "#eb4d5c",
    "decreasing_fillcolor": "#eb4d5c",
}

trace2 = {
    "x": df["date"],
    "y": df["close"],
    "type": "scatter",
    "line": {"dash": "solid", "color": "rgba(253, 253, 0, 1.0)", "width": 1.3},
}

data = [trace1]
fig = go.Figure(data=data, layout=layout)
# fig.update_layout(xaxis_range=["2021-04-25", "2021-05-30"])
fig.update_xaxes(
    rangebreaks=[
        # dict(bounds=[17, 9], pattern="hour"), #hide hours outside of 9am-5pm
        dict(bounds=[17,9], pattern="hour")
    ]
)

app.layout = html.Div(
    html.Div([
        dcc.Graph(id="basic-candlestick", figure=fig, config={'scrollZoom':True},),
        dcc.Interval(
            id="interval-component",
            interval=20*1000,
            n_intervals=0
        )
    ])
)

fig.update_xaxes(
    rangebreaks=[
        # dict(bounds=[17, 9], pattern="hour"), #hide hours outside of 9am-5pm
        dict(bounds=[17,9], pattern="hour")
    ]
)

@app.callback(Output('basic-candlestick', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_chart(n):
    new_df=return_data()
    trace1 = {
    "x": new_df["date"],
    "open": new_df["open"],
    "high": new_df["high"],
    "low": new_df["low"],
    "close": new_df["close"],
    "type": "candlestick",
    "increasing_line_color": "#53b987",
    "increasing_fillcolor": "#53b987",
    "decreasing_line_color": "#eb4d5c",
    "decreasing_fillcolor": "#eb4d5c",
    }
    return {'data':[trace1], 'layout':layout}

if __name__ == "__main__":
    app.run_server(debug=True)


# children=[dcc.Graph(id="basic-candlestick", figure=fig)]
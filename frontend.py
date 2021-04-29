import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

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
        type="category",
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
    ),
    paper_bgcolor="white",  # sets the colour behind the plot
    plot_bgcolor="#181818",
    # hovermode=Fasle #can turn the hover false too,
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

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
# fig.update_layout(xaxis_range=["01-04-2020", "01-01-2021"])

app.layout = html.Div(children=[dcc.Graph(id="basic-candlestick", figure=fig)])

if __name__ == "__main__":
    app.run_server(debug=True)

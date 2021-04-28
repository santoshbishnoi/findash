import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
# )

# fig = px.line(df, x="Date", y="AAPL.High")
# print(df["Date"][0])

# # Use date string to set xaxis range
# fig.update_layout(
#     xaxis_range=["2016-02-07", "2016-12-31"], title_text="Manually Set Date Range"
# )
# fig.show()





from backend.server import return_data

df=return_data()
print(df)

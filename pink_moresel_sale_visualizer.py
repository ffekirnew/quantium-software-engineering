# Run this app with `python pink_moresel_sale_visualizer.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

CSV_FILE = './curated_data.csv'

app = Dash(__name__)

df = pd.read_csv(CSV_FILE)

line_graph = px.line(df, x='date', y='sales', color='region', hover_name='sales')

app.layout = html.Div(children=[
    html.H1(children="Soul Food's Pink Morsel Sale Visualization"),
    dcc.Graph(
        id='soul-food-change-outcomes',
        figure=line_graph
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

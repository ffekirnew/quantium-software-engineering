# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('./data/curated_data.csv')

fig = px.line(df, x='date', y='sales', color='region', hover_name='sales')

app.layout = html.Div(children=[
    html.H1(children="Soul Food's Pink Morsel Sale Visualization"),
    dcc.Graph(
        id='soul-food-change-outcomes',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

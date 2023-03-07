# Run this app with `python pink_moresel_sale_visualizer.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

CSV_FILE = './curated_data.csv'

app = Dash(__name__)

df = pd.read_csv(CSV_FILE)

regions = ['all', 'north', 'south', 'east', 'west']

figures = {}
for region in regions:
    if region == 'all':
        region_df = df
    else:
        region_df = df.query(f'region=="{region}"')
    figures[region] = px.line(region_df, x='date', y='sales', color='region', hover_name='sales')

app.layout = html.Div(children=[
    html.H1(
        children="Soul Food's Pink Morsel Sale Visualization",
        style={
            "fontSize" : 32,
            "fontFamily": "Arial",
            "textAlign": 'center'
        }),
    dcc.RadioItems(
        id='region-radio',
        options=[{'label': region.capitalize(), 'value': region} for region in regions],
        value='all',
        labelStyle={
            'padding': '2px',
            'display': 'inline-block',
            'margin-right': '10px',
            'align': 'center'
        }
    ),
    dcc.Graph(
        id='soul-food-change-outcomes'
    ),
], style={
    'fontFamily': 'Arial',
    'textAlign': 'center',
})


@app.callback(
    Output(component_id='soul-food-change-outcomes', component_property='figure'),
    Input(component_id='region-radio', component_property='value')
)
def update_output_figure(region_name):
    return figures[region_name]


if __name__ == '__main__':
    app.run_server(debug=True)

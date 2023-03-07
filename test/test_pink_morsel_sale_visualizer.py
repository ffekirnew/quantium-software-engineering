from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Import the names of callback functions you want to test
from pink_moresel_sale_visualizer import update_output_figure

def test_update_figure_callback_true():
    CSV_FILE = './curated_data.csv'
    df = pd.read_csv(CSV_FILE)
    output = update_output_figure('north')
    assert output == px.line(df.query(f'region=="north"'), x='date', y='sales', color='region', hover_name='sales')

def test_update_figure_callback_false():
    CSV_FILE = './curated_data.csv'
    df = pd.read_csv(CSV_FILE)
    output = update_output_figure('south')
    assert output != px.line(df.query(f'region=="north"'), x='date', y='sales', color='region', hover_name='sales')
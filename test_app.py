import pytest
from dash import Dash
from app import app  # assumes your Dash app is in app.py

def test_title_is_correct(dash_duo):

    dash_duo.start_server(app)

    title = dash_duo.find_element("h1")
    assert title.text == "Sales Over Time For Pink Morsel"

def test_radio_present(dash_duo):
    dash_duo.start_server(app)

    try:
        radio = dash_duo.find_element("#region-selector")
        exists = True
    except Exception:
        exists = False

    assert exists == True


def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    try:
        radio = dash_duo.find_element("#pink-morsel-graph")
        exists = True
    except Exception:
        exists = False

    assert exists == True





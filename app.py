from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()


df = pd.read_csv('data/pink_morsel_formatted.csv')

fig = px.line(df, x="date", y="sales", title="Sales Over Time")

app.layout = html.Div(children=[
    html.H1(children='Sales Over Time For Pink Morsel'),

    dcc.Graph(
        id='pink-morsel-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
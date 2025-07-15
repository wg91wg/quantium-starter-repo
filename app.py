import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('data/pink_morsel_formatted.csv')

fig = px.line(df, x="date", y="sales", title="Sales Over Time")
fig.update_layout(
    plot_bgcolor='black',     
    paper_bgcolor='black',     
    font_color='white'         
)

app.layout = html.Div(children=[
    html.H1(children='Sales Over Time For Pink Morsel',
            style={'textAlign': 'center'}),

    dcc.RadioItems(
        id='region-selector',
        options=[
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
            {"label": "All", "value": "all"}
        ],
        value='all',
        inline=True,
        style={'margin-bottom': '20px'}
    ),

    dcc.Graph(
        id='pink-morsel-graph',
        figure=fig
    )
])


@app.callback(
    Output('pink-morsel-graph', 'figure'),
    Input('region-selector', 'value')
)

def update_line_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else: 
        filtered_df = df[df["region"] == selected_region]
        
    fig = px.line(filtered_df, x="date", y="sales", title=f"Sales in {selected_region}")

    if selected_region == 'north':
            fig.update_traces(line_color="red")
    elif selected_region == 'south':
        fig.update_traces(line_color="cyan")
    elif selected_region == 'east':
        fig.update_traces(line_color="magenta")
    elif selected_region == 'west':
        fig.update_traces(line_color="dark blue")
    elif selected_region == 'all':
         fig.update_traces(line_color="blue")

    fig.update_layout(
        plot_bgcolor='black',      
        paper_bgcolor='black',     
        font_color='white'         
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
from dash import html, dcc
import dash_bootstrap_components as dbc


layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph1'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 1}
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph2'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 2}
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph3'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 1}
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph4'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 2}
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph5'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 1}
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph6'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 2}
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph7'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 1}
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(id='graph8'),
                        style={'width': '100%', 'height': '100%'}
                    ),
                    width={"size": 6, "order": 2}
                ),
            ]
        ),
    ],
    id='accordion_all',
    style={'marginLeft': '20rem'}
)

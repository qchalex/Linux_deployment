from dash import html, dcc
import dash_bootstrap_components as dbc


layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    dcc.Graph(id='graph'),
                    style={'width': '150%', 'height': '150%'}
                ),
                width={"size": 6, "order": 1}
            ),
        )
    ],
    id='accordion_all',
    style={'marginLeft': '20rem'}
)

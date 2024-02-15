from dash import html, dcc
import dash_bootstrap_components as dbc


class Paths:
    PATH_LOGO = 'static/linux-ar21.svg'
    PATH_TO_DATA = r"../data/dataset.csv"


class SidebarElement:
    GENDER = html.Div(
        [
            dbc.CardHeader("   Gender", className='bi bi-123', style={'color': 'black', 'padding': '8px'}
                           ),
            dbc.RadioItems(
                id="gender",
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-dark",
                labelCheckedClassName="active",
                style={"margin-top": "10px", "margin-bottom": "10px"},
                options=[
                    {"label": "Male", "value": 1},
                    {"label": "Female", "value": 2},
                ],
            ),
        ],
        className="radio-group",
    )

    SENIOR_CITIZEN = html.Div(
        [
            dbc.CardHeader("   Senior Citizen", className='bi bi-123', style={'color': 'black', 'padding': '8px'}
                           ),
            dbc.RadioItems(
                id="senior_citizen",
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-dark",
                labelCheckedClassName="active",
                style={"margin-top": "10px", "margin-bottom": "10px"},
                options=[
                    {"label": "No", "value": 1},
                    {"label": "Yes", "value": 2},

                ],
            ),
        ],
        className="radio-group",
    )

    PHONE_SERVICE = html.Div(
        [
            dbc.CardHeader("   Phone Service", className='bi bi-123', style={'color': 'black', 'padding': '8px'}
                           ),
            dbc.RadioItems(
                id="phone_service",
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-dark",
                labelCheckedClassName="active",
                style={"margin-top": "10px", "margin-bottom": "10px"},
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 2},
                ],
            ),
        ],
        className="radio-group",
    )

    INTERNET_SERVICE = html.Div(
        [
            dbc.CardHeader("   Internet Service", className='bi bi-123', style={'color': 'black', 'padding': '8px'}),
            dcc.Dropdown(
                id="internet_service",
                options=[
                    {"label": "DSL", "value": 1},
                    {"label": "Fiber optic", "value": 2},
                    {"label": "No", "value": 3},
                ],
                value=None,
                style={"margin-top": "10px", "margin-bottom": "10px"},
                className="btn-outline-dark"
            ),
        ],
        className="radio-group",
    )

    CONTRACT = html.Div(
        [
            dbc.CardHeader("   Contract", className='bi bi-123', style={'color': 'black', 'padding': '8px'}),
            dcc.Dropdown(
                id="contract",
                options=[
                    {"label": "Month-to-Month", "value": 1},
                    {"label": "One year", "value": 2},
                    {"label": "Two year", "value": 3},
                ],
                value=None,
                style={"margin-top": "10px", "margin-bottom": "10px"},
                className="btn-outline-dark"
            ),
        ],
        className="radio-group",
    )

    PAYMENT_METHOD = html.Div(
        [
            dbc.CardHeader("   Payment Method", className='bi bi-123', style={'color': 'black', 'padding': '8px'}),
            dcc.Dropdown(
                id="payment_method",
                options=[
                    {"label": "Bank transfer", "value": 1},
                    {"label": "Mailed Check", "value": 2},
                    {"label": "Credit card", "value": 3},
                    {"label": "Electronic check", "value": 4},

                ],
                value=None,
                style={"margin-top": "10px", "margin-bottom": "10px"},
                className="btn-outline-dark"
            ),
        ],
        className="radio-group",
    )

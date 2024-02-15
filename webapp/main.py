import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from navbar import navbar
from sidebar import sidebar
from webapp.style.sidebar_style import SIDEBAR_STYLE, SIDEBAR_HIDDEN
from layout import layout
from static.params import Paths

data = pd.read_csv(Paths.PATH_TO_DATA)
data['TotalCharges'] = data['TotalCharges'].replace('', pd.NA)

data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data['TotalCharges'] = data['TotalCharges'].astype(float)

app = dash.Dash(external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.BOOTSTRAP])
app.title = 'Linux Application'


# region App layout

app.layout = html.Div(  # layout with the others components.
    [
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='side_click'),
        navbar,
        sidebar,
        layout,
    ],
)

# endregion

# region callback Sidebar


@app.callback(
    # Callback when we click on the sidebar button,
    # It hides the sidebar by changing it with SIDEBAR_HIDDEN or STYLE in sidebar_style.py
    Output("sidebar", "style"),
    Output("side_click", "data"),
    Output("accordion_all", "style"),
    Input("sidebar-button", "n_clicks"),
)
def hide_or_show_sidebar_while_clicking_on_sidebar_button(n_clicks):
    if n_clicks % 2 == 0:
        sidebar_style = SIDEBAR_STYLE
        cur_nclick = "HIDDEN"
        accordion_style = {"marginLeft": "20rem", "transition": "all 0.5s"}
    else:
        sidebar_style = SIDEBAR_HIDDEN
        cur_nclick = "SHOW"
        accordion_style = {"marginLeft": "0", "transition": "all 0.5s"}

    return sidebar_style, cur_nclick, accordion_style


def get_sidebar_value(value, element):
    if element == "gender":
        if value == 1:
            return 'Male'
        elif value == 2:
            return 'Female'
    elif element == "senior_citizen":
        if value == 1:
            return 0
        elif value == 2:
            return 1
    elif element == "phone_service":
        if value == 1:
            return 'Yes'
        elif value == 2:
            return 'No'
    elif element == "internet_service":
        if value == 1:
            return 'DSL'
        elif value == 2:
            return 'Fiber optic'
        elif value == 3:
            return 'No'
    elif element == "payment_method":
        if value == 1:
            return 'Bank transfer (automatic)'
        elif value == 2:
            return 'Mailed check'
        elif value == 3:
            return 'Credit card (automatic)'
        elif value == 4:
            return 'Electronic check'
    elif element == "contract":
        if value == 1:
            return 'Month-to-Month'
        elif value == 2:
            return 'One year'
        elif value == 3:
            return 'Two year'

# endregion


# region main callback


@app.callback(
    Output('graph', 'figure'),
    [Input('gender', 'value'),
     Input('senior_citizen', 'value'),
     Input('phone_service', 'value'),
     Input('internet_service', 'value'),
     Input('contract', 'value'),
     Input('payment_method', 'value')]
)
def update_graph(gender_value, senior_citizen_value, phone_service_value, internet_service_value, contract_value,
                 payment_method_value):
    filtered_df = data.copy()

    if gender_value is not None:
        filtered_df = filtered_df[filtered_df['gender'] == get_sidebar_value(gender_value, "gender")]
    if senior_citizen_value is not None:
        filtered_df = filtered_df[
            filtered_df['SeniorCitizen'] == get_sidebar_value(senior_citizen_value, "senior_citizen")]
    if phone_service_value is not None:
        filtered_df = filtered_df[
            filtered_df['PhoneService'] == get_sidebar_value(phone_service_value, "phone_service")]
    if internet_service_value is not None:
        filtered_df = filtered_df[
            filtered_df['InternetService'] == get_sidebar_value(internet_service_value, "internet_service")]
    if contract_value is not None:
        filtered_df = filtered_df[filtered_df['Contract'] == get_sidebar_value(contract_value, "contract")]
    if payment_method_value is not None:
        filtered_df = filtered_df[
            filtered_df['PaymentMethod'] == get_sidebar_value(payment_method_value, "payment_method")]

    fig = px.scatter(filtered_df, x='MonthlyCharges', y='TotalCharges', color='Churn',
                     title='Total Charges vs Monthly Charges',
                     labels={'MonthlyCharges': 'Monthly Charges', 'TotalCharges': 'Total Charges'})

    return fig

# endregion


if __name__ == '__main__':
    app.run_server(port=8050)

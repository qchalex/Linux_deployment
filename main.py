import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from webapp.navbar import navbar
from webapp.sidebar import sidebar
from webapp.style.sidebar_style import SIDEBAR_STYLE, SIDEBAR_HIDDEN
from webapp.layout import layout
from webapp.static.params import Paths
from webapp.static.get_sidebar_elements_value import GetSidebarElementsValue

import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv(Paths.PATH_TO_DATA)
data['TotalCharges'] = data['TotalCharges'].replace('', pd.NA)

data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data['TotalCharges'] = data['TotalCharges'].astype(float)

app = dash.Dash(external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.BOOTSTRAP])
app.title = 'Customers Web Application'


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


# endregion


# region main callback


@app.callback(
    [Output('graph1', 'figure'),
     Output('graph2', 'figure'),
     Output('graph3', 'figure'),
     Output('graph4', 'figure'),
     Output('graph5', 'figure'),
     Output('graph6', 'figure'),
     Output('graph7', 'figure'),
     Output('graph8', 'figure')],
    [Input('gender', 'value'),
     Input('senior_citizen', 'value'),
     Input('phone_service', 'value'),
     Input('internet_service', 'value'),
     Input('contract', 'value'),
     Input('payment_method', 'value')]
)
def update_graph(gender_value, senior_citizen_value, phone_service_value, internet_service_value, contract_value,
                 payment_method_value):

    data_copy = data.copy()

    if gender_value is not None:
        data_copy = data_copy[data_copy['gender'] == GetSidebarElementsValue.get_sidebar_value(gender_value, "gender")]
    if senior_citizen_value is not None:
        data_copy = data_copy[data_copy['SeniorCitizen'] == GetSidebarElementsValue.get_sidebar_value(senior_citizen_value, "senior_citizen")]
    if phone_service_value is not None:
        data_copy = data_copy[data_copy['PhoneService'] == GetSidebarElementsValue.get_sidebar_value(phone_service_value, "phone_service")]
    if internet_service_value is not None:
        data_copy = data_copy[data_copy['InternetService'] == GetSidebarElementsValue.get_sidebar_value(internet_service_value, "internet_service")]
    if contract_value is not None:
        data_copy = data_copy[data_copy['Contract'] == GetSidebarElementsValue.get_sidebar_value(contract_value, "contract")]
    if payment_method_value is not None:
        data_copy = data_copy[data_copy['PaymentMethod'] == GetSidebarElementsValue.get_sidebar_value(payment_method_value, "payment_method")]

    figure1 = px.scatter(data_copy, x='MonthlyCharges', y='TotalCharges', color='gender',
                     title='Total Charges vs Monthly Charges',
                     labels={'MonthlyCharges': 'Monthly Charges', 'TotalCharges': 'Total Charges'})

    churn_counts = data_copy['Churn'].value_counts()
    colors = ['lightblue', 'lightgreen']
    figure2 = go.Figure(
        data=[go.Pie(labels=churn_counts.index, values=churn_counts.values, hole=.3, marker_colors=colors)])
    figure2.update_traces(textinfo='percent+label', textfont_size=14)
    figure2.update_layout(title='Churn Distribution')

    figure3 = px.histogram(data_copy, x='MultipleLines', color='MultipleLines', title='Multiple Lines Distribution',
                           pattern_shape="MultipleLines", barmode='stack')
    figure3.update_traces(texttemplate='%{value}', textposition='outside')
    figure3.update_layout(legend_title_text='Multiple Lines')

    streaming_tv_avg_charges = data_copy.groupby('StreamingTV')['MonthlyCharges'].mean().reset_index()
    figure4 = px.bar(streaming_tv_avg_charges, x='StreamingTV', y='MonthlyCharges',
                     text='MonthlyCharges', color='StreamingTV',
                     title='Charges Mensuelles Moyennes par Statut de Streaming TV')
    figure4.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    figure4.update_layout(xaxis_title="Statut de Streaming TV",
                          yaxis_title="Charges Mensuelles Moyennes ($)")

    # Streaming Movies Distribution - Box Plot
    figure5 = px.box(data_copy, x='StreamingMovies', y='MonthlyCharges', color='StreamingMovies',
                     title='Distribution des Charges Mensuelles par Catégorie de Streaming de Films')
    figure5.update_layout(xaxis_title="Catégorie de Streaming de Films",
                          yaxis_title="Charges Mensuelles ($)")

    figure6 = px.box(data_copy, x='InternetService', y='MonthlyCharges', color='InternetService',
                     title="Distribution des Charges Mensuelles par Type de Service Internet")

    online_security_counts = data_copy['OnlineSecurity'].value_counts()
    figure7 = px.pie(names=online_security_counts.index, values=online_security_counts.values,
                     title='Online Security Distribution')

    # Distribution de la sauvegarde en ligne
    online_backup_counts = data_copy['OnlineBackup'].value_counts()
    figure8 = px.bar(x=online_backup_counts.index, y=online_backup_counts.values, title='Online Backup Distribution')

    return figure1, figure2, figure3, figure4, figure5, figure6, figure7, figure8

# endregion


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
    print('Application available at http://40.68.93.181:8050/')

from dash import html
import dash_bootstrap_components as dbc

from webapp.style.sidebar_style import SIDEBAR_STYLE
from webapp.static.params import SidebarElement

sidebar = html.Div(
    [
        html.H5("Sidebar Filter", style={"margin-top": "10px", "margin-left": "25px"}),
        dbc.Card(SidebarElement.GENDER),
        dbc.Card(SidebarElement.SENIOR_CITIZEN),
        dbc.Card(SidebarElement.PHONE_SERVICE),
        dbc.Card(SidebarElement.INTERNET_SERVICE),
        dbc.Card(SidebarElement.CONTRACT),
        dbc.Card(SidebarElement.PAYMENT_METHOD),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

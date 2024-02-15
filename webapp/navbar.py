import dash_bootstrap_components as dbc
from dash import html
import base64

LOGO = 'static/linux-ar21.svg'
with open(LOGO, 'r') as f:
    svg_content = f.read()

encoded_svg = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')

navbar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        dbc.Row(
                            dbc.Col(html.Img(src='data:image/svg+xml;base64,{}'.format(encoded_svg), height='85vh')),
                        ),
                        className="d-flex align-items-center justify-content-end",
                        href='/'
                    ),
                    width='auto',
                ),
                dbc.Col(
                    dbc.Nav(
                        dbc.NavItem(
                            dbc.Button(id="sidebar-button", n_clicks=0, className='bi bi-filter-left', color="dark")
                        ),
                        className="d-flex align-items-center justify-content-end",
                        navbar=True,
                    ),
                    width='auto',
                ),
            ],
            align="center",
            style={"margin-right": "auto"},
        ),
    ],
    color="dark",
    dark=True,
    className="p-3 sticky-top", #remain at the top of the screen while scrolling
    style={"height": "8vh","min-height": "8vh"},#change the height of the navbar
)

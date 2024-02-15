SIDEBAR_STYLE = {
    "position": "fixed",
    "top": '8vh',  # Here if we decrease the number of top here, it will increase the size of the sidebar. 5vh if navbar is on
    "left": 0,  # Sidebar is located on the left side of the application
    "bottom": 0,
    "width": "15rem",
    "height": "95%",
    "z-index": 1,
    "overflow-x": "hidden",
    "overflow": "auto",
    "transition": "all 0.5s",  # Time of transition while clicking on the button. It will take here 0.5 secondes to appear the sidebar.
    "padding": "0.5rem 1rem",
    "background-color": "#fafafa"  # Grey color. If you want to change go check the HEX HTML colors
}

SIDEBAR_HIDDEN = {
    "position": "fixed",
    "top": '8vh', #5vh if navbar is on
    "left": "-20rem",  # Grant the fact of the hidden sidebar. Move to the left as the same size as the width of Sidebar Style  of sidebar to hide totally the sidebar
    "bottom": 0,
    "width": "15rem",
    "height": "95%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#fafafa"  # Grey color. If you want to change go check the HEX HTML colors
}
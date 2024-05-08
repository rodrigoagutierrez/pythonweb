import reflex as rx
from pythonweb.pages.index import index
import pythonweb.styles.styles as styles
from pythonweb.styles.styles import Size as Size
from pythonweb.pages.index import index
from pythonweb.pages.courses import courses



class State(rx.State):
    pass
    

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets= [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]
)






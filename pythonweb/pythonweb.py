import reflex as rx
from pythonweb.components.navbar import navbar
from pythonweb.components.footer import footer
from pythonweb.views.header.header import header
from pythonweb.views.links.links import links
from pythonweb.views.sponsors.sponsors import sponsors
import pythonweb.styles.styles as styles
from pythonweb.styles.styles import Size as Size


class State(rx.State):
    pass


def index()-> rx.Component:
    return rx.chakra.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            )
        ),
        footer()
    )
    
    

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets= [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]
)
app.add_page(
    index,
    title="RodriDev | Te ayudo a crear tu sitio web y aplicaciones moviles",
    description="Hola, mi nombre es Rodrigo Gutiérrez. Soy desarrollador freelance",
    image="avatar.jpg"
    )
app.compile()

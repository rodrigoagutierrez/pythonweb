import reflex as rx
from pythonweb.components.navbar import navbar
from pythonweb.components.footer import footer
from pythonweb.views.header import header
from pythonweb.views.links import links
from pythonweb.views.sponsors import sponsors
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

title = "RodriDev | Te ayudo a crear tu sitio web y aplicaciones moviles"
description = "Hola, mi nombre es Rodrigo Gutiérrez. Soy desarrollador web/software"
preview = "https://github.com/rodrigoagutierrez"

app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@rodridev"}
        ]
    )


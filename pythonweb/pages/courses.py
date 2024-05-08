import reflex as rx
from pythonweb.routes import Route
import pythonweb.styles.styles as styles
import pythonweb.utils as utils
from pythonweb.components.navbar import navbar
from pythonweb.components.footer import footer
from pythonweb.views.header import header
from pythonweb.views.links import links
from pythonweb.views.sponsors import sponsors
 
 
@rx.page(
    route=Route.COURSES.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta        
)

def courses()-> rx.Component:
    return rx.chakra.box(
        utils.lang(),
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            )
        ),
        footer()
    )
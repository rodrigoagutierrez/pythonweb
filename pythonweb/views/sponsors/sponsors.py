import reflex as rx
import pythonweb.constants as const
from pythonweb.styles.styles import Size
from pythonweb.components.title import title
from pythonweb.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran"),
        rx.chakra.responsive_grid(
            link_sponsor(
                "elgato.png",
                const.ELGATO_URL,
                "Logotipo de Elgato"
            ),
            link_sponsor(
                "mvp.png",
                const.MVP_URL,
                "Logotipo de Microsoft MVP"
            ),
            spacing=Size.BIG.value,
            columns=[1, 2]
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )
import reflex as rx
import pythonweb.styles.styles as styles
from pythonweb.styles.styles import Size
from pythonweb.styles.colors import Color


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.chakra.vstack(
                    rx.chakra.text(title, style=styles.button_title_style),
                    rx.chakra.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )

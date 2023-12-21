import reflex as rx
from pythonweb.styles.colors import Color, TextColor
import pythonweb.styles.styles as styles


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(title, font_weight="bold", color=Color.PRIMARY.value),
        f" {body}", font_size=styles.Size.MEDIUM.value,
        color=TextColor.BODY.value,
    )
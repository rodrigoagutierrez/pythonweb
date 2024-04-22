import reflex as rx
import datetime
import pythonweb.constants as const
from pythonweb.styles.colors import Color, TextColor
from pythonweb.styles.styles import Size


def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src="logo.png",
            display="grid",
            align_items="center",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de RodriDev. Una \"eme\" entre llaves."
        ),
        rx.chakra.link(
            rx.chakra.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.chakra.span("RodriDev by Rodrigo Gutiérrez", color=Color.PRIMARY.value),
                " v3."
            ),
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.chakra.text(
            "BUILDING SOFTWARE WITH ♥ FROM VALENCIA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )
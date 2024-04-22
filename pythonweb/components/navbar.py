import reflex as rx
from pythonweb.styles.colors import Color
from pythonweb.styles.styles import Size as Size
from pythonweb.styles.styles import styles as styles
from pythonweb.styles.styles import styles


def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.text(
            "RodriDev",
            height=Size.BIG.value,          
            margin=Size.DEFAULT.value,
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size=Size.DEFAULT.value,
            padding_left=Size.BIG.value,
            style=styles.navbar_title_style
            ),
            position="sticky",
            bg="linear-gradient(271.68deg, #171F26, #0C151D 70%)",
            padding_x=Size.DEFAULT.value,
            padding_y=Size.SMALL.value,
            z_index="999",
            top="0",
    )
import reflex as rx
from pythonweb.styles.styles import Size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
     return rx.chakra.link(
        rx.chakra.image(
            src=image,
            width=Size.LARGE.value,
            height=Size.LARGE.value,
            alt=alt,
        ),
        align_items="start",
        href=url,
        is_external=True,
    )
import reflex as rx
import datetime
import pythonweb.constants as const
from pythonweb.styles.styles import Size
from pythonweb.styles.colors import Color, TextColor
from pythonweb.components.link_icon import link_icon
from pythonweb.components.info_text import info_text


def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                name="Rodrigo Gutiérrez",
                size="xl",
                src="avatar.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.chakra.vstack(
                rx.chakra.heading(
                    "Rodrigo Gutiérrez",
                    size="lg",
                    color=TextColor.BODY.value,
                ),
                rx.chakra.text(
                    "@rodridev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.chakra.hstack(
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Size.BIG.value
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.chakra.flex(
            info_text(
                f"{experience()}+",
                "años de experiencia"
            ),
            rx.chakra.spacer(),
            info_text(
                "100+", "aplicaciones creadas"
            ),
            rx.chakra.spacer(),
            info_text(
                "1M+", "seguidores"
            ),
            width="100%"
        ),
        rx.chakra.text(
            f"""
            Soy ingeniero de software y actualmente trabajo como freelance
            full-stack developer iOS y Android.
            Además, creo contenido formativo sobre programación en redes.
            Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2010
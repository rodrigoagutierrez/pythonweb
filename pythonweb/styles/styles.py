import reflex as rx
from enum import Enum
import pythonweb.styles.styles as styles
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight


# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO="0px !important"
    SMALL="0.5em"
    MEDIUM="0,75em"
    DEFAULT="1em"
    LARGE="1,5em"
    BIG="2em"
    VERY_BIG = "4em"

# Stylesheets se colocan en la pagina principal dentro de app
# STYLESHEETS = [
#     "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
#     "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
# ]

# Styles
    
BASE_STYLE = {
    "font_family" : Font.DEFAULT.value,
    "font_weight" : FontWeight.LIGHT.value,
    "background_color" : Color.BACKGROUND.value,

    
    rx.chakra.Button: {
        "width" : "100%",
        "height" : "100%",
        "display" : "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "color" : TextColor.HEADER.value,
        "background_color" : Color.CONTENT.value,
        "white_space" : "normal",
        "text_align" : "start",
        "_hover" : {
            "background_color" : Color.SECONDARY.value,
        }   
    },
    rx.chakra.Link: {
        "text_decoration" : "none",
        "_hover" : {},
    }
    
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=TextColor.HEADER.value
)

title_style = dict (
    font_family=Font.TITLE.value,
    width="100%",
    padding_top=styles.Size.MEDIUM.value,
    color=TextColor.HEADER.value,
)

button_title_style = dict(
    width="100%",
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.HEADER.value,
)
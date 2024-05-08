import reflex as rx


# Común

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://github.com/rodrigoagutierrez"
_meta=[
        {"name": "og:type", "content": "website"},        
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@rodridev"}
        ]

# Index

index_title = "RodriDev | Te ayudo a crear tu sitio web y aplicaciones moviles"
index_description = "Hola, mi nombre es Rodrigo Gutiérrez. Soy desarrollador web/software"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)



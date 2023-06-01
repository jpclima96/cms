# CMS Templates
# https://docs.django-cms.org/en/latest/how_to/install.html#templates

CMS_TEMPLATES = [
    ("app/home.html", "Home"),
    ("campaign/landpage.html", "Landpage"),
]

# Placeholder
# https://docs.django-cms.org/en/latest/reference/configuration.html#std-setting-CMS_PLACEHOLDER_CONF
CMS_PLACEHOLDER_CONF = {
    "content": {
        "plugins": ["BlockPlugin"],
        "name": "Conteúdo",
        # 'language_fallback': True,
        # 'default_plugins': [
        #     {
        #         'plugin_type': 'TextPlugin',
        #         'values': {
        #             'body':'<p>Lorem ipsum dolor sit amet...</p>',
        #         },
        #     },
        # ],
        # 'child_classes': {
        #     'TextPlugin': ['PicturePlugin', 'LinkPlugin'],
        # },
        # 'parent_classes': {
        #     'LinkPlugin': ['TextPlugin'],
        # },
    },
    "navigation": {
        "plugins": ["NavbarPlugin"],
        "language_fallback": True,
        "default_plugins": [
            {
                "plugin_type": "NavbarPlugin",
                "values": {}
            },
        ],
    },
    "footer": {
        "plugins": ["FooterPlugin"],
    },
}

# Picture
# https://github.com/django-cms/djangocms-picture

DJANGOCMS_PICTURE_ALIGN = [
    # Change prefix classes alignment for not use space
    (" object-left", "Esquerda"),
    (" mx-auto", "Centro"),
    (" object-right", "Direita"),
]

from .ckeditor import *

import re

import discord
from discord import embeds


def generate_embed_message(title: str, message: str, color: discord.Color):
    embed = embeds.Embed(
        title=title,
        description=message,
        color=color
    )

    return embed


def clean_url(url: str):
    url = re.sub(r'\\', '', url)
    return url


def clean_html_tags(string: str):
    html_tags = {
        "<br>": "\n",
        "<b>": " ",
        "<\\/b>": " ",
        "<i>": " ",
        "<\\/i>": " "
    }
    for tag in html_tags.keys():
        string = string.replace(tag, html_tags.get(tag))

    return re.sub(r'\n+', '\n\n', string)

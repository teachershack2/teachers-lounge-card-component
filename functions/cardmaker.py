from PIL import Image, ImageFont, ImageDraw
from color_convert import color
import datetime
import os
import re


def text_length(word):
    length = len(word) * 50
    remainder = (1500 - length) / 2
    return 1500 - length - remainder


def hex_to_rgb(hex_code):
    rgb_str = color.hex_to_rgb(hex_code).replace("rgb(", "").replace(")", "")
    return eval(rgb_str)


def make_card1(title, subtitle, hex_code1, hex_code2):
    image = Image.open("images/card1.png")

    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 100)

    subtitle_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 100)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(title), 700), title, hex_to_rgb(hex_code1), font=title_font)

    image_editable.text((text_length(subtitle), 900), subtitle, hex_to_rgb(hex_code2), font=subtitle_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename


def make_card2(title, subtitle, hex_code1, hex_code2):
    image = Image.open("images/card2.png")

    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 100)

    subtitle_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 100)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(title), 800), title, hex_to_rgb(hex_code1), font=title_font)

    image_editable.text((text_length(subtitle), 1200), subtitle, hex_to_rgb(hex_code2), font=subtitle_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename


def make_card3(title, subtitle, hex_code1, hex_code2):
    image = Image.open("images/card3.png")

    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 100)

    subtitle_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 100)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(title), 800), title, hex_to_rgb(hex_code1), font=title_font)

    image_editable.text((text_length(subtitle), 1000), subtitle, hex_to_rgb(hex_code2), font=subtitle_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename


def delete_cards():
    dir = 'static'
    for file in os.listdir(dir):
        f = os.path.join(dir, file)
        if os.path.isfile(f):
            if "default" in f or "error" in f:
                continue
            os.remove(f)


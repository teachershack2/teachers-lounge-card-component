from PIL import Image, ImageFont, ImageDraw
import datetime


def text_length(word):
    length = len(word) * 50
    remainder = (1500 - length) / 2
    return 1500 - length - remainder


def make_card1(title, subtitle):
    image = Image.open("images/card1.png")

    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 100)

    subtitle_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 100)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(title), 700), title, (237, 230, 211), font=title_font)

    image_editable.text((text_length(subtitle), 900), subtitle, (237, 230, 211), font=subtitle_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename


def make_card2(title, subtitle):
    image = Image.open("images/card2.png")

    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 100)

    subtitle_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 100)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(title), 800), title, (54, 69, 79), font=title_font)

    image_editable.text((text_length(subtitle), 1200), subtitle, (54, 69, 79), font=subtitle_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename


def make_card3(title, subtitle):
    image = Image.open("images/card3.png")

    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 100)

    subtitle_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 100)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(title), 800), title, (54, 69, 79), font=title_font)

    image_editable.text((text_length(subtitle), 1000), subtitle, (54, 69, 79), font=subtitle_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename

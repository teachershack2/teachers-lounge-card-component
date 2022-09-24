from PIL import Image, ImageFont, ImageDraw
from color_convert import color
import datetime
import os


def text_length(word):
    print(len(word))
    length = len(word) * 50
    remainder = (1500 - length) / 2
    x_axis = 1500 - length - remainder
    print(f"length: {length}")
    print(f"remainder: {remainder}")
    print(f"x-axis: {x_axis}")
    return x_axis


def hex_to_rgb(hex_code):
    rgb_str = color.hex_to_rgb(hex_code).replace("rgb(", "").replace(")", "")
    return eval(rgb_str)


def get_colors(req):
    colors = []

    for i in range(0, 4):
        if req.form.get("c" + str(i)):
            colors.append(hex_to_rgb(req.form['c' + str(i)]))

    return colors


def is_bold(req):
    bold = []

    for i in range(0, 4):
        if req.form.get("bold" + str(i)):
            bold.append('fonts/Montserrat-Bold.ttf')
        else:
            bold.append('fonts/Montserrat-Regular.ttf')

    return bold


def get_texts(req):
    text = []

    for i in range(0, 4):
        if req.form.get("t" + str(i)):
            text.append(req.form['t' + str(i)])
        else:
            text.append(req.form['t' + str(i)])

    return text


def make_card1(text, colour, bold):
    image = Image.open("images/card1.png")

    title_font = ImageFont.truetype(bold[0], 100)

    subtitle_font = ImageFont.truetype(bold[1], 100)

    to_font = ImageFont.truetype(bold[2], 80)

    from_font = ImageFont.truetype(bold[3], 80)

    image_editable = ImageDraw.Draw(image)
    image_editable.text((text_length(text[0]), 700), text[0], colour[0], font=title_font)
    image_editable.text((text_length(text[0]), 900), text[1], colour[1], font=subtitle_font)
    image_editable.text((270, 1290), text[2], colour[2], font=to_font)
    image_editable.text((270, 1410), text[3], colour[3], font=from_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename


def make_card2(text, colour, bold):
    image = Image.open("images/card2.png")

    title_font = ImageFont.truetype(bold[0], 100)

    subtitle_font = ImageFont.truetype(bold[1], 100)

    to_font = ImageFont.truetype(bold[2], 80)

    from_font = ImageFont.truetype(bold[3], 80)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(text[0]), 780), text[0], colour[0], font=title_font)
    image_editable.text((text_length(text[1]), 1100), text[1], colour[1], font=subtitle_font)
    image_editable.text((270, 1290), text[2], colour[2], font=to_font)
    image_editable.text((270, 1410), text[3], colour[3], font=from_font)

    date = str(datetime.datetime.now())

    filename = f"{date}.png"

    image.save(f"static/{filename}")

    return filename


def make_card3(text, colour, bold):
    image = Image.open("images/card3.png")

    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 100)

    subtitle_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 100)

    to_font = ImageFont.truetype(bold[2], 80)

    from_font = ImageFont.truetype(bold[3], 80)

    image_editable = ImageDraw.Draw(image)

    image_editable.text((text_length(text[0]), 800), text[0], colour[0], font=title_font)
    image_editable.text((text_length(text[1]), 1000), text[1], colour[1], font=subtitle_font)
    image_editable.text((270, 1290), text[2], colour[2], font=to_font)
    image_editable.text((270, 1410), text[3], colour[3], font=from_font)

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

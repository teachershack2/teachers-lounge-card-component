from flask import Flask, render_template, request, url_for
from functions import cardmaker
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():

    cardmaker.delete_cards()

    image_file = url_for('static', filename="default.png")

    return render_template('index.html', image_file=image_file)


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':

        text = cardmaker.get_texts(request)

        number = request.form['card_no']

        colour = cardmaker.get_colors(request)

        bold = cardmaker.is_bold(request)

        print(text, number, bold, colour)

        file = "static/errorimg.png"

        if len(text) > 0:
            if number == '1':
                file = cardmaker.make_card1(text, colour, bold)
            elif number == '2':
                file = cardmaker.make_card2(text, colour, bold)
            elif number == '3':
                file = cardmaker.make_card3(text, colour, bold)

            image_file = url_for('static', filename=file)

            return render_template('index.html', image_file=image_file)

        else:
            print('fasdfsafsadf')
            error_image_file = url_for('static', filename=file)
            return render_template('index.html', image_file=error_image_file)


if __name__ == ' __main__':
    app.debug = True
    app.run()

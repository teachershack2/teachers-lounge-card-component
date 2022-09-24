from flask import Flask, render_template, request, url_for
from functions import cardmaker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    image_file = url_for('static', filename="default.png")

    return render_template('index.html', image_file=image_file)


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':

        title = request.form['title']
        subtitle = request.form['subtitle']
        number = request.form['card_no']

        print(title, subtitle, number)

        file = "static/errorimg.png"

        if title or subtitle:
            if number == '1':
                file = cardmaker.make_card1(title, subtitle)
            elif number == '2':
                file = cardmaker.make_card2(title, subtitle)
            elif number == '3':
                file = cardmaker.make_card3(title, subtitle)

            image_file = url_for('static', filename=file)

            return render_template('index.html', image_file=image_file)

        else:
            print('fasdfsafsadf')
            error_image_file = url_for('static', filename=file)
            return render_template('index.html', image_file=error_image_file)


if __name__ == ' __main__':
    app.debug = True
    app.run()

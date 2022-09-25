import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


def is_send(req):
    if req.form.get("isEmail"):
        if req.form.get("e1"):
            return True
    return False


def send(req, image, name):
    email = req.form['e1']
    print(email)
    if is_send(req):
        message = Mail(
            from_email='teacherslougne@gmail.com',
            to_emails=email,
            subject=f"[teachers lounge] {name} sent you a card!",
            html_content='<strong>Create your own custom appreciation cards at </strong>'
                         '<br>'
                         '<a href="https://appreciationcards.pythonanywhere.com">teachers lounge appreciation '
                         'cards</a>.')
        with open(f"static/{image}", 'rb') as f:
            data = f.read()
            f.close()
        encoded_file = base64.b64encode(data).decode()

        attached_file = Attachment(
            FileContent(encoded_file),
            FileName('image.png'),
            FileType('image/png'),
            Disposition('attachment')
        )
        message.attachment = attached_file
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)


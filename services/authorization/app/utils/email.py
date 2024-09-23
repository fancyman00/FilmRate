from email.message import EmailMessage


def email_constructor(link: str):
    msg = EmailMessage()
    msg['Subject'] = "Подтверждение адреса электронной почты"
    msg.set_content("""\
    <html>
      <head></head>
      <body>
        <h2>Подтверждение адреса электронноЙ почты</h2>
        <div><h4>Перейдите по ссылке ниже для подтвеждения адреса электронной почты</div>
        <div>{item}</div>
      </body>
    </html>
    """.format(item=link), subtype='html')
    return msg

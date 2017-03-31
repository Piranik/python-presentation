import smtplib
import json
from email.mime.text import MIMEText


def get_body(phones):
    phone_format = '!!! {} LA PRETUL DE NUMAI {} LEI !!!'

    body = '\n'.join([phone_format.format(phone['name'], phone['price'])
                      for phone in phones])

    # return json.dumps(phones, sort_keys=True, indent=4, separators=(',', ': '))

    return body


def send_phones_email(phones, to):
    body = get_body(phones)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("cdl.demo.python@gmail.com", "demopython")

    msg = MIMEText(body)
     
    msg['Subject'] = 'Oferta SENZATIONALA!!!1'
    msg['From'] = 'CDL Demo Python <cdl.demo.python@gmail.com>'
    msg['To'] = to

    server.sendmail('cdl.demo.python@gmail.com',
                    [to, 'razvan.ch95@gmail.com'],
                    msg.as_string())
    server.quit()


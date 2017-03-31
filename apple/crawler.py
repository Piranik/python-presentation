from bs4 import BeautifulSoup
import requests
import json
import smtplib
import re
from email.mime.text import MIMEText


def send_email(body, to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("cdl.demo.python@gmail.com", "demopython")

    msg = MIMEText(body)
     
    msg['Subject'] = 'Oferta SENZATIONALA!!!1'
    msg['From'] = 'CDL Demo Python <cdl.demo.python@gmail.com>'
    msg['To'] = to

    server.sendmail('cdl.demo.python@gmail.com',
                    to,
                    msg.as_string())
    server.quit()


def get_body(phones):
    phone_format = '!!! {} LA PRETUL DE NUMAI {} LEI !!!'

    body = '\n'.join([phone_format.format(phone['name'], phone['price'])
                      for phone in phones])

    return json.dumps(phones, sort_keys=True, indent=4, separators=(',', ': '))

    # return body


if __name__ == '__main__':
    price_matcher = re.compile(r'^([0-9]*\.[0-9]*) Lei')

    req = requests.get('http://www.emag.ro/telefoane-mobile/brand/apple/c?path=telefoane-mobile%2Fbrand%2Fapple%2Fp1%2Fc&pc=40')

    bs = BeautifulSoup(req.text, 'html.parser')

    phones = []

    for form in bs.find_all('form', {'class': 'inner-form'}):
        phone = {}

        name = form.find('div', {'class': 'middle-container'}).find('a').text.strip()
        full_price = form.find('span', {'class': 'price-over'}).text.strip()

        price = price_matcher.match(full_price).group(1)

        phone['name'] = name
        phone['price'] = price

        phones.append(phone)

    send_email(get_body(phones), 'monicamariabaluna@gmail.com')

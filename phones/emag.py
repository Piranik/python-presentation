from bs4 import BeautifulSoup
import requests
import re
from my_email import send_phones_email


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

    send_phones_email(phones, 'your email')

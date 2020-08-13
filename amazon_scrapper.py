import requests
from selectorlib import Extractor, Formatter
import re
from openpyxl import Workbook


class PriceFraction(Formatter):
    def format(self, text):
        price_fraction = ''.join(re.findall(r'\d+', text))
        if price_fraction:
            price_fraction = float(price_fraction) / 100
            return price_fraction
        return None


class PriceWhole(Formatter):
    def format(self, text):
        price_whole = ''.join(re.findall(r'\d+', text))
        if price_whole:
            price_whole = float(price_whole)
            return price_whole
        return None


def get_data(search):

    headers = ({
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept-Language':
            'en-US, en;q=0.5'})

    base_url = "https://www.amazon.com.br/s/ref=nb_sb_noss_2"

    params = {
        '__mk_pt_BR': '%C3%85M%C3%85%C5%BD%C3%95%C3%91',
        'url': 'search-alias%3Daps',
        'field-keywords': search.replace(' ', '+')}

    data = requests.get(base_url + search, params=params, headers=headers)
    return data


def format_response(response):
    formatters = Formatter.get_all()
    extractor = Extractor.from_yaml_file('./scrapper.yaml', formatters=formatters)
    data = extractor.extract(response.text)
    return data


def to_xlsx(data):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "products_data"

    for index, item in enumerate(data['product']):

        price_whole = item['price_whole'] if item['price_whole'] else 0
        price_fraction = item['price_fraction'] if item['price_fraction'] else 0

        total_price = price_whole + price_fraction

        sheet.append([item['product_name'], total_price])

    workbook.save(filename="products_data.xlsx")


if __name__ == "__main__":
    query = "Iphone"
    res = get_data(query)
    formatted_res = format_response(res)
    to_xlsx(formatted_res)


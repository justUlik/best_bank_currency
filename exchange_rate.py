#Uliana Eskova
"""
BeautifulSoup is used for parsing
Requests is used for getting pages data
"""

from bs4 import BeautifulSoup
import requests

def get_best_exchange_rate(currency_code, num_branches):
    """
    Function for finding the best price or currency
    """
    main_url = "https://www.banki.ru/products/currency/cash/"
    response = requests.get(main_url + currency_code.lower() + "/sankt-peterburg/")
    content = response.content.decode("utf-8", errors='ignore')
    soup = BeautifulSoup(content, 'lxml')
    class_of_blocks = "table-flex__row item calculator-hover-icon__container"
    blocks = soup.findAll("div", {"class" : class_of_blocks})
    if len(blocks) < num_branches:
        raise IndexError("Num of brunces is too big")
    res = []
    for bank in blocks:
        name = bank.find("a", {"class" : "font-size-default color-gray-gray"})
        address = bank.find("a", {"data-test" : "bank-name"})
        price = bank.find("div", {"data-currencies-code" : currency_code})
        price = price.attrs["data-currencies-rate-buy"]
        res.append((name.get_text(), address.get_text(), float(price)))
    sorted_res = sorted(res, key=lambda tup: tup[2])
    return sorted_res[:num_branches]

excinfo = get_best_exchange_rate("USD", 3)
print(excinfo)

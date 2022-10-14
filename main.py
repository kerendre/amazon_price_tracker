import requests
from bs4 import BeautifulSoup
from mail_brain import send_mail
import datetime


def check_if_amazon_current_price_lower_than_target_price():
    URL = 'https://www.amazon.com/Receive-SmartWatch-Android-Compatible-Fitness/dp/B09W52WZKT/ref=sr_1_6?crid=1QJJ4T7V2Q8NF&keywords=smart%2Bwatch&qid=1662980582&sprefix=smart%2Caps%2C223&sr=8-6&th=1 '

    #  we are interested in buying the item if the price of the item is lower then this target price.
    target_price = 50

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-GB,en;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
               }

    def ask_requests_from_url():
        # try to get response from the amazon site, if you receive the AttributeError error, try rerun this function
        r = requests.get(URL, headers=headers)
        print(r)
        return r

    response = ask_requests_from_url()

    # soup making (with features="lxml" not 'lxml parser' or 'html parser'
    soup = BeautifulSoup(response.content, features="lxml")
    print(soup.prettify())

    # finding the price of the item
    price_with_dollar_symbol = soup.find(name="span", class_="a-offscreen")

    # splitting the string to get the number only without a dollar sign
    price_split = price_with_dollar_symbol.text.split('$')

    # converting split string to float
    price_only = float(price_split[1])

    # finding the price of the item
    item_name = soup.find(name="span", class_="a-size-large product-title-word-break").text
    print(f" this is item_name {item_name}")

    # mail data
    to_address = 'drevinkeren@gmail.com'
    mail_head = f'Its shopping time ,item you are tracking is  now on sale.'
    mail_body = f" The item: you wanted to buy but it was too expensive is now under the " \
                f"buying price you decided on." \
                f" for the product {URL} use link"

    # If the price of the item is lower then the target price send an email letting me know
    if price_only < target_price:
        send_mail(to_address, mail_head, mail_body)
stop_time = datetime.datetime(2023, 12, 13, 18, 33, 0)
while True:
    dtn = datetime.datetime.now()

    if dtn <= stop_time:
        time = datetime.timedelta(1)  # 1 day
        check_if_amazon_current_price_lower_than_target_price()

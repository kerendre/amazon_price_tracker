import requests
from bs4 import BeautifulSoup
from mail_brain import send_mail
import personal_setting


def check_if_amazon_current_price_lower_than_target_price():

    url= personal_setting.URL

    #  we are interested in buying the item if the price of the item is lower then this target price.
    target_price = personal_setting.target_price

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-GB,en;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
               }


     # connect to amazon site,
    response= requests.get(url, headers=headers)


    # soup making (with features="lxml" not 'lxml parser' or 'html parser'
    soup = BeautifulSoup(response.content, features="lxml")
    #print(soup.prettify())

    # finding the price of the item
    price_with_dollar_symbol = soup.find(name="span", class_="a-offscreen")

    # splitting the string to get the number only without a dollar sign
    price_split = price_with_dollar_symbol.text.split('$')

    # converting split string to float
    price_only = float(price_split[1])

    # finding the name of the item
    item_name = soup.find(name="span", class_="a-size-large product-title-word-break").text.encode("utf-8")


    # mail data
    to_address = personal_setting.send_to_address
    mail_head = f'Its shopping time ,item you are tracking is  now on sale.'
    mail_body = f' The item:{item_name} you wanted to buy but it was too expensive is now under the ' \
                f"buying price you decided on." \
                f" for the product {url} use link"

    # If the price of the item is lower then the target price send an email letting me know
    if price_only < target_price:
        send_mail(to_address, mail_head, mail_body)


def run_amazon_tracer():
    """ recursive function, the function is calling itself if the
    check_if_amazon_current_price_lower_than_target_price is unable to the url due to amazon anti-bot protection """
    try:
        check_if_amazon_current_price_lower_than_target_price()
    except AttributeError:
        run_amazon_tracer()
    else:
        print("The connection to Amazon was successful")

run_amazon_tracer()

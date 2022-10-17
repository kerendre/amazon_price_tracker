import os

""" in order to use this script to trace other item, change the url, target_price.
    if its the first time u use this program change all the variables"""
URL= 'https://www.amazon.com/Receive-SmartWatch-Android-Compatible-Fitness/dp/B09W52WZKT/ref=sr_1_6?crid=1QJJ4T7V2Q8NF&keywords=smart%2Bwatch&qid=1662980582&sprefix=smart%2Caps%2C223&sr=8-6&th=1 '
target_price = 50

# The receiving address, can be of anY mail provider
send_to_address= "drevinkeren@gmail.com"

# sending mail with smtp, in order to use gmail via (mail_brain), you may need to create and use app passwords and
# use 2-Step-Verification. follow the instruction: https://support.google.com/mail/answer/185833?hl=en-GB
my_gmail = os.environ.get("MY_GMAIL_APP_ACCOUNT")
my_gmail_app_password = os.environ.get("MY_GMAIL_APP_PASSWORD")
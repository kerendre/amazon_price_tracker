import smtplib
import os


def send_mail(to_address ,mail_head, mail_body):
    ''' sending mail with smtp, in order to use gmail, you may need to create and use app passwords and use  2-Step-Verification
     follow the instraction: https://support.google.com/mail/answer/185833?hl=en-GB'''
    my_gmail = os.environ.get("MY_GMAIL_APP_ACCOUNT")
    my_gmail_app_password = os.environ.get("MY_GMAIL_APP_PASSWORD")

    # Sending Email with Python
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_gmail_app_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=to_address ,
            msg=f"Subject:{mail_head}\n\n{mail_body}."
        )
import smtplib
import personal_setting

def send_mail(to_address ,mail_head, mail_body):

    my_gmail=personal_setting.my_gmail
    my_gmail_app_password=personal_setting.my_gmail_app_password
    # Sending Email with SMTP
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_gmail_app_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=to_address ,
            msg=f"Subject:{mail_head}\n\n{mail_body}."
        )

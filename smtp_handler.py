import smtplib
import os


sender_email = os.environ["SENDER_EMAIL"]
sender_pass = os.environ["SENDER_PASS"]
target_email = os.environ["TARGET_EMAIL"]


class SendEmail:
    def __init__(self) -> None:
        pass

    def send_mail(self, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_pass)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=target_email,
                                msg=email_body
                                )

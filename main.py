import smtplib
import os
from dadjoke import DadJoke
from motivational import DailyQuote
from currency_convert import CurrencyConvert

# Secrets
sender_email = os.environ["SENDER_EMAIL"]
sender_pass = os.environ["SENDER_PASS"]
target_email = os.environ["TARGET_EMAIL"]

dadjoke = DadJoke()
daily_quote = DailyQuote()
currency_rates = CurrencyConvert()

subject = "Morning Email\n\n"
welcome = "Good morning!\n"
joke = f"\nJoke of the day: {dadjoke.joke}\n"
quote = f"\nQuote: {daily_quote.quote} - {daily_quote.quote_author}\n"
currency = (f"\n100 GBP will get you: "
      f"\n- {currency_rates.gbp_to_huf} HUF"
      f"\n- {currency_rates.gbp_to_jpy} JPY"
      f"\n- {currency_rates.gbp_to_usd} USD")

email_msg = f"Subject:" + subject + welcome + joke + quote + currency

# print(email_msg)  # Debug info

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_pass)
    connection.sendmail(from_addr=sender_email,
                        to_addrs=target_email,
                        msg=email_msg
                        )

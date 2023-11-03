from dadjoke import DadJoke
from motivational import DailyQuote
from currency_convert import CurrencyConvert
from smtp_handler import SendEmail

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
print(email_msg)  # Debug info

send_email = SendEmail()
send_email.send_mail(email_body=email_msg)

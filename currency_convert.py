import requests
import os

EXCHANGE_BEARER = os.environ["EXCHANGE_BEARER"]
EXCHANGE_HEADERS = {"Authorization": f"Bearer {EXCHANGE_BEARER}"}


def pretty_currency(input):
    hundred_units = '{0:.2f}'.format(100 * input)
    formatted_result = '{:,}'.format(float(hundred_units))
    return formatted_result


class CurrencyConvert:
    def __init__(self):
        self.gbp_to_huf = ""
        self.gbp_to_jpy = ""
        self.gbp_to_usd = ""
        self.convert_url = "https://v6.exchangerate-api.com/v6/latest/GBP"
        self.convert_currency()

    def convert_currency(self):
        response = requests.get(url=self.convert_url, headers=EXCHANGE_HEADERS)
        response.raise_for_status()
        # print(response.json())  # Debug info
        response_json = response.json()

        self.gbp_to_huf = pretty_currency(float(response_json["conversion_rates"]["HUF"]))
        self.gbp_to_jpy = pretty_currency(float(response_json["conversion_rates"]["JPY"]))
        self.gbp_to_usd = pretty_currency(float(response_json["conversion_rates"]["USD"]))

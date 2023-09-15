import requests


class CurrencyConvert:
    def __init__(self):
        self.gbp_to_huf = ""
        self.gbp_to_jpy = ""
        self.gbp_to_usd = ""
        self.convert_url = "https://api.exchangerate.host/latest"
        self.convert_currency()

    def convert_currency(self):
        parameters = {
                            "base": "GBP",
                            "symbols": "HUF,JPY,USD",
                            "amount": 100,
                            "places": 2
                        }
        response = requests.get(url=self.convert_url, params=parameters)
        response.raise_for_status()
        response_json = response.json()
        self.gbp_to_huf = "{:,}".format(response_json["rates"]["HUF"])
        self.gbp_to_jpy = "{:,}".format(response_json["rates"]["JPY"])
        self.gbp_to_usd = "{:,}".format(response_json["rates"]["USD"])

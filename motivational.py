import requests


class DailyQuote:
    def __init__(self):
        self.quote = ""
        self.quote_author = ""
        self.zenquote_url = "https://zenquotes.io/api/random"
        self.request_quote()

    def request_quote(self):
        response = requests.get(url=self.zenquote_url)
        response.raise_for_status()
        response_json = response.json()
        self.quote = response_json[0]["q"]
        self.quote_author = response_json[0]["a"]

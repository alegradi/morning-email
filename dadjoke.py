import requests


class DadJoke:
    def __init__(self):
        self.joke = ""
        self.icanhazdadjoke_url = "https://icanhazdadjoke.com/"
        self.headers = {'User-Agent': 'python-requests, used by: TBA', 'Accept': 'application/json'}
        self.request_joke()

    def request_joke(self):
        response = requests.get(url=self.icanhazdadjoke_url, headers=self.headers)
        response.raise_for_status()
        response_json = response.json()
        self.joke = response_json["joke"]

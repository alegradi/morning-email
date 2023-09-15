# Morning - Mail

A simple Python app to email a target with every morning with some useful info.

Currently uses:
- Zenquotes - https://zenquotes.io
- Dad Jokes - https://icanhazdadjoke.com
- Currency Exchange rates - https://api.exchangerate.host

## How to use

1. Clone the repo
```commandline
git clone https://github.com/alegradi/morning-email.git
```

2. Set up a cronjob

The below example is to have this run at 07:00 every weekday.
```commandline
0 7 * * 1-5 export SENDER_EMAIL=""; export SENDER_PASS=""; export TARGET_EMAIL=""; python3 /home/user/morning-email/main.py
```

Specify the variables, they are self-explanatory:
```commandline
SENDER_EMAIL = "Where you are sending from"
SENDER_PASS = "API key to access sending email account"
TARGET_EMAIL= "Where you want to send to"
```

3. Enjoy

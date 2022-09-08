# Bidoo Free Bets

### Project Tree
```
├── project
│   ├── main.py
│   ├── notification.py
│   ├── pybot.py
│   └── Secrets
│       ├── gmail_api_credentials.json
│       └── SECRETS.py
└── requirements.txt
```

## What is Bidoo?

Bidoo is a digital auction site that allows you to bid and relaunch in order to win various types of objects, including hi-tech products, from the iPhone to the airpods, from the notebook to the iRobot, and thanks to which you can get up to 99% savings. For purchases of this type, Bidoo is the number one platform in Italy.

## Free Bets

Bidoo donates about 10-12 bets every day, through different channels (Email, Web Push Notification and SMS), so I felt the need to automate the collection of these bets with a python and crontab script.

## How the script works?

1 - Reads and takes bets from different channels (Web Push Notification, Email ...) and enters them in a dictionary.

2 - Send links for bets on a telegram channel (for a public utility service) [Link Channel](https://t.me/bidoo_puntate_gratis "Bidoo - Puntate Gratis").

3 - Claim all bets in the dictionary on the Bidoo site via Selenium.

4 - Cleans the log file and mailbox

## Using Crontab

To fully automate this process, on Linux you can use Cronetab, a tool you can use to schedule script execution at certain times.

<br>

## TODO

- [ ] Add support for Email and SMS



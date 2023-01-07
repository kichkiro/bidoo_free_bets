# Bidoo Free Bets

### Project Tree
```
├── config
│   ├── config.cfg
│   └── ms_graph_api_token.json
├── logs
│   ├── errors.log
│   └── history.log
├── project
│   ├── main.py
│   ├── notification.py
│   └── pybot.py
├── .gitignore
├── README.md
└── requirements.txt

```

🐍 Python -V = 3.10
-------

## What is Bidoo?

Bidoo is a digital auction site that allows you to bid and relaunch in order to win various types of objects and thanks to which you can get up to 99% savings. For purchases of this type, Bidoo is the number one platform in Italy.

## Free Bets

Bidoo donates about 10-12 bets every day, through different channels (Email, Web Push Notification and SMS), so I felt the need to automate the collection of these bets with a python and crontab script.

## How the script works?

1 - Reads and takes bets from different channels (Web Push Notification, Email ...) and enters them in a dictionary.

2 - Send links for bets on a telegram channel (for a public utility service).

3 - Claim all bets in the dictionary on the Bidoo site via Selenium.

4 - Cleans the log file and mailbox

## Using Crontab

To fully automate this process, on Linux you can use Crontab, this tool is used to schedule the execution of scripts at certain times.

<br>

## TODO

- [ ] Add support for Email and SMS

<br>
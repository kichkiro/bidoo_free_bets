from notification import WebPushNotification
from pybot import PyBot
from selenium import webdriver
from Secrets import SECRETS

def main():

    # Telegram_bot
    pybot = PyBot(SECRETS.BOT_TOKEN, SECRETS.CHANNEL)

    # Notification
    logfile_path = f"/home/{SECRETS.USER}/.config/google-chrome/Default/"\
        "Platform Notifications/000003.log"

    web_push_not = WebPushNotification(logfile_path)

    # Add free_bets to dict
    free_bets = {}
    free_bets = free_bets | web_push_not.read()

    # For each item in dict send a msg to telegram_channel
    for key, value in free_bets.items():
        pybot.send_msg(key, value)

    # Take a free bets with selenium
    pass

    # Clear logfile and email
    pass

    #print(free_bets)

if __name__ == '__main__':
    main()
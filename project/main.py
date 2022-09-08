from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from notification import WebPushNotification
from pybot import PyBot
from Secrets import SECRETS
import time

LOGFILE_PATH = f"/home/{SECRETS.USER}/.config/google-chrome/Default/"\
    "Platform Notifications/000003.log"

def main():

    web_push_not = WebPushNotification(LOGFILE_PATH)
    pybot = PyBot(SECRETS.BOT_TOKEN, SECRETS.CHANNEL)

    # Add free_bets to dict ------------------------------------------->

    free_bets = {}
    free_bets = free_bets | web_push_not.read()

    # For each item in dict send a msg to telegram_channel ------------>

    for key, value in free_bets.items():
        pybot.send_msg(key, value)

    # Take free bets with selenium ------------------------------------>

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    is_first = 1
    
    for key, value in free_bets.items():
        driver.get(key)
        if is_first:
            driver.find_element(
                "id", "field_email").send_keys(SECRETS.BIDOO_USERNAME)
            driver.find_element(
                "id", "password").send_keys(SECRETS.BIDOO_PASSWORD)
            js='javascript:document.getElementsByClassName("btlogin btn\
                btn-grey btn-block btn-lg signup-btn")[1].click();\
                window.open("/checkout")'
            driver.execute_script(js)
            is_first = 0
            time.sleep(5)
        time.sleep(5)
        driver.refresh()
 
    # Clear logfile and email ----------------------------------------->

    web_push_not.clear()

if __name__ == '__main__':
    main()
    
# Stdlib
import time
from datetime import datetime
# Extlib (requiremnts.txt)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
# My Modules
from notification import WebPushNotification, Email
from pybot import PyBot
from Secrets import SECRETS

def main():

    # Add free_bets to a dict ----------------------------------------->
    try:
        web_push_not = WebPushNotification(SECRETS.NOTIFICATION_LOGFILE_PATH)
        free_bets = {}
        free_bets = free_bets | web_push_not.read()

    except BaseException as error:
        with open(SECRETS.ERROR_LOGFILE_PATH, "a") as file:
            file.write(f"{datetime.now()} - {str(error)}\n")

    # For each item in dict send a msg to telegram_channel ------------>
    try:
        pybot = PyBot(SECRETS.BOT_TOKEN, SECRETS.CHANNEL)

        for key, value in free_bets.items():
            pybot.send_msg(key, value)

    except BaseException as error:
        with open(SECRETS.ERROR_LOGFILE_PATH, "a") as file:
            file.write(f"{datetime.now()} - {str(error)}\n")

    # Take free bets with Selenium ------------------------------------>

    try:
        with Display(visible=False, size=(1200, 1500)):
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()))
            is_first = 1

            for key, value in free_bets.items():
                driver.get(key)
                if is_first:
                    driver.find_element(
                        "id", "field_email").send_keys(SECRETS.BIDOO_USERNAME)
                    driver.find_element(
                        "id", "password").send_keys(SECRETS.BIDOO_PASSWORD)
                    js = 'javascript:document.getElementsByClassName("btlogin \
                        btn btn-grey btn-block btn-lg signup-btn")[1].click();\
                        window.open("/checkout")'
                    driver.execute_script(js)
                    is_first = 0
                    time.sleep(5)
                time.sleep(5)
                driver.refresh()

            driver.close()

    except BaseException as error:
        with open(SECRETS.ERROR_LOGFILE_PATH, "a") as file:
            file.write(f"{datetime.now()} - {str(error)}\n")

    # Clear logfile and email ----------------------------------------->

    web_push_not.clear()

if __name__ == '__main__':
    main()

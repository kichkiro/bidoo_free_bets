import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
from notification import WebPushNotification
from pybot import PyBot
from Secrets import SECRETS

def main():

    # Add free_bets to a dict ----------------------------------------->

    web_push_not = WebPushNotification(SECRETS.NOTIFICATION_LOGFILE_PATH)
    free_bets = {}
    free_bets = free_bets | web_push_not.read()

    # For each item in dict send a msg to telegram_channel ------------>

    pybot = PyBot(SECRETS.BOT_TOKEN, SECRETS.CHANNEL)

    for key, value in free_bets.items():
        try:
            pybot.send_msg(key, value)
        except BaseException as error:
            with open(SECRETS.ERROR_LOGFILE_PATH, "a") as file:
                file.write(str(error))

    # Take free bets with Selenium ------------------------------------>

    with Display(visible=False, size=(1200, 1500)):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        is_first = 1

        for key, value in free_bets.items():
            try:
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
            except BaseException as error:
                with open(SECRETS.ERROR_LOGFILE_PATH, "a") as file:
                    file.write(str(error))

        driver.close()

    # Clear logfile and email ----------------------------------------->

    web_push_not.clear()

if __name__ == '__main__':
    main()
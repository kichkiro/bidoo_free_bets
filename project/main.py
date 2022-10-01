# Stdlib
import time
import logging
from configparser import ConfigParser

# Extlib (requirements.txt)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display

# My Modules
from notification import WebPushNotification, Email
from pybot import PyBot


def main():

    # Config settings ------------------------------------------------->
    config = ConfigParser()
    config.read('../config/config.cfg')
    path_config = config['path']
    telegram_settings = config['telegram']
    bidoo_settings = config['bidoo']
    azure_settings = config['azure']

    # Logging settings ------------------------------------------------>
    logging.basicConfig(
        filename=path_config['ERRORS_LOG_PATH'],
        level=logging.ERROR, 
        format='\n[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - '\
            '%(message)s',
        datefmt='%H:%M:%S'
    )

    # Add free_bets to a dict ----------------------------------------->
    try:
        web_push_not = WebPushNotification(path_config)
        free_bets = {}
        free_bets = free_bets | web_push_not.read()

    except BaseException:
        logging.error("Exception occurred", exc_info=True)

    # For each item in dict send a msg to telegram_channel ------------>
    try:
        pybot = PyBot(telegram_settings)

        for key, value in free_bets.items():
            pybot.send_msg(key, value)

    except BaseException:
        logging.error("Exception occurred", exc_info=True)
    
    # Take free bets with Selenium ------------------------------------>
    try:
        with Display(visible=False, size=(1200, 1500)):
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()))
            is_first = 1

            for key, value in free_bets.items():
                driver.get(key)
                if is_first:
                    driver.find_element("id", "field_email").send_keys(
                        bidoo_settings["USERNAME"])
                    driver.find_element("id", "password").send_keys(
                        bidoo_settings["PASSWORD"])
                    js = 'javascript:document.getElementsByClassName("btlogin \
                        btn btn-grey btn-block btn-lg signup-btn")[1].click();\
                        window.open("/checkout")'
                    driver.execute_script(js)
                    is_first = 0
                    time.sleep(5)
                time.sleep(5)
                driver.refresh()

            driver.close()

    except BaseException:
        logging.error("Exception occurred", exc_info=True)
    
    # Clear logfile and email ----------------------------------------->
    web_push_not.clear()


if __name__ == "__main__":
    main()

# StdLib
from configparser import SectionProxy

# Extlib (requirements.txt)
import telegram

class PyBot:
    """

    """
    settings: SectionProxy

    def __init__(self, config: SectionProxy) -> None:
        self.settings = config
        self.token = self.settings["BOT_TOKEN"]
        self.channel = self.settings["CHANNEL"]
        self.bot = telegram.Bot(token=self.token)

    def send_msg(self, link: str, body: str):
        """
        
        """
        msg = f'<b>{body}</b> {link}'
        self.bot.send_message(
            chat_id=self.channel, 
            text=msg,
            parse_mode=telegram.ParseMode.HTML
        )

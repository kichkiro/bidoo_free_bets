# StdLib
from configparser import SectionProxy

# Extlib (requirements.txt)
import telegram

class PyBot:
    """
    This class represent a telegram bot.
    """
    settings: SectionProxy

    def __init__(self, config: SectionProxy) -> None:
        self.settings = config
        self.token = self.settings["BOT_TOKEN"]
        self.channel = self.settings["CHANNEL"]
        self.bot = telegram.Bot(token=self.token)

    def send_msg(self, link: str, body: str) -> None:
        """
        This method allows sending a message.
        """
        def add_fire(body: str) -> str:
            """
            This method allows you to add the fire emoji for a certain 
            number of times as the number of bets if different from 1.
            """
            n = ''
            for char in body:
                if char != ' ':
                    n += char
                else:
                    break
            n = int(n)
            if n != 1:
                new_body = f"{body} "
                for _ in range(n):
                    new_body += "🔥"
                return new_body
            return body

        msg = f'<b>{add_fire(body)}</b> {link}'
        self.bot.send_message(
            chat_id=self.channel, 
            text=msg,
            parse_mode=telegram.ParseMode.HTML
        )

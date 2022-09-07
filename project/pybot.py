import telegram

class PyBot:
    def __init__(self, token: str, channel: str):
        self.token = token
        self.channel = channel
        self.bot = telegram.Bot(token=self.token)

    def send_msg(self, link: str, body: str):
        msg = f'<b>{body}</b> {link}'
        self.bot.send_message(
            chat_id=self.channel, 
            text=msg,
            parse_mode=telegram.ParseMode.HTML
        )

# Stdlib
import os
import requests
import webbrowser
from configparser import SectionProxy

# Extlib (requirements.txt)
from msal import SerializableTokenCache, PublicClientApplication


class Email:
    """

    """
    settings: SectionProxy

    def __init__(self, config: SectionProxy) -> None:
        self.settings = config
        self.client_id = self.settings["clientId"]
        self.graph_scopes = self.settings["graphUserScopes"].split(" ")

    def generate_access_token(self) -> dict:
        """
        
        """
        # Save Session Token as a token file
        access_token_cache = SerializableTokenCache()

        # Read the token file
        if os.path.exists('ms_graph_api_token.json'):
            access_token_cache.deserialize(
                open('ms_graph_api_token.json', 'r').read())

        # Assign a SerializableTokenCache object to the client instance     
        client = PublicClientApplication(
            client_id=self.client_id, token_cache=access_token_cache)
        
        accounts = client.get_accounts()
        if accounts:
            # Load the session
            token_response = client.acquire_token_silent(
                scopes=self.graph_scopes, account=accounts[0])
        else:
            # Authenticate your account as usual
            flow = client.initiate_device_flow(scopes=self.graph_scopes)
            print(f"user code: {flow['user_code']}")
            webbrowser.open(flow['verification_uri'])
            token_response = client.acquire_token_by_device_flow(flow)

        with open('ms_graph_api_token.json', 'w') as _f:
            _f.write(access_token_cache.serialize())
        return token_response

    def read(self) -> dict:
        """
        
        """
        def get_email(self) -> dict:
            """
            Find emails sent by Bidoo and store content in json format.
            """
            GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'
            BIDOO_EMAIL = 'noreply@bidoo.com'

            access_token = self.generate_access_token()
            headers = {
                'Authorization': f"Bearer {access_token['access_token']}"}
            endpoint = f"{GRAPH_ENDPOINT}/me/messages"
            filter = f"(from/emailAddress/address) eq '{BIDOO_EMAIL}'"
            request_url = f"{endpoint}?$filter={filter}"
            response = requests.get(request_url, headers=headers)
            return response.json()

        def find_url(self) -> str:
            """
            
            """
        
        def find_body(self) -> str:
            """

            """

    def clear(self) -> None:
        """

        """


class WebPushNotification:
    """
    This class encloses the methods for "read" and "clean" the web push 
    notifications stored in logfile, for example the google-chrome push 
    notifications in Ubuntu 22.04LTS are located at the path: 
    "~/.config/google-chrome/Default/Platform Notifications/000003.log" 
    for ms-edge in Windows 11 are in: "~\AppData\Local\Microsoft\Edge\
    User Data\Default\EdgePushStorageWithWinRt\000003.log"
    """
    settings: SectionProxy

    def __init__(self, config: SectionProxy) -> None:
        self.settings = config
        self.logfile_path = self.settings["NOTIFICATION_LOGFILE_PATH"]
        self.history_path = self.settings["HISTORY_LOG_PATH"]

    def read(self) -> dict:
        """
        Search the log file to locate, by substrings, the link of the 
        bet (url) and the number of bets that contains the link (body).
        """
        def duplicate(url: str, history_path: str) -> int:
            """
            Checks if a link is not a duplicate and does so by comparing 
            it with the previous links stored in history.log
            """
            with open(history_path, 'r+') as history:
                for row in history:
                    if row == (url+"\n"):
                        return 1
                history.write(f"{url}\n")
                return 0

        msg = {}
        body_substring = "Puntat"
        url_substring = [
            "https://it.bidoo.com/gest_cod.php?",
            "https://es.bidoo.com/gest_cod.php?",
        ]

        with open(self.logfile_path, "rb") as file:
            for row in file:
                
                # Find URL (key)
                url, skip = "", 3
                for char in row:
                    if char == 34 and (url_substring[0] in url or \
                        url_substring[1] in url):
                        break
                    elif char == 34 and (url_substring[0] not in url or \
                        url_substring[1] not in url):
                        url, skip = "", 3
                    if skip > 0:
                        skip -= 1
                        continue
                    url += chr(char)

                # Find body (value)
                body, check_number = "", False
                for char in row:
                    if body_substring in body:
                        body += chr(char)
                        break
                    if char >= 48 and char <= 57:
                        check_number = True
                    if check_number:
                        body += chr(char)

                # Add to dict
                if body_substring not in body:
                    body = "1 Puntata"
                if url_substring[0] in url or url_substring[1] in url:
                    if not duplicate(url, self.history_path):
                        msg[url] = body
        return msg

    def clear(self) -> None:
        """
        Clean the log file.
        """
        with open(self.logfile_path, "r+") as file:
            file.truncate(0)

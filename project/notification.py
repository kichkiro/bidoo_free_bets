class Email:
    pass

class WebPushNotification:
    
    def __init__(self, logfile_path: str):
        self.logfile_path = logfile_path

    def read(self) -> dict:

        msg = {}
        body_substring = "Puntat"
        url_substring = [
            "https://it.bidoo.com/gest_cod.php?",
            "https://es.bidoo.com/gest_cod.php?",
        ] 


        with open(self.logfile_path, 'rb') as file:

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
                    msg[url] = body
        return msg

    def clear(self):

        with open(self.logfile_path, 'r+') as file:
            file.truncate(0)

class SMS():
    pass
                
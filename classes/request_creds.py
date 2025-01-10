# Class for requests
class RequestCreds:
    def __init__(self, url, payload, headers):
        self.url = url
        self.payload = payload
        self.headers = headers
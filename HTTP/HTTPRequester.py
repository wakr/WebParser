

import urllib.request


class HttpRequester:

    @staticmethod
    def response_of(address):
        return urllib.request.urlopen("http://" + address).read()

import urllib3.request


class HttpRequester:
    """
    Simple HTTPRequester class
    """
    @staticmethod
    def get_response_of(address):
        """
        Produces a HTTP-GET and returns the whole contents of the html_file
        :param address: web-page
        :return: HTML-contents
        """
        http = urllib3.PoolManager()
        result = http.request('GET', 'http://' + address)
        return result.data

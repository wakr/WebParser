import queue
import threading

from HTML.HTMLParser import HtmlParser
from HTTP.HTTPRequester import HttpRequester


class Threader:

    def __init__(self):
        self.q = queue.Queue()

    def __send_n_parse(self, q, address):
        try:
            self.q.put({address: HtmlParser.get_parsed_of(HttpRequester.response_of(address))})
            print("Done: " + address)
        except Exception as e:
            self.q.put({address: str(e)})
            return

    def execute(self, webpages):

        results = []

        for address in webpages:
            t = threading.Thread(target=self.__send_n_parse, args = (self.q, address))
            t.daemon = True
            t.start()

        self.q.join()

        for page in webpages:
            results.append(self.q.get())

        return results
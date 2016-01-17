import queue
import threading

from HTML.HTMLParser import HtmlParser
from HTTP.HTTPRequester import HttpRequester


class Threader:
    """
    Handles threading inside the app.
    Enables concurrency for the http-requests.
    """

    def __init__(self):
        self.queue = queue.Queue()
        self.parser = HtmlParser()

    def execute(self, webpages):
        """
        Executes threading for webpage-parsing
        :param webpages: array which contains all urls in string-format
        :return: final results inside an array. Keys are the webpage names.
        """
        results = []

        self.__start_threading(webpages)
        self.__populate_result_array(results, webpages)

        return results

    def __populate_result_array(self, results, webpages):
        for page in webpages:
            results.append(self.queue.get())

    def __start_threading(self, webpages):
        for address in webpages:
            t = threading.Thread(target=self.__send_n_parse, args=(self.queue, address))
            t.daemon = True
            t.start()
        self.queue.join()

    def __send_n_parse(self, temp_queue, address):
        try:
            http_response = HttpRequester.get_response_of(address)
            parsed_response = self.parser.get_parsed_of(http_response)
            temp_queue.put({address: parsed_response})
            print("Done: " + address)
        except Exception as e:
            temp_queue.put({address: str(e)})
            return
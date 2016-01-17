import json
import pprint

from Thread.Threader import Threader


class TextInterface:
    """
    Ask url-queries, executes them and finally shows the result to the user.
    """
    def __init__(self):
        self.command_map = {'ask': self.__ask_pages,
                            'run': self.__run_queries,
                            'show': self.__show_results}
        self.queries = []
        self.results = []

    def start(self):
        """
        Asks pages -> Runs queries -> Shows results.
        """
        self.command_map['ask']()
        self.command_map['run']()
        self.command_map['show']()

    def __ask_pages(self):
        iterations = input("How many webpages you want to parse: ")

        for i in range(int(iterations)):
            address = input("Give a webpage: ")
            self.queries.append(address)

    def __run_queries(self):
        self.results = Threader().execute(self.queries)

    def __show_results(self):
            jsonified = json.dumps(self.results, ensure_ascii=False)
            pprint.pprint(json.loads(jsonified))

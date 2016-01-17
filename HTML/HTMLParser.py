from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner


class HtmlParser:
    """
    Parses the html-file to readable text
    """

    def __init__(self):
        self.cleaner = Cleaner()
        self.cleaner.javascript = True
        self.cleaner.style = True
        self.prettify_functions = [self.__remove_lonelystrings, self.__remove_whitespaces]

    def get_parsed_of(self, html_contents):
        """
        Main parse -functionality. Removes html-tags, whitespaces and lines with just one character
        :param html_contents: string in html-format
        :return: body-text of the html-file
        """
        res = self.cleaner.clean_html(html_contents)
        main_text = BeautifulSoup(res, 'lxml').get_text()\
            .strip().split("\n")

        return self.__prettify(main_text)

    def __prettify(self, main_text):
        for prettify_fn in self.prettify_functions:
            main_text = prettify_fn(main_text)
        return main_text

    def __remove_whitespaces(self, content_array):
        filtered_array = []
        for text_line in content_array:
            text_line = text_line.strip()
            if text_line:
                filtered_array.append(text_line)

        return filtered_array

    def __remove_lonelystrings(self, content_array):
        return filter(lambda x: len(x) > 1, content_array)

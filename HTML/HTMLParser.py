from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner



class HtmlParser:

    @staticmethod
    def get_parsed_of(html_contents):
        cleaner = Cleaner()
        cleaner.javascript = True
        cleaner.style = True

        res = cleaner.clean_html(html_contents)
        souped = BeautifulSoup(res, 'lxml')
        main_text = souped.get_text().strip()
        main_text = main_text.split("\n")

        main_text = HtmlParser.__remove_whitespaces(main_text)
        main_text = HtmlParser.__remove_lonelystrings(main_text)

        return main_text

    @staticmethod
    def __remove_whitespaces(content_array):
        filtered_array = []
        for text_line in content_array:
            text_line = text_line.strip()
            if text_line:
                filtered_array.append(text_line)

        return filtered_array

    @staticmethod
    def __remove_lonelystrings(content_array):
        filtered_array = []
        for text_line in content_array:
            if len(text_line) > 1:
                filtered_array.append(text_line)

        return filtered_array
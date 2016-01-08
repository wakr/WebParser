from HTML.HTMLParser import HtmlParser
from HTTP.HTTPRequester import HttpRequester


def main():

    address = input("Give a webpage: ")

    try:
        res = HttpRequester.response_of(address)
    except:
        print("Requested URL is invalid!")
        return
    parsed = HtmlParser.get_parsed_of(res)

    for line in parsed:
        print(line)


if __name__ == '__main__':
    main()
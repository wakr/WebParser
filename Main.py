from Thread.Threader import Threader


def main():

    webpages = []
    iterations = input("How many webpages you want to parse: ")

    ask_webpages(iterations, webpages)

    t = Threader()
    results = t.execute(webpages)

    print(results)


def ask_webpages(iterations, webpages):
    for i in range(int(iterations)):
        address = input("Give a webpage: ")
        webpages.append(address)


if __name__ == '__main__':
    main()
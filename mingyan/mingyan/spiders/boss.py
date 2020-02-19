import requests
from bs4 import BeautifulSoup
def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.guazi.com/cq/buy/h' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'target': '_blank'}):
            href = "https://www.guazi.com" + link.get('href')
            title = link.string

            if title:
                print(href)
                print(title)
                fw = open("web.txt", "a")
                fw.write(href + '\n')
                fw.write(title + '\n')
                fw.close()

        page += 1
spider(10)

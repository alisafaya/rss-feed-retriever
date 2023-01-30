import datetime
import json

import bs4, requests

url = "https://www.estadao.com.br/"
currentDate = datetime.datetime.now()
try:
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    jsonOutput = []
    seenLinks = []

    for result in soup.select('.chapeu'):
        for linkList in result.select('a'):
            output = {
                "link": linkList.get('href'),
                "year": currentDate.year,
                "month": currentDate.month,
                "day": currentDate.day
            }
            if linkList.get('href') in seenLinks:
                continue
            else:
                jsonOutput.append(output)
                seenLinks.append(linkList.get('href'))

    for result in soup.select('.manchete-content'):
        for linkList in result.select('a'):
            output = {
                "link": linkList.get('href'),
                "year": currentDate.year,
                "month": currentDate.month,
                "day": currentDate.day
            }

            if linkList.get('href') in seenLinks:
                continue
            else:
                jsonOutput.append(output)
                seenLinks.append(linkList.get('href'))

    for result in soup.select('.related-news-item'):
        for linkList in result.select('a'):
            output = {
                "link": linkList.get('href'),
                "year": currentDate.year,
                "month": currentDate.month,
                "day": currentDate.day
            }
            if linkList.get('href') in seenLinks:
                continue
            else:
                jsonOutput.append(output)
                seenLinks.append(linkList.get('href'))

    for result in soup.select('.bullets'):
        for linkList in result.select('a'):
            output = {
                "link": linkList.get('href'),
                "year": currentDate.year,
                "month": currentDate.month,
                "day": currentDate.day
            }
            if linkList.get('href') in seenLinks:
                continue
            else:
                jsonOutput.append(output)
                seenLinks.append(linkList.get('href'))

    for result in soup.select('.carousel-item-especiais'):
        for linkList in result.select('a'):
            output = {
                "link": linkList.get('href'),
                "year": currentDate.year,
                "month": currentDate.month,
                "day": currentDate.day
            }
            if linkList.get('href') in seenLinks:
                continue
            else:
                jsonOutput.append(output)
                seenLinks.append(linkList.get('href'))


    for result in soup.select('.carousel-item-blog-coluna'):
        for linkList in result.select('a'):
            output = {
                "link": linkList.get('href'),
                "year": currentDate.year,
                "month": currentDate.month,
                "day": currentDate.day
            }
            if linkList.get('href') in seenLinks:
                continue
            else:
                jsonOutput.append(output)
                seenLinks.append(linkList.get('href'))

    data = ""
    try:
        with open("estadao_today_news.json", "r+") as outfile:
            data = json.loads(outfile.read())
            print(data)
            for news in jsonOutput:
                print(news)
                data['articles'].append(news)
            print(data)
            with open("estadao_today_news.json", "w") as outfile:
                outfile.write(str(data).replace("'", '"'))
    except:
        with open("estadao_today_news.json", "w") as outfile:
            outfile.write('{"articles": []}')

except Exception as e:
    print(e)
    pass
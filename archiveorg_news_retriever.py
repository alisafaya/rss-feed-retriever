import bs4, requests

#Change the starting date for the snapshot date
yearNumber = "2010"
monthNumber = "01"
dayNumber = "01"
hourNumber = "00"
lastUrl = ""

#Change the ending year or add a condition to determine ending point with this while loop
while yearNumber < "2016":

    urlHour = hourNumber + "0000"
    # Change news website url
    newsWebsiteLink = "http://www.estadao.com.br"

    if (monthNumber == "12" and dayNumber == "31"):
        yearNumber = str(int(yearNumber) + 1)
        monthNumber = "01"
        dayNumber = "01"
    elif (dayNumber == "31"):
        if int(monthNumber) < 9:
            monthNumber = "0" + str(int(monthNumber) + 1)
            dayNumber = "00"
        else:
            monthNumber = str(int(monthNumber) + 1)
            dayNumber = "00"

    if int(hourNumber) == 23:
        if int(dayNumber) < 9:
            dayNumber = "0" + str(int(dayNumber) + 1)
            hourNumber = "00"
        else:
            dayNumber = str(int(dayNumber) + 1)
            hourNumber = "00"
    else:
        if int(hourNumber) < 9:
            hourNumber = "0" + str(int(hourNumber) + 1)
        else:
            hourNumber = str(int(hourNumber) + 1)

    urlPart = yearNumber + monthNumber + dayNumber + urlHour
    finalUrl = "https://web.archive.org/web/{}/{}/".format(urlPart,newsWebsiteLink)

    try:
        res = requests.get(finalUrl)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        jsonOutput = []
        seenLinks = []
        retrievedSnapshotLink = res.url

        if lastUrl == res.url:
            continue
        else:
            #Put your css selectors here, example css selector:
            for result in soup.select('.c-main-headline__url'):
                output = {
                    "link": result.get('href'),
                    "year": "2019",
                    "month": monthNumber
                }

                jsonOutput.append(output)

            lastUrl = retrievedSnapshotLink
    except:
        lastUrl = retrievedSnapshotLink
        pass
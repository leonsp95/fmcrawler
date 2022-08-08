from googletrans import Translator
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests


def checkExistence(finalTitles, finalYear, mediaType):
    url = "https://movie-database-alternative.p.rapidapi.com/"
    chosenName = ""

    for testNames in finalTitles:
        querystring = {"s": testNames, "r": "json",
                       "type": mediaType, "y": finalYear, "page": "1"}
        headers = {
            # YOUR API-KEY HERE
            # YOUR API-HOST HERE
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring).json()
        try:
            response["Search"][0]["Title"]
            chosenName = response["Search"][0]["Title"]
            return response["Search"][0]["Title"]
        except:
            pass
    if chosenName == "":
        chosenName = finalTitles[0]
        return chosenName
    else:
        return chosenName


def main(pageURL, finalYear, mediaType):
    translator = Translator()
    url = Request(pageURL,
                  headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(url)
    dados = BeautifulSoup(html, 'lxml')
    mainTitle = dados.find("h1", itemprop="name").text
    origTitle = dados.find(
        'h2', {'class': 'movie-original-title'}).text.strip()
    otherTitles = []
    finalTitles = []
    detectMainTitle = translator.detect(mainTitle)
    detectOriginTitle = translator.detect(origTitle)

    if ((detectMainTitle.lang != "en") or ((detectMainTitle.lang == "en") and (detectMainTitle.confidence < 1))):
        if (detectOriginTitle.lang != "en"):
            if dados.find("div", class_="movie-other-titles"):
                for x in dados.find("div", class_="movie-other-titles").findAll("li"):
                    otherTitles.append(x.text.split("-")[0].strip())
                otherTitles.extend([mainTitle, origTitle])

                for givenTitle in otherTitles:
                    result = translator.detect(givenTitle)
                    if ((result.lang == "en") and (result.confidence >= 0.2)):
                        finalTitles.append(givenTitle)
                if (not finalTitles):
                    finalTitles.append(origTitle)
                if len(finalTitles) > 1:
                    return checkExistence(finalTitles, finalYear, mediaType)
                else:
                    return finalTitles
            else:
                return origTitle
        else:
            return origTitle
    else:
        return mainTitle


if __name__ == "__main__":
    main()

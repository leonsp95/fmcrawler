from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
from checker import main as checkName
from csvgen import main as csvGen
from PIL import Image
from pyzbar.pyzbar import decode
import os
import qrcode
from time import sleep
from rich.console import Console

finalMovieList = []


def pageCrawler(pageURL, mediaType):
    transMediaType = ""
    if (mediaType) == "filmes":
        transMediaType == "movies"
    elif (mediaType) == "series":
        transMediaType == "series"
    url = Request(pageURL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(url)
    bs = BeautifulSoup(html, 'lxml')
    try:
        finalYear = bs.find(
            'small', {'class': 'release'}).get_text().strip()
    except AttributeError:
        tryYear = bs.find(
            'div', {'class': 'item release_date'})
        altYear = tryYear.find("div").get_text().strip()[-4:]
        finalYear = altYear
    treatedMovie = ''.join(checkName(pageURL, finalYear, transMediaType))
    finalMovie = getDataFromAPI(treatedMovie, finalYear, transMediaType)
    return finalMovie


def getDataFromAPI(title, year, mediaType):
    finalMovie = {'title': None, 'year': None, 'imdbcode': None}
    url = "https://movie-database-alternative.p.rapidapi.com/"

    querystring = {"s": title, "r": "json",
                   "type": mediaType, "y": year, "page": "1"}

    headers = {
        # YOUR API-KEY HERE
        # YOUR API-HOST HERE
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring).json()
    try:
        response["Search"][0]["imdbID"]
        finalMovie['title'] = title
        finalMovie['year'] = str(year)
        finalMovie['imdbcode'] = str(
            "https://www.imdb.com/title/" + response["Search"][0]["imdbID"])
        finalMovieList.append(finalMovie)
    except:
        finalMovie['title'] = title
        finalMovie['year'] = year
        finalMovie['imdbcode'] = "IMDb não encontrado"
        finalMovieList.append(finalMovie)
    return finalMovie


def main(username, mediaType, mediaCategory):
    os.system('clear')
    baseURL = "https://filmow.com"
    srcLink = f"https://filmow.com/usuario/{username}/{mediaType}/{mediaCategory}/"
    ammountMovies = 0
    pageNumber = 1

    while True:
        url = Request(srcLink, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(url)
        bs = BeautifulSoup(html, 'lxml')
        filmowPage = bs.findAll('span', attrs={'class': 'wrapper'})
        #
        console = Console()
        tasks = [f"task {movieContainer}" for movieContainer in filmowPage]
        with console.status(f"[bold green] Analisando lista de {mediaType}...") as status:
            for movieContainer in filmowPage:
                movieData = movieContainer.find(
                    'a', attrs={'class': 'cover tip-movie'})
                finalLink = baseURL + (movieData.attrs['href'])
                movieDataFFF = pageCrawler(finalLink, mediaType)
                ammountMovies += 1
                task = tasks.pop(0)
                sleep(1)
                console.log(
                    f"{mediaType.capitalize()} analisados(as): {str(ammountMovies).rjust(3,' ')} | {movieDataFFF['title']} ({movieDataFFF['year']}) ")

        nextPage = bs.find('a', attrs={'id': 'next-page'})
        if ((nextPage) and nextPage.get("href")):
            pageNumber += 1
            srcLink = baseURL + nextPage.attrs["href"]
            print(
                f"\nVerificação da página {pageNumber-1} finalizada.\nVerificando a página {pageNumber} agora...\n\n")
        else:
            break
    userPath = csvGen(finalMovieList)
    print("\nA lista .csv foi gerada com sucesso.\nSe o programa ajudou você, considere fazer uma doação através do PIX.\n")
    read = decode(Image.open("./src/pixqrcode.png"))
    qr = qrcode.QRCode()
    qr.add_data(read[0].data)
    qr.print_ascii(invert=True)
    sleep(1)
    print(
        f"Processo finalizado com êxito.\nO arquivo foi gerado em {userPath}.")


if __name__ == "__main__":
    main()

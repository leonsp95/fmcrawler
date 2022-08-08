
import os
import csv
from datetime import datetime


def main(finalMovieList):
    userPath = os.path.expanduser("~")
    dateTag = datetime.now().strftime(f"%Y_%m_%d-%H-%M-%S")
    f = open(f"{userPath}/lista_{dateTag}.csv",
             'w', newline='', encoding='UTF-8')
    w = csv.writer(f, delimiter=";")
    w.writerow(["Nome", "Ano", "Link IMDb"])
    w.writerow(["", "", ""])
    for i in finalMovieList:
        w.writerow([i['title'].replace(",", ""), i['year'], i['imdbcode']])
    f.close()
    return userPath


if __name__ == "__main__":
    main()

from maincrawler import main as mainChecking
from checkusername import main as checkUserName
from time import sleep
import os


def main():
    print('''
   ▄████████   ▄▄▄▄███▄▄▄▄    ▄████████    ▄████████    ▄████████  ▄█     █▄   ▄█          ▄████████    ▄████████
  ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███   ███    ███ ███     ███ ███         ███    ███   ███    ███
  ███    █▀  ███   ███   ███ ███    █▀    ███    ███   ███    ███ ███     ███ ███         ███    █▀    ███    ███
 ▄███▄▄▄     ███   ███   ███ ███         ▄███▄▄▄▄██▀   ███    ███ ███     ███ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀
▀▀███▀▀▀     ███   ███   ███ ███        ▀▀███▀▀▀▀▀   ▀███████████ ███     ███ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███        ███   ███   ███ ███    █▄  ▀███████████   ███    ███ ███     ███ ███         ███    █▄  ▀███████████
  ███        ███   ███   ███ ███    ███   ███    ███   ███    ███ ███ ▄█▄ ███ ███▌    ▄   ███    ███   ███    ███
  ███         ▀█   ███   █▀  ████████▀    ███    ███   ███    █▀   ▀███▀███▀  █████▄▄██   ██████████   ███    ███
                                          ███    ███                          ▀                        ███    ███
    ''')
    print("                                              Bem-vindo ao FilmowCrawler\n  Gere uma lista csv de seus filmes do Filmow com links do IMDb e poupe tempo atualizando as suas listas do IMDb\n")
    print("\nVisite o repositório do projeto no GITHUB:\n\u25BA https://bit.ly/3POSGVA \u25C4\n")

    while (True):
        username = input("Para começar, digite o seu nome de usuário:\n\n")
        validUsrName = checkUserName(username)
        if(validUsrName):
            break
        else:
            print("\nUsuário não existe. Tente novamente.\n")
    sleep(3)
    os.system('clear')
    while(True):
        mediaType = input(
            "Agora, escolha o tipo de mídia que deseja:\n\n1. FILMES\n2. CURTAS\n3. SÉRIES\n\n")
        if mediaType == "1":
            mediaType = "filmes"
            break
        elif mediaType == "2":
            mediaType = "curtas"
            break
        elif mediaType == "3":
            mediaType = "series"
            break
        else:
            print("\nPor favor, digite apenas os valores mostrados.\n")
    os.system('clear')
    while(True):
        mediaCategory = input(
            "\nEscolha a categoria:\n1. JÁ VI\n2. QUERO VER\n3. NÃO QUERO VER\n4. FAVORITOS\n\n")
        if mediaCategory == "1":
            mediaCategory = "ja-vi"
            break
        elif mediaCategory == "2":
            mediaCategory = "quero-ver"
            break
        elif mediaCategory == "3":
            mediaCategory = "nao-quero-ver"
            break
        elif mediaCategory == "4":
            mediaCategory = "favoritos"
            break
        else:
            print("Por favor, digite apenas os valores mostrados.\n")
    mainChecking(username, mediaType, mediaCategory)


if __name__ == "__main__":
    main()

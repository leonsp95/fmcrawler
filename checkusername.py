from urllib.request import urlopen


def main(username):
    validName = None
    try:
        with urlopen(f"https://filmow.com/usuario/{username}", timeout=10):
            validName = True
    except:
        validName = False
    return validName


if __name__ == "__main__":
    main()

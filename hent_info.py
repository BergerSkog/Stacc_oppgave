import requests
from bs4 import BeautifulSoup


def hentInfoGoogle(navn):
    # Henter info om kunden fra google sin oppsummering
    try:
        linkNavn = navn.replace(' ', '+')
        URL = 'https://www.google.com/search?q=' + linkNavn
        cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}

        r = requests.get(URL, cookies=cookies)
        soup = BeautifulSoup(r.content, 'html.parser')

        # Returnerer teksten fra google sin oppsummering
        return soup.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'}).text
    except:
        return "Data ikke tilgjengelig"


def hentInfoWikipedia(navn):
    # Henter første avsnitt fra wikipedia siden til kunden
    try:
        linkNavn = ""
        # formaterer navnet slik at det passer med wikipedia sin formatering
        for i in navn.split():
            linkNavn += i.capitalize() + "_"

        URL = 'https://no.wikipedia.org/wiki/' + linkNavn
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')

        # Returnerer første avsnitt fra wikipedia
        return soup.find('p').text
    except:
        return "Data ikke tilgjengelig"

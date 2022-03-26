import requests
from bs4 import BeautifulSoup
import time

def hentInfoGoogle(navn):
    #Henter info om kunden fra google sin oppsummering
    linkNavn = navn.replace(' ', '+')
    URL = 'https://www.google.com/search?q=' + linkNavn
    cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}
    r = requests.get(URL, cookies=cookies)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find('div', {'class':'BNeawe s3v9rd AP7Wnd'}).text

def hentInfoWikipedia(navn):
    #Henter første avsnitt fra wikipedia siden til kunden
    linkNavn = ""
    for i in navn.split():
        linkNavn += i.capitalize() + "_"
    print(linkNavn)

    URL = 'https://no.wikipedia.org/wiki/' + linkNavn
    print(URL)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find('p').text
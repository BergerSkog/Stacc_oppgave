import requests
import hent_info

kundeNavn = "Knut Arild Hareide"
knut = {"numberOfHits":2,"hits":[{"score":0.0003451437393358565,"id":"evpo-ff10bc5a-4aad-4895-b886-fb88e598ed57","schema":"Person","name":"Knut Arild Hareide","aliases":"Hareide, Knut Arild","birth_date":"1972-11-23","countries":"no","identifiers":"Q1350399","sanctions":"","phones":"","emails":"","dataset":"Every Politician","last_seen":"2021-07-26 11:55:45","first_seen":"2021-10-07 03:02:59"},{"score":0.01857804455091699,"id":"us-cia-norway-knut-arild-hareide-min-of-transportation-communications","schema":"Person","name":"Knut Arild HAREIDE","aliases":"","birth_date":"","countries":"no","identifiers":"","sanctions":"","phones":"","emails":"","dataset":"CIA World Leaders","last_seen":"2021-07-26 11:55:45","first_seen":"2021-10-07 03:02:59"}]}

kunde = knut #hentData(navn)

def hentDataApi(kundeNavn):
    #Kjører en get request på api-en med kundens navn
    x = eval(requests.get("https://code-challenge.stacc.dev/api/pep?name=" + kundeNavn).text)
    data = ''
    if len(x["hits"]) == 0: #Personen er ikke flagget
        return "No data in database."
    data += "Antall treff: " + str(x["numberOfHits"]) + ". Fra"
    for i in x["hits"]:
        data += " " + i["dataset"] + ","

    return data[:-1] + '.'

def hentDataCsv(kundeNavn):
    kundeNavn = kundeNavn.upper()
    flags = 0
    data = []
    with open('pep.csv', encoding="utf-8") as csv_file:
        for row in csv_file:
            if kundeNavn in row.upper():
                data.append(eval("[" + row + "]")[11])
    return data


def main(getInfo):
    for i in kunde["hits"]:
        print(i["dataset"])
    if getInfo:
        info = hent_info.hentInfoWikipedia("Jens stoltenberg")


if __name__ == "__main__":
    print(hentDataCsv("Knut Arild Hareide"))

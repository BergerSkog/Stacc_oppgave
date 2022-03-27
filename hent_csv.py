import requests
import hent_info
import csv

def hentDataCsv(kundeNavn):
    #Løper gjennom csv filen og leter etter personen
    #Noterer seg alle databasene personen er funnet i

    kundeNavnStor = kundeNavn.upper()
    data = ''
    flags = 0

    #Åpner pep.csv filen og løper gjennom hver linje
    with open('pep.csv', encoding="utf-8") as csv_file:
        read_csv = csv.DictReader(csv_file)
        for row in read_csv:
            if kundeNavnStor in row["name"].upper():
                data += ' ' + row['dataset'] + ','
                flags += 1
    #Returnerer en streng som blir skrevet til index.html
    if data == '':
        return kundeNavn + " er ikke flagget"
    else:
        data = kundeNavn + " er flagget. Antall treff: " + str(flags) + ". Fra" + data
        return data[:-1] + '.'


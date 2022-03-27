import requests

liste = []

print(liste)

print(len(liste))

alleRoller = []
teller =0
for i in liste[:10000]:
    print(i)
    teller += 1
    print(teller)
    alleRoller.append(requests.get("https://code-challenge.stacc.dev/api/roller?orgNr/=" + i).text)

    print(alleRoller)

with open("alleRoller.txt", "w+", encoding="utf-8") as l:
    l.write(str(alleRoller))
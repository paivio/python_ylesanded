from random import *
from easygui import *

# Küsime mängija nime ja tutvustame reegleid:
nimi = enterbox('Tere tulemast viktoriinile "Põlvamaa korvpall". \nViktoriini alustamiseks palun sisesta oma nimi ja vajuta nuppu "OK".')

# Loeme küsimused_vastused failist järjendisse:
kysimus_fail = open("kysimus.txt", encoding="UTF-8")
vastus_fail = open("vastus.txt", encoding="UTF-8")

küsimused = []
for i in kysimus_fail:
    küsimused.append(i.strip("\n"))
kysimus_fail.close()

vastused = []
for j in vastus_fail:
    vastused.append(j.strip("\n"))
vastus_fail.close()

# Kuvame küsimused, kontrollime vastuse õigsust, kvame punktid küsimuse kohta ja arvutame punktide kogusumma:
m = 0
punkte_kokku = 0
while m < 10:
    jrk = randint(0, len(vastused)-1)
    nupud = ["A", "B", "C", "Lõpeta"]
    küsimus = küsimused[jrk]
    vajutati = buttonbox(küsimus, choices=nupud)

    punktid = 0
    if vajutati == vastused[jrk]:
        tulemus = "õige!"
        punktid += 1
    elif vajutati == "Lõpeta":
        exit()
    else:
        tulemus = "vale."

    msgbox("Vastus on " + tulemus + " Punkte selle vastuse eest " + str(punktid) + ".")
    punkte_kokku += punktid
    m += 1

# Kuvame punktide kogusumma:
msgbox("Hea mäng " + nimi + "! Punkte kokku " + str(punkte_kokku) + ".")
tulemus = "Mängija " + nimi + " punktide arv selles viktoriinis oli " + str(punkte_kokku) + "/10."
    
# Kirjutame mängu tulemused faili (kõikide mängijate tulemused üksteise all):
tulemused_fail = open("tulemused.txt", "a")
tulemused_fail.write(tulemus)
tulemused_fail.close()

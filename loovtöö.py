# Programm testib kasutaja selgeltnägemisvõimet läbi arvude ära arvamise.
# Arvata saab viis arvu, igal kolm katset. Programm annab vihjeid, kui pakutud arv on liiga suur/väike.
# Lõpuks väljastatakse kogutud punktide arv ning preemiaks väike täheke (tahad või ei taha).
# Esimese korraga ära arvamine annab kolm punkti, teisega kaks ja kolmadaga ühe punkti.

from turtle import *
from random import *
from easygui import *
from time import sleep


# Funktsioon, mis joonistab tähekese:
def täheke():
    bgcolor("navy blue")
    color("yellow")
    begin_fill()
    i = 0
    while i < 8:
        fd(300)
        lt(180-45)
        i += 1
    end_fill()
    exitonclick()
    

# Tekstikast, mis selgitab reegleid:
msgbox("Testi oma selgeltnägemisvõimet!\nGenereerin viis juhuslikku arvu vahemikus 1-10.\nSaad iga kord arvamiseks kolm katset.\nAlustamiseks vajuta 'OK'")

# Viie juhusliku arvu genereerimine ja kolm pakkumist neile:
i = 5
summa = 0
while i > 0:
    kordi = 3
    punkte = 0
    juhuslik_arv = randint(1, 10)
    pakutud_arv = integerbox("Paku, millisele arvule mõtlen: ")
    if juhuslik_arv == pakutud_arv:
        msgbox("Super! Õige vastus.")
        punkte = 3
    else:
        while kordi > 1:
            if juhuslik_arv == pakutud_arv:
                msgbox("Super! Õige vastus.")
                punkte = kordi
                break
            elif juhuslik_arv > pakutud_arv:
                kordi -= 1
                pakutud_arv = integerbox("Liiga vähe. Proovi uuesti: ")
            else:
                kordi -= 1
                pakutud_arv = integerbox("Liiga palju. Proovi uuesti: ")
    i -= 1
    summa += punkte

# Punktisumma väljastamine:
if summa > 10:
    msgbox("Kogusid " + str(summa) + " punkti.\nVau! Super tulemus. Peaksid kaaluma selgeltnägija karjääri.")
elif summa > 5:
    msgbox("Kogusid " + str(summa) + " punkti. \nVäga hästi!")
else:
    msgbox("Kogusid " + str(summa) + " punkti. \nArenguruumi veel on.")
    
# Tähekese joonistamine (tahad või ei):
variandid = ["Muidugi tahan!", "Ei ole vaja."]
valik = buttonbox("Tahad, ma joonistan sulle tähekese?", choices=variandid)
if valik == "Muidugi tahan!":
    täheke()
else:
    variandid = ["Hea küll, joonista.", "Ma ei taha."]
    valik = buttonbox("Oled kindel? Äkki ma ikka joonistan?", choices=variandid)
    if valik == "Hea küll, joonista.":
        täheke()
    else:
        sleep(1)
        msgbox("Aga ma joonistan ikka.")
        täheke()

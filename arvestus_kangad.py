# Defineeri funktsioon, mis võtab argumentideks kanga meetri hinna ning soovitud koguse (meetrites) ja tagastab ostu kogusumma
# ümardatuna kahe komakohani. Kanga hinnale (meetri hind * kogus meetrites) lisandub ka kardinate valmistamise tasu 8 eurot.
# Kampaania tõttu ei lisandu valmistamise tasu juhul, kui kangast ostetakse rohkem kui kuus meetrit.
# Lisaks koosta programm, mis...
# · Küsib kasutajalt failinime, tema eelarve (ujukomaarvuna) ning soovitud kanga koguse (ujukomaarvuna).
# · Loeb tekstifailist järjendisse kangaste meetrihinnad.
# · Väljastab defineeritud funktsiooni abil iga kanga ostu kogusumma. Kui ostu maksumus ületab kasutaja eelarvet, tuleb kasutajat
# sellest teavitada. NB! Kood peaks töötama sõltumata sellest, mitu rida tekstifailis on!
# · Küsib kasutajalt, mitmendat kangast ta osta soovib. (Võib eeldada, et kasutaja ei vali toodet, mis on tema jaoks liiga kallis.)
# · Väljastab ekraanile, kui palju raha kulus kasutajal ostu peale ning kui palju alles jäi (samuti ümardatuna 2 komakohani).

def ostusumma(meetri_hind, kogus):
    if kogus < 6.0:
        hind = meetri_hind * kogus + 8.0
    else:
        hind = meetri_hind * kogus
    return round(hind, 2)

failinimi = input("Sisesta failinimi: ")
eelarve = float(input("Sisesta eelarve: "))
kogus = float(input("Sisesta kogus: "))

fail = open(failinimi, encoding="UTF-8")

hinnad = []
for i in fail:
    hinnad.append(float(i.strip("\n")))
fail.close()

jrk = 0
while jrk < len(hinnad):
    hind = ostusumma(hinnad[jrk], kogus)
    if hind > eelarve:
        print(str(jrk + 1) + ". toote maksumus on " + str(hind) + " eurot. --See on liiga kallis!")
        jrk += 1
    else:
        print(str(jrk + 1) + ". toote maksumus on " + str(hind) + " eurot.")
        jrk += 1

mitmes = int(input("Mitmendat toodet osta soovid: "))
raha_tagasi = round(eelarve - ostusumma(hinnad[mitmes - 1], kogus), 2)

print("Ost sooritatud! Kokku kulus " + str(ostusumma(hinnad[mitmes - 1], kogus)) + " eurot. Alles jäi " + str(raha_tagasi) + " eurot.")

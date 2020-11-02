# Koostada funktsioon lõimede_pikkus, mis võtab argumentideks vaiba lõpp-pikkuse (ujukomaarv) ja lõimede arvu (täisarv),
# arvutab ja tagastab vaiba lõimede kogupikkuse ümardatuna sajandikeni.
# Koostada programm, mis küsib kasutajalt failinime, kus on vaipade lõpp-pikkused ujukomaarvudena meetrites eraldi ridadel,
# kõrvuti olevate lõimede arvu 5-meetriste ja pikemate vaipade puhul (täisarv),
# kõrvuti olevate lõimede arvu lühemate vaipade puhul (täisarv);
# loeb failist vaipade pikkused,
# arvutab (funktsiooni lõimede_pikkus abil) ja väljastab ekraanile iga vaiba lõimede kogupikkuse,
# arvutab ja väljastab ekraanile, kui palju läheb lõimeniiti vaja kõigi vaipade peale kokku ümardatuna sajandikeni.

failinimi = input("Sisestage faili nimi: ")
lõimed_üle_viis = int(input("Sisestage 5-meetriste ja pikemate vaipade lõimede arv: "))
lõimed_alla_viis = int(input("Sisestage lühemate vaipadde lõimede arv: "))

def lõimede_pikkus(pikkus, lõimede_arv):
    kogupikkus = (pikkus * 1.2 + 0.5) * lõimede_arv
    return round(kogupikkus, 3)

fail = open(failinimi, encoding="UTF-8")

pikkused = []
for i in fail:
    pikkused.append(float(i.strip("\n")))

summa = 0
j = 0
while j < len(pikkused):
    if pikkused[j] >= 5:
        pikkus = lõimede_pikkus(pikkused[j], lõimed_üle_viis)
        print(pikkus)
        j += 1
        summa += pikkus
    else:
        pikkus = lõimede_pikkus(pikkused[j], lõimed_alla_viis)
        print(pikkus)
        j += 1
        summa += pikkus
print("Kõigi vaipade peale läheb vaja " + str(summa) + " meetrit lõimeniiti.")
        
        
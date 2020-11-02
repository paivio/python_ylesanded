# Koostada funktsioon parandatud_tulemus, mis võtab argumentideks vigase tulemuse (meetrites) ja mõõteparanduse (sentimeetrites). Funktsioon arvutab tegeliku tulemuse (meetrites) ning tagastab selle. (tegelikTulemus = viganeTulemus + mõõteparandus / 100)
# Koostada programm, mis küsib kasutajalt
# failinime,
# mõõteparanduse (nt 35 näitab, et igale tulemusele tuleb liita 35 sentimeetrit (e 0,35 meetrit)),
# meistrivõistluste normatiivi.
# Programm peab
# lugema failist vigased tulemused (meetrites);
# (kasutades vastavat funktsiooni) arvutama tegelikud tulemused ja väljastama need ekraanile (ümardatuna kahe kümnendkohani pärast koma);
# arvutama ja väljastama ekraanile normatiivi täitnud tegelike tulemuste arvu ja nende keskmise (ümardatuna kahe kümnendkohani pärast koma).
# Kui normatiivi täitjaid ei ole, siis keskmist ei arvutata ega väljastata.ta ega väljastata.

def parandatud_tulemus(vigane_tulemus, mõõteparandus):
    tegelik_tulemus = vigane_tulemus + mõõteparandus/100
    return round(tegelik_tulemus, 2)

failinimi = input("Sisestage faili nimi: ")
parandus = int(input("Sisestage parandus sentimeetrites: "))
normatiiv = float(input("Sisestage meistrivõistluste normatiiv meetrites: "))

fail = open(failinimi, encoding="UTF-8")

tulemused = []
for i in fail:
    tulemused.append(float(i.strip("\n")))
fail.close()

print("Tegelikud tulemused")
j = 0
summa_norm = 0
loend_norm = 0

while j < len(tulemused):
    tegelik_tulemus = parandatud_tulemus(tulemused[j], parandus)
    print(tegelik_tulemus)
    if tegelik_tulemus >= normatiiv:
        summa_norm += tegelik_tulemus
        loend_norm += 1
        j += 1
    else:
        j += 1
        
keskmine = round(summa_norm / loend_norm, 2)

print("Normatiivi täitis " + str(loend_norm) + ".")
print("Täitnute keskmine on " + str(keskmine) + ".")

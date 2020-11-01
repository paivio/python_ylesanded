# Koostada programm, mis arvutab, kui palju inimene maksis poes koos käibemaksuga. Samuti arvutab programm, kui palju ta saab raha tagasi (kui lahkub riigist).
# Koostada funktsioon hind_käibemaksuga, mis võtab argumentideks käibemaksuta hinna ja käibemaksu protsendi ning arvutab käibemaksuga hinna ja tagastab selle. kmgaHind = kmtaHind * (1 + kmProtsent/100)
# Koostada programm, mis küsib kasutajalt
# failinime,
# käibemaksu protsendi,
# summa, millest alates saab tagasi käibemaksu.
# Programm peab
# lugema failist ilma käibemaksuta hinnad.
# arvutama ja väljastama ekraanile koos käibemaksuga hindade summa, mis on ümardatud kahe kohani peale koma. Käibemaksuga hindade arvutamisel kasutada funktsiooni hind_käibemaksuga.
# ümardama peab tulemuse, arvutuste ajal ümardada ei tohi.
# arvutama ja väljastama ekraanile, kui palju raha (ümardatuna kahe kohani pärast koma) inimene riigist lahkudes tagasi saab.
# ümardama peab tulemuse, arvutuste ajal ümardada ei tohi.

failinimi = input("Sisestage failinimi: ")
KM = int(input("Sisestage riigi käibemaks: "))
alates_tagasi = int(input("Sisestage summa, millest alates saab käibemaksu tagasi: "))

def hind_käibemaksuga(neto, protsent):
    bruto = neto * (1 + protsent/100)
    return bruto

fail = open(failinimi, encoding="UTF-8")

neto_järjend = []

for i in fail:
    neto_järjend.append(float(i.strip("\n")))
    
summa = 0
j = 0
tagasi_summa = 0

while j < len(neto_järjend):
    bruto = hind_käibemaksuga(neto_järjend[j], KM)
    j += 1
    summa += bruto
    if bruto > alates_tagasi:
        tagasi = bruto - bruto/(1 + KM/100)
        tagasi_summa += tagasi
    
ümard_summa = round(summa, 2)
ümard_tagasi = round(tagasi_summa, 2)
    
print("Kokku on kulutatud: " + str(ümard_summa))
print("Tagasi saab: " + str(ümard_tagasi))

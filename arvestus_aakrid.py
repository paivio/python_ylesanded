# Ühel omanikul on ainult ühe puuliigi metsad. Konkreetsete puuliikide puhul on teada aastane metsa juurdekasv hektari kohta tihumeetrites (tm/ha). Näiteks kase puhul võib see olla 4,8 tm/ha, kuuse puhul 6,6 tm/ha, männi puhul 3,7 tm/ha.
# Omanik tahab teada, mitu tihumeetrit metsa aastas teatud suurusest suuremates metsatükkides juurde kasvab.
# Koostada funktsioon juurdekasv, mis
# võtab argumentideks metsatüki pindala (ujukomaarv aakrites) ja metsa aastase juurdekasvu hektari kohta (ujukomaarv),
# tagastab selle pindalaga metsatüki aastase juurdekasvu ümardatuna sajandikeni.
# Koostada programm, mis
# küsib kasutajalt
# failinime (failis on eraldi ridadel metsatükkide pindalad aakrites);
# vastava puuliigi aastast juurdekasvu hektari kohta tihumeetrites (ujukomaarv);
# piiri, mitmest aakrist suuremad metsatükid arvesse võtta (ujukomaarv);
# loeb failist metsatükkide pindalad;
# arvutab (funktsiooni juurdekasv abil) ja väljastab metsatüki aastase juurdekasvu, kui selle metsatüki pindala on sisestatud piirist suurem;
# väljastab teate “Metsatükki ei võeta arvesse”, kui metsatüki pindala ei ole sisestatud piirist suurem;
# väljastab lõpuks ekraanile, mitme metsatüki juurdekasv arvutati.

def juurdekasv(pindala_aakrites, aasta_juurdekasv):
    kogu_juurdekasv = pindala_aakrites * 0.4047 * aasta_juurdekasv
    return round(kogu_juurdekasv, 2)

failinimi = input("Sisestage faili nimi: ")
aastas_juurde = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükis arvesse võtta: "))

fail = open(failinimi, encoding="UTF-8")

pindalad = []
for i in fail:
    pindalad.append(float(i.strip("\n")))
fail.close()

j = 0
mitu = 0
while j < len(pindalad):
    if pindalad[j] >= piir:
        kasv = juurdekasv(pindalad[j], aastas_juurde)
        print("Maatüki aastane juurdekasv on " + str(kasv))
        j += 1
        mitu += 1
    else:
        print("Maatükki ei võeta arvesse")
        j += 1
print("Arvutati " + str(mitu) + " metsatüki juurdekasv.")
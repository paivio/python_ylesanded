# Ühes firmas on komme kinkida töötajale juubeli (20, 30, 40, ... ) puhul kristallvaas. Vaaside tellimiseks on vaja loendada,
# mitmel töötajal on 2019. aastal juubel. Kõigi töötajate sünniaastad on kirjas tekstifailis (tehke see fail ise).
# Kui firmasse tuleb tööle uus töötaja, siis tahetakse teada, mitme töötajaga on tal sama sünniaasta.
# Koostage funktsioon juubelite_arv, mis saab argumendiks aastate järjendi ja tagastab mitmel töötajal on 2019. aastal juubel.
# Võimalik on kontrollida, kas aasta lõpeb 9-ga või vanus (2019 - aasta) jagub 10-ga.
# Koostada programm, mis
# • küsib kasutajalt, mis failis sünniaastad on;
# • loeb failist sünniaastad ja paneb need järjendisse;
# • arvutab ja väljastab ekraanile töötajate koguarvu;
# • arvutab (ülalmainitud funktsiooni abil) ja väljastab ekraanile nende töötajate arvu, kel on aastal 2019 juubel;
# • küsib kasutajalt uue töötaja sünniaasta ja väljastab ekraanile, mitu töötajat on sündinud temaga samal aastal.

failinimi = input("Sisesta faili nimi: ")

def juubelite_arv(järjend):
    summa = 0
    for i in järjend:
        if i[-1] == "9":
            summa += 1
    return summa

fail = open(failinimi, encoding="UTF-8")

järjend = []
for j in fail:
    järjend.append(j.strip("\n"))
fail.close()

töötajaid = len(järjend)
juubel = juubelite_arv(järjend)

print("Firmas on " + str(töötajaid) + " töötajat")
print("Aastal 2019 on  juubel " + str(juubel) + " töötajal")

aasta = int(input("Sisestage uue töötaja sünniaasta: "))

kokku = 0
for a in järjend:
    if aasta == int(a):
        kokku += 1

print(str(kokku) + " töötajat on sündinud samal aastal")    

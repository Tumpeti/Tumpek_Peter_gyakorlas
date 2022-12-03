import random

sorozat = [-3, 5, 11, -2, 4]

def separator(irasjel):
    i = 0
    sorozat_elvalasztoval = ""
    while i < len(sorozat)-1:
        sorozat_elvalasztoval += str(sorozat[i]) + irasjel
        i += 1
    sorozat_elvalasztoval += str(sorozat[-1])
    print(sorozat_elvalasztoval)


def veletlen_hozzaad(i):
    sorozat[i] = sorozat[i] + random.randint(5, 12)


def utolso_csere():
    paratlan_szam = int(input("Adj meg egy páratlan hárommal osztható kétjegyű számot! "))
    while paratlan_szam % 3 != 0 or paratlan_szam <= 10 or paratlan_szam % 2 == 0:
        paratlan_szam = int(input("Nem, jó! Páratlan, hárommal osztható kétjegyű számot kérek!"))
    sorozat.append(paratlan_szam)


separator("//")

veletlen_hozzaad(0)
print(sorozat)
utolso_csere()
print(sorozat)

"""list = [1,2,3,4]
list[0] = 11
print(list)"""

"""tomb = (1,2,3,4)
tomb[0] = 20
print(tomb)"""
# TypeError: 'tuple' object does not support item assignment Tehát a tömb nem módosítható!

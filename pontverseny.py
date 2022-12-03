"""5. feladat

Adott az alábbi 2 lista Az egyikben személyek nevét tároljuk, a másikban azonos pozíción ugyanezek személyek nemét:

szemelyek = ["Ákos", "Béla", "Éva", "Zoli", "Judit"]

nemek = ["férfi", "férfi", "nő", "férfi", "nő"]

Írd ki az utolsó férfi nevét!

A rendelkezésre álló idő 10 perc.

A kódról és a program futásáról is képernyőképet kérek feltölteni."""

szemelyek = ["Ákos", "Béla", "Éva", "Zoli", "Judit"]
nemek = ["férfi", "férfi", "nő", "férfi", "nő"]
i = 0
utolso_ferfi = ""
while i < len(szemelyek) and len(nemek):
    if nemek[i] == "férfi":
        utolso_ferfi = szemelyek[i]
    i += 1
print(f"Az utolsó férfi: {utolso_ferfi}")


i = len(nemek)-1
while (i >= 0 and nemek[i] != "férfi"):
    i -= 1
if i >= 0:
    print(szemelyek[i])
else:
    print("Nincs férfi")


i = -1
print(i > -len(nemek) and nemek[-1])
while nemek[i] != "férfi":
    i -= 1
print(szemelyek[i])
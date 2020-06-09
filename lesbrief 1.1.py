kleuren = {"broccoli": "groen", "framboos": "rood", "aardbei": "rood", "mango": "geel", "manderijn": "oranje"}
print(kleuren)
print(" ")
kleuren["kiwi"] = "groen"
print("kiwi : groen is toegevoegd.")
print(kleuren)
print(" ")

del kleuren["broccoli"] #broccoli is niet lekker :(
print("broccoli : groen is verwijderd want het is geen fruit soort.")
print(kleuren)
print(" ")

for key, value in kleuren.items():
    print("Alles")
    print(key, value)
print(" ")

inputfruit = input("Noem een fruit soort: ")

if inputfruit in kleuren:
    print(kleuren[inputfruit])
    
d1 = {"sinaasappel": "oranje"}
d2 = {"appel": "rood"}
d3 = {"banaan": "geel"}
d4 = {}
d4.update(d1)
d4.update(d2)
d4.update(d3)
print (d4)

kwadraten = {}
hoevaak = int(input("Tot welk getal wil je de kwadraat weten: "))
hoevaak += 1
for getal in range(hoevaak):
    kwadraten[getal] = getal*getal
    
print (kwadraten)
    
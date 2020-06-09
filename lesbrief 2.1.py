# oefening functies aanroepen
def hallo():
    for i in range(10):
        print("hallo allemaal")
    
def tafel_van_5():
    for t in range(11):
        print(5*t)

hallo()
tafel_van_5()

# oefening parameters
def hello(n):
    for y in range(n):
        print("hello")
print("4 keer hello:")
hello(4)
print("3 keer hello:")
hello(3)
print("8 keer hello:")
hello(8)

def woord(n, woord):
    for i in range(n):
        print(woord)

print("4 keer hallo")
woord(4, "hallo")
print (" ")
print("4 keer blij")
woord(8, "blij")
print (" ")
print("2 keer boos")
woord(2, "boos")

def kerstboom(leuk_woord, aantal):
    for letter in leuk_woord:
        aantal += 1
        print(aantal*letter)
aantal = 0
kerstboom("sofie", aantal)

#oefeningen return
def max_van_3():
    getal1 = int(input("Geef een getal: "))
    getal2 = int(input("Geef nog een getal: "))
    getal3 = int(input("Geef nog een getal: "))
    if getal1 > getal2 and getal1 > getal3:
        grootste_getal = getal1
    elif getal2 > getal1 and getal2 > getal3:
        grootste_getal = getal2
    elif getal3 > getal1 and getal3 > getal2:
        grootste_getal = getal3
    return (grootste_getal)
    
print(max_van_3())

def reverse_string():
    string = input("Geef een woord: ")
    lengte_string = len(string)
    letters = " "
    for i in string:
        letters = i + letters
    return letters
    
print(reverse_string())

def is_priemgetal():
    priemgetallen = []
    priem = int(input("Geef een getal en ik ga kijken of het een priemgetal is: "))
    ja_of_nee = "gadoor"
    teller = 2
    while ja_of_nee == "gadoor":
        if priem == 1:
            ja_of_nee = "stop"
            conclusie = (False)
        elif priem % teller != 0:
            teller += 1
        elif priem == teller:
            conclusie = (True)
            ja_of_nee = "stop"
        else:
            ja_of_nee = "stop"
            conclusie = (False)
    return (conclusie)
print(is_priemgetal())
    
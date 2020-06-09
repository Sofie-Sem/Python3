def print_menu(naam):
    #hier komt het menu in te staat
    pass

def main():
    #Dit is de main van het programma dus waar alle andere functies worden aan geroepen.
    doorgaan = True
    contacten = {"Piet": 12345678, "Willie": 87654321, "Jantje": 23456789}#dit zijn even random nummers ik voeg later echte namen en nummers toe 
    naam = input("Hoe heet je: ")
    while doorgaan:
        #in de loop gaat alles gebeuren
        print_menu(naam)
        keuze = input("Wat is je keuze geworden: ")

def contact_toevoegen():
    #Hier komt de code voor als je er voor kiest om een contact toe te voegen
    pass
    
def lijst_van_contacten():
    #Hier komt de code voor als je er voor kiest om al je contacten en hoeveel je er hebt te bekijken
    pass
def toon_contacten():
    #voor het laten zien van al je contacten
    pass
def aantal_contacten():
    #voor het kijken naar hoeveel contacten je hebt
    pass

def contact_verwijderen():
    #Hier komt de code voor als je er voor kiest om een contact te verwijderen
    pass
    
def contact_aanpassen():
    #Hier komt de code voor als je er voor kiest om een contact aan te passen
    
def contacten_opslaan():
    #Hier komt de code voor als je er voor kiest om een contact op te slaan
    pass
    
main()
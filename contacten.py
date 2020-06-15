def print_menu(naam):
    #Hier komt het menu in te staat.
    print("Welkom " + naam + ", hier kun je je contacten aanpassen/opslaan/bekijken/aanmaken. \n\nVoor aanpassen kies 'a'\nVoor opslaan kies 'o'\nVoor het bekijken van al je contacten kies 'b'\nVoor het aanmaken van contacten kies 'n' \nAls je er geen zin meer in hebt kies dan 'q'\n")

def main():
    #Dit is de main van het programma dus waar alle andere functies worden aan geroepen.
    doorgaan = True
    contacten = {"Piet": 12345678, "Willie": 87654321, "Jantje": 23456789}#dit zijn even random nummers ik voeg later echte namen en nummers toe. 
    naam = input("Hoe heet je: ")
    while doorgaan:
        #In de loop gaat alles gebeuren.
        print_menu(naam)
        keuze = input("Wat is je keuze geworden (a/o/b/n/q): ")
        if keuze == "a":
            contact_aanpassen(contacten)
            
        elif keuze == "o":
            contacten_opslaan(contacten)
            
        elif keuze == "b":
            bekijk_contacten(contacten)
            
        elif keuze == "n":
            contacten_toevoegen(contacten)
            
        elif keuze == "q":
            doorgaan = False
             
        else:
            print("Je hebt iets verkeerts getypt probeer het nog een keer, ik laat je de mogelijkheden nog een keer zien.")

def contact_toevoegen(contacten):
    #Hier komt de code voor als je er voor kiest om een contact toe te voegen.
    print (contacten)
    
def bekijk_contacten(contacten):
    #Hier komt de code voor als je er voor kiest om al je contacten en hoeveel je er hebt te bekijken.
    print (contacten)
            
def toon_aantal_contacten(contacten):
    #Voor het laten zien van al je contacten.
    print (contacten)
            
def aantal_contacten(contacten):
    #Voor het kijken naar hoeveel contacten je hebt.
    print (contacten)

def contact_verwijderen(contacten):
    #Hier komt de code voor als je er voor kiest om een contact te verwijderen
    print (contacten)
    
def contact_aanpassen(contacten):
    #Hier komt de code voor als je er voor kiest om een contact aan te passen
    print (contacten)
            
    
def contacten_opslaan(contacten):
    #Hier komt de code voor als je er voor kiest om een contact op te slaan
    print (contacten)
    
main()#Dit roept de eerste functie aan

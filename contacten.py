def print_menu():
    #Hier komt het menu in te staat.
    print(" ")
    print("-----------------------------------------------\nVoor aanpassen kies 'a'\nVoor opslaan kies 'o'\nVoor het bekijken van al je contacten kies 'b'\nVoor het aanmaken van contacten kies 'n' \nVoor het verwijderen van een contact kies 'v' \nAls je er geen zin meer in hebt kies dan 'q'\n-----------------------------------------------\n")
    
def main():
    #Dit is de main van het programma dus waar alle andere functies worden aan geroepen.
    doorgaan = True
    contacten = {"Piet": 12345678, "Willie": 87654321, "Jantje": 23456789}#dit zijn even random nummers ik voeg later echte namen en nummers toe. 
    naam = input("Hoe heet je: ")
    print("Welkom " + naam + ", hier kun je je contacten aanpassen/opslaan/bekijken/aanmaken.")
    while doorgaan:
        #In de loop gaat alles gebeuren.
        print_menu()
        keuze = input("Wat is je keuze geworden (a/o/b/n/v/q): ")
        
        if keuze == "a": #Dit werkt!
            contact_aanpassen(contacten)
            klik_enter()
            
        elif keuze == "o": #Dit werkt!
            contacten_opslaan(contacten, naam)
            klik_enter()
            
        elif keuze == "b": #Dit werkt! 
            toon_contacten(contacten)
            aantal_contacten(contacten)
            klik_enter()
            
        elif keuze == "n": #Dit werkt!
            contacten_toevoegen(contacten)
            klik_enter()
            
        elif keuze == "v": # Dit werkt!
            contact_verwijderen(contacten)
            klik_enter()
            
        elif keuze == "q": #Dit werkt
            print("Doei!  :)")
            doorgaan = False
             
        else:
            print("Je hebt iets verkeerts getypt probeer het nog een keer, ik laat je de mogelijkheden nog een keer zien.")


#Alle functies
def contact_aanpassen(contacten):
    #Hier komt de code voor als je er voor kiest om een contact aan te passen
    doorgaan_aanpassen = True
    while doorgaan_aanpassen:
        naam_contact_aanpassen = input("Hoe heet het persoon waarvan je de contacteninfo wilt aanpassen: ")
        if naam_contact_aanpassen in contacten:
            wat_aanpassen = input("Wil je het nummer of de naam aanpassen (naam/nummer): ")
            if wat_aanpassen == "nummer":
                nieuw_nummer = input("Wat wordt het nieuwe nummer: ")
                contacten[naam_contact_aanpassen] = nieuw_nummer
                doorgaan_aanpassen = False
                print("Het nummer van " + naam_contact_aanpassen + " is veranderd naar " + nieuw_nummer)
            elif wat_aanpassen == "naam":
                nieuwe_naam = input("Wat word de nieuwe naam voor " + naam_contact_aanpassen + ": ")
                oud_nummer = contacten[naam_contact_aanpassen]
                del contacten[naam_contact_aanpassen]
                contacten[nieuwe_naam] = oud_nummer
                doorgaan_aanpassen = False
                print(naam_contact_aanpassen + " is veranderd in " + nieuwe_naam)
            else:
                print("Je hebt iets verkeerd getypet voer opnieuw de naam in.")
        
        else:
            print("Dit contact bestaat niet, voer een nieuwe naam in.")
        

def contacten_toevoegen(contacten):
    #Hier komt de code voor als je er voor kiest om een contact toetevoegen.
    naam_nieuw_contact = input("Hoe heet het persoon die je wilt toevoegen: ")
    
    if naam_nieuw_contact in contacten:
        naam_nieuw_contact = input("Je hebt al iemand die " + naam_nieuw_contact + " heet, je kan niet iemands naam er 2 keer in hebben staan geef een nieuwe naam: ")
    nummer_nieuw_contact = input("Wat is het nummer van " + naam_nieuw_contact + ": ")
    contacten[naam_nieuw_contact] = nummer_nieuw_contact
    print(naam_nieuw_contact + " : " + nummer_nieuw_contact + " | is toegevoegd aan je contactenlijst.")

def contact_verwijderen(contacten):
    #Hier komt de code voor als je er voor kiest om een contact te verwijderen
    print("Dit zijn al je contacten op dit moment: ")
    toon_contacten(contacten)
    doorgaan2 = True
    while doorgaan2:
        verwijder_contact_naam = input("\nHoe heet het persoon waarvan je het nummer wilt verwijderen, als je niemand wilt verwijderen type 'niemand': ")
        if verwijder_contact_naam in contacten:
            del contacten[verwijder_contact_naam]
            doorgaan2 = False
            print("Je contacten lijst is aangepast.")
        elif verwijder_contact_naam == 'niemand':
            print("Hier is het menu weer.")
            doorgaan2 = False
        else:
            print("De naam die je hebt opgegeven komt niet voor in je contactenlijst voor een nieuwe naam in.")
  
def toon_contacten(contacten):
    #Voor het laten zien van al je contacten.
    for naam, nummer in contacten.items():
        print(naam, ": ", nummer)

def aantal_contacten(contacten):
    #Voor het kijken naar hoeveel contacten je hebt.
    aantal = 0
    for i in contacten.items():
        aantal += 1
    print("Je hebt "+ str(aantal) + " contacten.")
    
def contacten_opslaan(contacten, naam):
    #Hier komt de code voor als je er voor kiest om een contact op te slaan
    naam_bestand = input("hoe wil je je bestand gaan noemen: ")
    je_contacten = open(naam_bestand + ".txt", "w")
    je_contacten.writelines("Contacten van " + naam)
    je_contacten.close()
    for naam_contacten, nummer in contacten.items():
        je_contacten = open(naam_bestand + ".txt", "a+")
        je_contacten.writelines("\n" + str(naam_contacten) + ": " + str(nummer))
        je_contacten.close()
    print("Er is een bestand met de naam " + naam_bestand +".txt voor je aangemaakt.")
    
def klik_enter():
    input("\n-----------------------------------------------\nKlik op enter om verder te gaan ")

    
main()#Dit roept de eerste functie aan

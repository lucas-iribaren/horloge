import time

def afficher_heure(duree): #Comment l'heure va s'afficher
    heure_format = "{:02d}:{:02d}:{:02d}".format(duree[0], duree[1], duree[2]) 
    print(heure_format)

#Mes input
def regler_heure():
    heures = int(input("Entrez l'heure : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    return heures, minutes, secondes #Renvoi l'heure initialisée
def regler_alarme():
    alarme_heures= int(input("Entrez l'heure de l'alarme : "))
    alarme_minutes= int(input("Entrez les minutes de votre alarme : "))
    alarme_secondes= 00
    return alarme_heures,alarme_minutes,alarme_secondes #Revoi à quel heure l'alarme va sonner

def main():
    temps = regler_heure()
    heure_alarme = regler_alarme()


    while True: #Boucle infini
        afficher_heure(temps) #On insère les données de temps dans le format
        time.sleep(1) #Temps d'actualisation
        temps = (temps[0], temps[1], temps[2] + 1) # <-- +1 à mes secondes à chaque temps d'actualisation

        if temps[2] == 60: #Si mes secondes sont à 60 
            temps = (temps[0], temps[1] + 1, 0) #Alors ajoute 1 au minutes et mes secondes reviennent à 0

        if temps[1] == 60:#Si mes minutes sont à 60
            temps = (temps[0] + 1, 0, 0)#Alors ajoute 1 au heures et mes minutes et secondes reviennent à 0
        
        if temps[0] == 24:#Si mes heures sont à 24
            temps = (0, temps[1], temps[2])#Alors mes heures reviennent à 0

        if temps == heure_alarme : #Si mon temps est égale à l'heure de mon alarme
            print("C'est l'heure !!!") #Print



main()
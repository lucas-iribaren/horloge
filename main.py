import time
import keyboard

def afficher_heure(heure):
    heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format)

def regler_heure():
    heures = int(input("Entrez l'heure : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    return heures, minutes, secondes


def regler_alarme():
    alarme_heures= int(input("Entrez l'heure de l'alarme : "))
    alarme_minutes= int(input("Entrez les minutes de votre alarme : "))
    alarme_secondes= 00
    return alarme_heures,alarme_minutes,alarme_secondes

def main():
    heure_a_afficher = regler_heure()
    heure_alarme = regler_alarme()


    while True:
        afficher_heure(heure_a_afficher)
        time.sleep(1)

        heure_a_afficher = (heure_a_afficher[0], heure_a_afficher[1], heure_a_afficher[2] + 1)

        if heure_a_afficher[2] == 60:
            heure_a_afficher = (heure_a_afficher[0], heure_a_afficher[1] + 1, 0)

        if heure_a_afficher[1] == 60:
            heure_a_afficher = (heure_a_afficher[0] + 1, 0, 0)
        
        if heure_a_afficher[0] == 24:
            heure_a_afficher = (0, heure_a_afficher[1], heure_a_afficher[2])

        if heure_alarme == heure_a_afficher:
            print("C'est l'heure !!!")



main()
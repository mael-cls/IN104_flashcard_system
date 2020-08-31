


import pickle
import random
from datetime import datetime
from datetime import timedelta

class FlashCard() : 
    #     Classe définissant les propriétés d'une flashcard (d'après l'énoncé) :
#        • a title : used to find a specific card to be edited/deleted
#        • top side : represents the question
#        • bottom side : represents the answer
#        • subject : the subject of the deck.
#        • location in the deck : we will use this to know where the card is in the deck.
#        • a flag which lets us know if a given card needs to be reviewed. If a
#        card was answered correctly, we do not need to review it for a given amount
#        of time. When that time passes we need to set this flag to True, meaning
#        that we need to review this card.
#        • the date when the card was last reviewed. This will help us to know 
#        if during a training session the card has to be reviewed or not
    
    def __init__(self, title, topside, bottomside, subject) : 
        
        self.title=title
        self.topside=topside
        self.bottomside=bottomside
        self.subject=subject
        self.location=0
        self.flag= True
        self.date_last_review=datetime.now()
            
        
        
        
        
def save_card(all_card, fichier): #fonction de sauvegarde des cartes 
        
    card_pickle=open(fichier, 'wb')
    pickle.dump(all_card, card_pickle )
    card_pickle.close()
        
def load_card(fichier) : #charge les cartes enregistrées dans le fichier card_pickle
    
    
    pickle_card=open(fichier, 'rb')
    card=pickle.load(pickle_card)
    pickle_card.close
    return(card) 
    
def add_card(all_card, card_info): #ajoute une carte à la liste all_card
        
    new_card=FlashCard(card_info[0], card_info[1],card_info[2],card_info[3])
    all_card.append(new_card)
        
    
def edit_flashcard(card_to_edit, new_info): #permet d'éditer les info d'une carte
    
    card_to_edit.title=new_info[0]
    card_to_edit.topside=new_info[1]
    card_to_edit.bottomside=new_info[2]
    card_to_edit.subject=new_info[3]
    card_to_edit.date_last_review=datetime.date()
    
#Cette partie permet de créer les paquets de cartes, elle n'est ulisée qu'une seule fois pour chaque paquet
 
#Création d'un paquet sur les capitales d'Europe
#save_card([],'capitales_europe')
#all_card=load_card('capitales_europe')
##print(all_card)
#title="Capital"
#topside=["France", "Angleterre","Irelande","Suède","Russie","Pays-Bas","Espagne","Suisse","Grèce","Italie"]
#bottomside=["Paris","Londre","Dublin","Stockholm","Moscou","Amsterdam","Madride","Berne","Athènes","Rome"]
#subject="Pays"
#for i in range (len(topside)) :
#    add_card(all_card, [title, topside[i], bottomside[i], subject])
#    print(all_card[i].date_last_review)
##print(all_card)
#save_card(all_card,'capitales_europe')
#
    
#création d'un paquet sur les capitales d'Asie
#save_card([],'capitales_asie')
#all_card=load_card('capitales_asie')
##print(all_card)
#title="Capital"
#topside=["Japon", "Chine","Turquie","Philippine","Inde","Indonésie","Pakistan","Corée du Sud","Malaisie","Taïlande"]
#bottomside=["Tokyo","Pékin","Ankara","Manille","New Dehli","Jakarta","Islamabad","Séoul","Kuala Lumpur","Bangkok"]
#subject="Pays"
#for i in range (len(topside)) :
#    add_card(all_card, [title, topside[i], bottomside[i], subject])
##    print(all_card[i].date_last_review)
##print(all_card)
#save_card(all_card,'capitales_asie')

#Permet au joueur de choisir le paquet avec lequel jouer
    

print("Choisissez un thème : 1-Les capitales d'Europe 2-Les capitales d'Asie")
choice=int(input("....:"))
while choice!=1 and choice !=2:
    print("Ce thème n'existe pas, recommencez !")
    choice=int(input("....:"))
if choice ==1:
    fichier="capitales_europe"
elif choice == 2 : 
    fichier="capitales_asie"
    
    
# on choisit l'action à réaliser
all_card=load_card(fichier) #charge le paquet choisi
print("Que voulez vous faire : \n1-Jouer\n2-Ajouter une carte \n3-Modifier une carte existente \n4-Supprimer une carte\n5-Quitter le jeu")
option=int(input("....:")) 
while option != 5 :
    if option == 1 :  

   

#Création des catégorie de boites, définissant le delais entre chaque rappels
        nb_box=4
        box_delay=[]
        for i in range(nb_box):
            box_delay.append(i*2)
#print(box_delay)


#Début de la partie concernant le déroulement du jeu

#répartition des cartes en deux paquets, celles à revoir et les autres
        card_to_review=[]
        card_not_review=[]
        for i in all_card :
        
            if (timedelta(minutes=box_delay[i.location])+i.date_last_review < datetime.now() ): #ici le delais choisi entre les revus est en minutes ( peut être défini en jour en changeant "minutes" par "days")
                i.flag=True
                card_to_review.append(i)
            else : 
                i.flag = False
                card_not_review.append(i)
        print(len(card_to_review), "cartes à jouer ")


        random.shuffle(card_to_review) #mélange aléatoire des cartes
#le joueur joue sur les cartes séléctionnées
        score = 0
        for n in range( len(card_to_review) ):
            card_to_review[n].date_last_review= datetime.now()
            print("\n ",card_to_review[n].title, card_to_review[n].topside)
            r=input("Réponse: ")
            if r != card_to_review[n].bottomside :
                card_to_review[n].location = 0
                print("Mauvaise réponse, la réponse était " , card_to_review[n].bottomside)
            elif card_to_review[n].location <  (len(box_delay)-1) :
                card_to_review[n].location +=1
                print("Bonne réponse")
                score+=1
                card_to_review[n].flag=False
            else :
                card_to_review[n].flag=False
                print("Bonne réponse")
                score+=1
    

    
        print("\nPartie terminée")
        print ("Votre score est :", score, "sur", len(card_to_review))
    #fin de partie, enregistrement des cartes
        all_card=card_to_review+card_not_review
    
    
    elif option ==2 :   #option pour ajouter une nouvelle carte
        card_info=[""]*4
        card_info[0]=input("Titre ? ")
        card_info[1]=input("Question ? ")
        card_info[2]=input("Réponse ? ")
        card_info[3]=input("Thème ? ")
        add_card(all_card, card_info)
    
    elif option ==3 : # option pour modifier une carte existente
        for i in range(len(all_card)):
            print(i , "-", all_card[i].topside)
        n_card=int(input("Numéro de la carte à modifier :"))
        while n_card not in range(len(all_card)) :
            print("Cette carte n'existe pas, recommencez !")
            n_card=int(input("Numéro de la carte à modifier :"))
        all_card[n_card].title=input("Titre ? ")
        all_card[n_card].topside=input("Question ? ")
        all_card[n_card].bottomside=input("Réponse ? ")
        all_card[n_card].subject=input("Thème ? ")
    
    
    elif option ==4 : #option pour supprimer une carte du paquet
        for i in range(len(all_card)):
            print(i , "-", all_card[i].topside)
        n_card=int(input("Numéro de la carte à supprimer : "))
        while n_card not in range(len(all_card)) :
            print("Cette carte n'existe pas, recommencez !")
            n_card=int(input("Numéro de la carte à supprimer : "))
        if n_card<len(all_card) :
            all_card.pop(n_card)
    print("Que voulez vous faire : \n1-Jouer\n2-Ajouter une carte \n3-Modifier une carte existente \n4-Supprimer une carte\n5-Quitter le jeu")
    option=int(input("....:"))     
        
    save_card(all_card, fichier)   # on sauvegarde toutes les modifications     
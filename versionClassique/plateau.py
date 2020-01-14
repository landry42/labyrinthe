# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""
import random
from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """

    # Liste des tresors
    ListeTresors=[]
    for i in range(12):         #Il y a 12 tresors
        ListeTresors.append(i)  
    ListeTresors=random.sample(ListeTresors, len(ListeTresors))
    

    matrice=Matrice(7,7,0)
    
    # 1ere ligne fixe
    matrice[0][0]=Carte(True, False, False, True, 0, [])        #On ne met pas de tresor sur les coins
    matrice[0][2]=Carte(True, False, False, False, 0, [])
    mettreTresor(matrice[0][2], ListeTresors[0])
    matrice[0][4]=Carte(True, False, False, False, 0, [])
    mettreTresor(matrice[0][4], ListeTresors[1])
    matrice[0][6]=Carte(True, True, False, False, 0, [])  #On ne met pas de tresor sur les coins
    


    # 2eme ligne fixe
    matrice[2][0]=Carte(False, False, False, True, 0, [])
    mettreTresor(matrice[2][0], ListeTresors[2])
    matrice[2][2]=Carte(False, False, False, True, 0, [])
    mettreTresor(matrice[2][2], ListeTresors[3])
    matrice[2][4]=Carte(True, False, False, False, 0, [])
    mettreTresor(matrice[2][4], ListeTresors[4])
    matrice[2][6]=Carte(False, True, False, False, 0, [])
    mettreTresor(matrice[2][6], ListeTresors[5])
    


    # 3eme ligne fixe
    matrice[4][0]=Carte(False, False, False, True, 0, [])
    mettreTresor(matrice[4][0], ListeTresors[6])
    matrice[4][2]=Carte(False, False, True, False, 0, [])
    mettreTresor(matrice[4][2], ListeTresors[7])
    matrice[4][4]=Carte(False, True, False, False, 0, [])
    mettreTresor(matrice[4][4], ListeTresors[8])
    matrice[4][6]=Carte(False, True, False, False, 0, [])
    mettreTresor(matrice[4][6], ListeTresors[9])


    # 4eme et derniere ligne fixe
    matrice[6][0]=Carte(False, False, True, True, 0, [])      #On ne met pas de tresor sur les coins
    matrice[6][2]=Carte(False, False, True, False, 0, [])
    mettreTresor(matrice[6][2], ListeTresors[10])
    matrice[6][4]=Carte(False, False, True, False, 0, [])
    mettreTresor(matrice[6][4], ListeTresors[11])
    matrice[6][6]=Carte(False, True, True, False, 0, [])      #On ne met pas de tresor sur les coins


    #cartes amovibles
    cartesAmovibles=creerCartesAmovibles(17, nbTresors)   #17 car nous avons deja placer 16 tresors

    listeAmovibles=cartesAmovibles[0]
    carteDeTrop=cartesAmovibles[1]

    matricePourPlateau=[]
    for miniListe in matrice:
        for element in miniListe:
            matricePourPlateau.append(element)

    cpt=0
    for i in range(len(matricePourPlateau)):
        if matricePourPlateau[i]==0
            matricePourPlateau[i]=listeAmovibles[cpt]
            cpt+=1

    # Nb joueurs
    if nbJoueurs==1:
        poserPion(matricePourPlateau[0], 1)
    if nbJoueurs==2:
        poserPion(matricePourPlateau[0], 1)
        poserPion(matricePourPlateau[6], 2)
    if nbJoueurs==3:
        poserPion(matricePourPlateau[0], 1)
        poserPion(matricePourPlateau[6], 2)
        poserPion(matricePourPlateau[42], 3)
    if nbJoueurs==4:
        poserPion(matricePourPlateau[0], 1)
        poserPion(matricePourPlateau[6], 2)
        poserPion(matricePourPlateau[42], 3)
        poserPion(matricePourPlateau[48], 4)

    """
    cpt=0
    matrice=[]
    miniListe=[]

    for nb in matricePourPlateau:
        if cpt!=7:
            miniListe.append(nb)
            cpt+=1
        else:
            matrice.append(miniListe)
            miniListe=[]
            cpt=0
    """
    return matricePourPlateau,CarteDeTrop

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    listeCartes=[]

    #Nb coins a faire:
    cptCoins = 16    
    
    #Nb jonctions a faire:
    cptJonctions = 6

    #nb ToutDroit a faire:
    cptToutDroit = 12

    while cptCoins>0:
        for i in range(cptCoins):
            carte = Carte(False, False, True, True, 0, [])
            carte=tourneAleatoire(carte)
            listeCartes.append(carte)
            cptCoins-=1

    while cptJonctions>0:
        for i in range(cptJonctions):
            carte = Carte(False, False, False, True, 0, [])
            carte=tourneAleatoire(carte)
            listeCartes.append(carte)
            cptJonctions-=1

    while cptToutDroit>0:
        for i in range(cptDroit):
            carte = Carte(True, False, True, False, 0, [])
            carte=tourneAleatoire(carte)
            listeCartes.append(carte)
            cptToutDroit-=1


    ListeCartes=random.sample(ListeCartes, len(ListeCartes))
    
    alea=None
    for i in range(len(ListeCartes)):
        alea=random.randint(0,1)
        if alea==1:
            mettreTresor(ListeCartes[i], i)
    
    return ListeCartes

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    res=getVal(plateau,lig,col)
    if numTresor=res["tresor"]:
        Booleen=True
        prendreTresor(res)
    else:
        Booleen=False
    return Booleen

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    res=None
    lig=0
    col=0
    for carte in plateau[0]:
        if carte['tresor']==numTresor:
            res=(lig,col)
        else:
            lig+=1
            col+=1
    return res

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    res=None
    lig=0
    col=0
    for carte in plateau[0]:
        if numJoueur in carte['pions']:
            res=(lig,col)
        else:
            lig+=1
            col+=1
    return res

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(getVal(plateau,lin,col), numJoueur)    

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(getVal(plateau,lin,col), numJoueur)


def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    pass

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass

# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *



def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    res = {}
    listeJoueur = []
    listeJoueur = ListeJoueurs(nomsJoueurs)
    initAleatoireJoueurCourant(listeJoueur)
    distribuerTresors(listeJoueur, nbTresors, nbTresorsMax)
    res['participants'] = listeJoueur
    res['plateau'] = Plateau(len(nomsJoueurs), nbTresors)
    res['phase'] = 1
    if len(res['participants'])>4:
        return 'Erreur : Le jeu du labyrinthe ne peut être joué qu\'à 4 !'
    return res

#laby=Labyrinthe(["joueur1","joueur2"],24,0)


def liste_to_liste_de_liste_labyrinthe(labyrinthe):
    """
    transforme une liste en liste de liste
    """
    mat=[]
    miniListe=[]
    for element in labyrinthe['plateau'][0]:
        miniListe.append(element.copy())
        if len(miniListe)==7:
            mat.append(miniListe)
            miniListe=[]
    return mat

def liste_de_liste_to_liste(liste):
    """
    transforme une liste de liste en liste
    """
    res=[]
    for l in liste:
        for i in l:
            res.append(i)
    return res 

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return liste_to_liste_de_liste_labyrinthe(labyrinthe)

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return len(labyrinthe["participants"])

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return labyrinthe["participants"][0]["nom"]

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return labyrinthe["participants"][0]["numJoueur"]

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """
    return labyrinthe["phase"]


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    if getPhase(labyrinthe) == 1:
        labyrinthe["phase"] = 2
    elif getPhase(labyrinthe) == 2:
        labyrinthe["phase"] = 1

def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """
    cpt = 0
    for carte in labyrinthe["plateau"][0]:
        if carte["tresor"] != 0:
            cpt += 1
    return cpt

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py
    """
    liste_des_joueurs = []
    for joueur in labyrinthe["participants"]:
        liste_des_joueurs.append(joueur)
    return liste_des_joueurs

def enleverTresor(labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe.
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    mat=liste_to_liste_de_liste_labyrinthe(labyrinthe)
    prendreTresorPlateau(mat,lin,col,numTresor)


def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    mat=liste_to_liste_de_liste_labyrinthe(labyrinthe)
    prendrePionPlateau(mat,lin,col,labyrinthe["participants"][0]["numJoueur"])

def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    mat=liste_to_liste_de_liste_labyrinthe(labyrinthe)
    poserPionPlateau(mat,lin,col,labyrinthe["participants"][0]["numJoueur"])

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer
    """
    return labyrinthe["plateau"][1]

def coupInterdit(labyrinthe,direction,rangee):
    """
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    res=False
    DirectionPossible = ['N','S','E','O']
    RangeePossible = [1,3,5]
    if direction not in DirectionPossible or rangee not in RangeePossible:
        res=True
    return res

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais met à jour le labyrinthe
    """
    mat=liste_to_liste_de_liste_labyrinthe(labyrinthe)

    if coupInterdit(labyrinthe, direction, rangee) == False:
        if direction == 'O':
            labyrinthe["plateau"]=[liste_de_liste_to_liste(mat),decalageLigneADroite(mat, rangee, labyrinthe["plateau"][1])]
        elif direction == 'E':
            labyrinthe["plateau"] = [liste_de_liste_to_liste(mat),decalageLigneAGauche(mat, rangee, labyrinthe["plateau"][1])]

        elif direction == 'S':
            labyrinthe["plateau"] = [liste_de_liste_to_liste(mat),decalageColonneEnHaut(mat, rangee, labyrinthe["plateau"][1])]

        elif direction=='N':
            labyrinthe["plateau"] = [liste_de_liste_to_liste(mat),decalageColonneEnBas(mat, rangee, labyrinthe["plateau"][1])]


def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    if sens == 'H':
        tournerHoraire(labyrinthe["plateau"][1])
    elif sens == 'A':
        tournerAntiHoraire(labyrinthe["plateau"][1])

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit chercher le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return labyrinthe["participants"][0]["tresor"][0]

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré
    resultat: les coordonnées du trésor à chercher ou None si celui-ci
              n'est pas sur le plateau
    """
    return getCoordonneesTresor(labyrinthe['plateau'][0], getTresorCourant(labyrinthe))


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré
    resultat: les coordonnées du joueur courant ou None si celui-ci
              n'est pas sur le plateau
    """
    return getCoordonneesJoueur(labyrinthe['plateau'][0], getNumJoueurCourant(labyrinthe))

def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5
                        => insérer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    res = 0
    if action == 'T':
        tournerHoraire(labyrinthe["plateau"][1])
    elif (action == 'N' or action == 'E' or  action == 'S' or action == 'O') and (rangee == 1 or rangee == 3 or rangee == 5):
        jouerCarte(labyrinthe, action, rangee)
        changerPhase(labyrinthe)
        res = 1
    elif not(action == 'N' or action == 'E' or  action == 'S' or action == 'O') and not(rangee == 1 or rangee == 3 or rangee == 5):
        res=  2
    elif type(action)==int and type(rangee)==int:
        res = 3
    else:
        res= 4
    return res

def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    x,y = getCoordonneesJoueurCourant(labyrinthe)
    res = accessibleDist(labyrinthe['plateau'][0], x, y , ligA, colA)
    return res


def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    mat=liste_to_liste_de_liste_labyrinthe(labyrinthe)

    joueurCourant = getJoueurCourant(labyrinthe["participants"])
    joueur_coords = getCoordonneesJoueurCourant(labyrinthe)
    tresor_coords = getCoordonneesTresorCourant(labyrinthe)
    res= 0
    if joueur_coords == tresor_coords:
        prendreTresorPlateau(mat, tresor_coords[1], tresor_coords[0], joueurCourant['tresor'][0])
        joueurCourant["tresor"].pop(0)

        changerJoueurCourant(labyrinthe["participants"])
        changerPhase(labyrinthe)
        res+=1
        if len(joueurCourant["tresor"]) == 0:
            res+=1
    else:
        changerJoueurCourant(labyrinthe["participants"])
        changerPhase(labyrinthe)
    return res

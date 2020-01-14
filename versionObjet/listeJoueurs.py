# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des Joueurs. 
"""
import random
from joueur import *

class ListeJoueurs(object):
    def __init__(self, nomsJoueurs):
        """
        constructeur
        """
        res=[]
        for nom in nomsJoueurs:
            res.append(Joueur(nom))
        for i in range(len(res)):
            res[i].setNumJoueur(i+1)
        self._listeJoueurs = res

    def getListeJoueurs(self):
        return self._listeJoueurs

    def ajouterJoueur(self, Joueur):
        """
        ajoute un nouveau Joueur à la fin de la liste
        paramètres: Joueurs un liste de Joueurs
                    Joueur le Joueur à ajouter
        cette fonction ne retourne rien mais modifie la liste des Joueurs
        """
        self._listeJoueurs.append(Joueur)
        self._listeJoueurs[len(self._listeJoueurs)-1].setNumJoueur(len(self._listeJoueurs))

    def initAleatoireJoueurCourant(self):
        """
        tire au sort le Joueur courant
        paramètre: _listeJoueurs un liste de _listeJoueurs
        cette fonction ne retourne rien mais modifie la liste des _listeJoueurs
        """
        courant= random.randint(0, len(self._listeJoueurs)-1)
        stock = self._listeJoueurs.pop(courant)
        self._listeJoueurs.insert(0,stock)
        for i in range(len(self._listeJoueurs)):
            self._listeJoueurs[i].setNumJoueur(i+1)
    
    def distribuerTresors(self,nbTresors=24, nbTresorMax=0):
        """
        distribue de manière aléatoire des trésors entre les _listeJoueurs.
        paramètres: _listeJoueurs la liste des _listeJoueurs
                    nbTresors le nombre total de trésors à distribuer (on rappelle 
                            que les trésors sont des entiers de 1 à nbTresors)
                    nbTresorsMax un entier fixant le nombre maximum de trésor 
                                qu'un Joueur aura après la distribution
                                si ce paramètre vaut 0 on distribue le maximum
                                de trésor possible  
        cette fonction ne retourne rien mais modifie la liste des _listeJoueurs
        """
        tresor = []
        if nbTresorMax == 0:
            nbTresorMax = nbTresors // len(self._listeJoueurs)
        for i in range(1,nbTresors+1):
            tresor.append(i)
        random.shuffle(tresor)
        for Joueur in self._listeJoueurs:
            for i in range(nbTresorMax):
                Joueur.addTresor(tresor.pop(0))

    def changerJoueurCourant(self):
        """
        passe au Joueur suivant (change le Joueur courant donc)
        paramètres: _listeJoueurs la liste des _listeJoueurs
        cette fonction ne retourne rien mais modifie la liste des _listeJoueurs
        """   
        
        j=self._listeJoueurs.pop(0)
        self._listeJoueurs.append(j)

    def getNb_listeJoueurs(self):
        """
        retourne le nombre de _listeJoueurs participant à la partie
        paramètre: _listeJoueurs la liste des _listeJoueurs
        résultat: le nombre de _listeJoueurs de la partie
        """
        return len(self._listeJoueurs)

    def getJoueurCourant(self):
        """
        retourne le Joueur courant
        paramètre: _listeJoueurs la liste des _listeJoueurs
        résultat: le Joueur courant
        """
        return self._listeJoueurs[0]

    def JoueurCourantTrouveTresor(self):
        """
        Met à jour le Joueur courant lorsqu'il a trouvé un trésor
        c-à-d enlève le trésor de sa liste de trésors à trouver
        paramètre: _listeJoueurs la liste des _listeJoueurs
        cette fonction ne retourne rien mais modifie la liste des _listeJoueurs
        """
        self._listeJoueurs[0].tresorTrouve()

    def nbTresorsRestantsJoueur(self,numJoueur):
        """
        retourne le nombre de trésors restant pour le Joueur dont le numéro 
        est donné en paramètre
        paramètres: _listeJoueurs la liste des _listeJoueurs
                    numJoueur le numéro du Joueur
        résultat: le nombre de trésors que Joueur numJoueur doit encore trouver
        """
        return self._listeJoueurs[self.getIndex(numJoueur)].getNbTresorsRestants()

    def numJoueurCourant(self):
        """
        retourne le numéro du Joueur courant
        paramètre: _listeJoueurs la liste des _listeJoueurs
        résultat: le numéro du Joueur courant
        """
        return self._listeJoueurs[0].getNumJoueur()
    def nomJoueurCourant(self):
        """
        retourne le nom du Joueur courant
        paramètre: _listeJoueurs la liste des _listeJoueurs
        résultat: le nom du Joueur courant
        """
        return self._listeJoueurs[0].getNom()

    def nomJoueur(self,numJoueur):
        """
        retourne le nom du Joueur dont le numero est donné en paramètre
        paramètres: _listeJoueurs la liste des _listeJoueurs
                    numJoueur le numéro du Joueur    
        résultat: le nom du Joueur numJoueur
        """
        return self._listeJoueurs[self.getIndex(numJoueur)].getNom()

    def prochainTresorJoueur(self,numJoueur):
        """
        retourne le trésor courant du Joueur dont le numero est donné en paramètre
        paramètres: _listeJoueurs la liste des _listeJoueurs
                    numJoueur le numéro du Joueur    
        résultat: le prochain trésor du Joueur numJoueur (un entier)
        """
        return self._listeJoueurs[self.getIndex(numJoueur)].prochainTresor()

    def tresorCourant(self):
        """
        retourne le trésor courant du Joueur courant
        paramètre: _listeJoueurs la liste des _listeJoueurs 
        résultat: le prochain trésor du Joueur courant (un entier)
        """
        return self._listeJoueurs[0].prochainTresor()

    def JoueurCourantAFini(self):
        """
        indique si le Joueur courant a gagné
        paramètre: _listeJoueurs la liste des _listeJoueurs 
        résultat: un booleen indiquant si le Joueur courant a fini
        """
        res=False
        if len(self._listeJoueurs[0]["tresor"]) == 0:
            res = True
        return res
    
    def getIndex(self,numJoueur):
        """
        retourne l'index du joueur dans la liste en fonction de son numéro.
        S'il est inexistant, retourne None
        """
        i = 0
        while i < len(self._listeJoueurs) and self._listeJoueurs[i].getNumJoueur() != numJoueur:
            i += 1
        if i == len(self._listeJoueurs):
            i = None
        return i

if __name__=='__main__':
    nomsJoueurs = ["Joueur_1","Joueur_2","Joueur_3"]
    l=ListeJoueurs(nomsJoueurs)
    l.ajouterJoueur(Joueur("Joueur_4"))
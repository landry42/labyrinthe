# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

class ListeJoueurs(object):
    def _init_(self, nomsJoueurs):
        """
        constructeur
        """
        res=[]
        for nom in nomsJoueurs:
            res.append(Joueur(nom))
        for i in range(len(res)):
            res[i].numjoueur = i+1
        self.joueurs = res

    def ajouterJoueur(self, joueur):
        """
        ajoute un nouveau joueur à la fin de la liste
        paramètres: joueurs un liste de joueurs
                    joueur le joueur à ajouter
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        self.joueurs.append(joueur)
        self.joueurs[len(self.joueurs)-1]["numJoueur"] = len(self.joueurs)-1

    def initAleatoireJoueurCourant(self):
        """
        tire au sort le joueur courant
        paramètre: joueurs un liste de joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        courant= random.randint(0, len(self.joueurs)-1)
        stock = self.joueurs.pop(courant)
        self.joueurs.insert(0,stock)
        for i in range(len(self.joueurs)):
            self.joueurs[i]["numJoueur"] = i+1
    
    def distribuerTresors(self,nbTresors=24, nbTresorMax=0):
        """
        distribue de manière aléatoire des trésors entre les joueurs.
        paramètres: joueurs la liste des joueurs
                    nbTresors le nombre total de trésors à distribuer (on rappelle 
                            que les trésors sont des entiers de 1 à nbTresors)
                    nbTresorsMax un entier fixant le nombre maximum de trésor 
                                qu'un joueur aura après la distribution
                                si ce paramètre vaut 0 on distribue le maximum
                                de trésor possible  
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        tresor = []
        if nbTresorMax == 0:
            nbTresorMax = nbTresors // len(self.joueurs)
        for i in range(1,nbTresors+1):
            tresor.append(i)
        random.shuffle(tresor)
        for joueur in self.joueurs:
            for i in range(nbTresorMax):
                joueur["tresor"].append(tresor.pop(0))

    def changerJoueurCourant(self):
        """
        passe au joueur suivant (change le joueur courant donc)
        paramètres: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """   
        
        j=self.joueurs.pop(0)
        self.joueurs.append(j)

    def getNbJoueurs(self):
        """
        retourne le nombre de joueurs participant à la partie
        paramètre: joueurs la liste des joueurs
        résultat: le nombre de joueurs de la partie
        """
        return len(self.joueurs)

    def getJoueurCourant(self):
        """
        retourne le joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le joueur courant
        """
        return self.joueurs[0]

    def joueurCourantTrouveTresor(self):
        """
        Met à jour le joueur courant lorsqu'il a trouvé un trésor
        c-à-d enlève le trésor de sa liste de trésors à trouver
        paramètre: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        tresorTrouve(self.joueurs[0])

    def nbTresorsRestantsJoueur(self,numJoueur):
        """
        retourne le nombre de trésors restant pour le joueur dont le numéro 
        est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur
        résultat: le nombre de trésors que joueur numJoueur doit encore trouver
        """
        return getNbTresorsRestants(self.joueurs[numJoueur -1])

    def numJoueurCourant(self):
        """
        retourne le numéro du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le numéro du joueur courant
        """
        return self.joueurs[0]["numJoueur"]

    def nomJoueurCourant(self):
        """
        retourne le nom du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le nom du joueur courant
        """
        return getNom(self.joueurs[0])

    def nomJoueur(self,numJoueur):
        """
        retourne le nom du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le nom du joueur numJoueur
        """
        return getNom(self.joueurs[numJoueur -1])

    def prochainTresorJoueur(self,numJoueur):
        """
        retourne le trésor courant du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le prochain trésor du joueur numJoueur (un entier)
        """
        return prochainTresor(self.joueurs[numJoueur -1])

    def tresorCourant(self):
        """
        retourne le trésor courant du joueur courant
        paramètre: joueurs la liste des joueurs 
        résultat: le prochain trésor du joueur courant (un entier)
        """
        return prochainTresor(self.joueurs[0])

    def joueurCourantAFini(self):
        """
        indique si le joueur courant a gagné
        paramètre: joueurs la liste des joueurs 
        résultat: un booleen indiquant si le joueur courant a fini
        """
        res=False
        if len(self.joueurs[0]["tresor"]) == 0:
            res = True
        return res

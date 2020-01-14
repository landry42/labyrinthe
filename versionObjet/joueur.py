# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""
class Joueur(object):
    def _init(self,nom):
        """
        constructeur
        """
        self._nom=nom
        self._tresor=[]
        self._numjoueur=0


    def Joueur(self,nom):
        """
        creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
        paramètre: nom une chaine de caractères
        retourne le joueur ainsi créé
        """
        return {'nom':self._nom,'tresor':self._tresor,'numjoueur':self._numjoueur}

    def ajouterTresor(self,tresor):
        """
        ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
        paramètres:
            joueur le joueur à modifier
            tresor un entier strictement positif
        la fonction ne retourne rien mais modifie le joueur
        """
        if tresor not in self._tresor:
            self._tresor.append(tresor)

    def prochainTresor(self):
        """
        retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
        paramètre:
            joueur le joueur
        résultat un entier représentant le trésor ou None
        """
        if getNbTresorsRestants(self) > 0:
            res = self._tresor[0]
        else:
            res = None
        return res 

    def tresorTrouve(self):
        """ 
        enlève le premier trésor à trouver car le joueur l'a trouvé
        paramètre:
            joueur le joueur
        la fonction ne retourne rien mais modifie le joueur
        """
        self._tresor.pop(0)

    def getNbTresorsRestants(self):
        """
        retourne le nombre de trésors qu'il reste à trouver
        paramètre: joueur le joueur
        résultat: le nombre de trésors attribués au joueur
        """
        return len(self._tresor)

    def getNom(self):
        """
        retourne le nom du joueur
        paramètre: joueur le joueur
        résultat: le nom du joueur 
        """
        return self._nom

if __name__=='__main__':
    j1=Joueur("François")
    j1.ajouterTresor(2)
    j1.ajouterTresor(5)
    j1.ajouterTresor(8)
    assert j1.getNom()=="François" and j1.getNbTresorsRestants()==3 and j1.getTresors()==[2,5,8]
    assert j1.getNbTresorsRestants()==3
    j1.tresorTrouve()
    assert j1.prochainTresor()==5
    assert j1.getNom()=="François" and j1.getNbTresorsRestants()==2 and j1.getTresors()==[5,8]
print("---------------\nIt just works !\n--------------
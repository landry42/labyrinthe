# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""
from matrice import *
from carte import *
import random

class plateau(object):
    def __init__(self, nbJoueurs, nbTresors):
        """
        Constructeur
        """
        # Liste des tresors
        ListeTresors=[]
        for i in range(1,13):         #Il y a 12 tresors
            ListeTresors.append(i)  
        random.shuffle(ListeTresors)

        matrice=Matrice(7,7,0)
        
        # 1ere ligne fixe
        matrice.setVal(0,0,Carte(True, False, False, True, 0, [])) #On ne met pas de tresor sur les coins
        matrice.setVal(0,2,Carte(True, False, False, False, ListeTresors[0], []))
        matrice.setVal(0,4,Carte(True, False, False, False, ListeTresors[1], []))
        matrice.setVal(0,6,Carte(True, True, False, False, 0, [])) #On ne met pas de tresor sur les coins

        # 2eme ligne fixe
        matrice.setVal(2,0,Carte(False, False, False, True, ListeTresors[2], []))
        matrice.setVal(2,2,Carte(False, False, False, True, ListeTresors[3], []))
        matrice.setVal(2,4,Carte(True, False, False, False, ListeTresors[4], []))
        matrice.setVal(2,6,Carte(False, True, False, False, ListeTresors[5], []))


        # 3eme ligne fixe
        matrice.setVal(4,0,Carte(False, False, False, True, ListeTresors[6], []))
        matrice.setVal(4,2,Carte(False, False, True, False, ListeTresors[7], []))
        matrice.setVal(4,4,Carte(False, True, False, False, ListeTresors[8], []))
        matrice.setVal(4,6,Carte(False, True, False, False, ListeTresors[9], []))


        # 4eme et derniere ligne fixe
        matrice.setVal(6,0,Carte(False, False, True, True, 0, [])) #On ne met pas de tresor sur les coins
        matrice.setVal(6,2,Carte(False, False, True, False, ListeTresors[10], []))
        matrice.setVal(6,4,Carte(False, False, True, False, ListeTresors[11], []))
        matrice.setVal(6,6,Carte(False, True, True, False, 0, [])) #On ne met pas de tresor sur les coins

        #cartes amovibles
        listeAmovibles=self.creerCartesAmovibles(13, nbTresors)   #13 car nous avons deja placer 12 tresors

        CarteDeTrop=listeAmovibles[-1]
        listeAmovibles.pop()

        matricePourPlateau=[]
        for miniListe in matrice.getMatrice():
            for element in miniListe:
                matricePourPlateau.append(element)

        cpt=0
        for i in range(len(matricePourPlateau)):
            if matricePourPlateau[i]==0:
                matricePourPlateau[i]=listeAmovibles[cpt]
                cpt+=1

            if nbJoueurs==1:
                matricePourPlateau[0].poserPion(1)
            elif nbJoueurs==2:
                matricePourPlateau[0].poserPion(1)
                matricePourPlateau[6].poserPion(2)
            elif nbJoueurs==3:
                matricePourPlateau[0].poserPion(1)
                matricePourPlateau[6].poserPion(2)
                matricePourPlateau[42].poserPion(3)
            else:
                matricePourPlateau[0].poserPion(1)
                matricePourPlateau[6].poserPion(2)
                matricePourPlateau[42].poserPion(3)
                matricePourPlateau[48].poserPion(4)

        self._matricePourPlateau = matricePourPlateau
        self._CarteDeTrop = CarteDeTrop
        print(self._matricePourPlateau,self._CarteDeTrop)

    def creerCartesAmovibles(self,tresorDebut,nbTresors):
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

        #Nb ToutDroit a faire:
        cptToutDroit = 12

        while cptCoins>0:
            for i in range(cptCoins):
                carte = Carte(False, False, True, True, 0, [])
                carte.tourneAleatoire()
                listeCartes.append(carte)
                cptCoins-=1

        while cptJonctions>0:
            for i in range(cptJonctions):
                carte = Carte(False, False, False, True, 0, [])
                carte.tourneAleatoire()
                listeCartes.append(carte)
                cptJonctions-=1

        while cptToutDroit>0:
            for i in range(cptToutDroit):
                carte = Carte(True, False, True, False, 0, [])
                carte.tourneAleatoire()
                listeCartes.append(carte)
                cptToutDroit-=1


        random.shuffle(listeCartes)
        
        #alea=None
        for i in range(tresorDebut,nbTresors+1):
            listeCartes[i].mettreTresor(i)
        
        return listeCartes


    def prendreTresorPlateau(self,lig,col,numTresor):
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
        matrice=[]
        miniListe=[]

        # A CORRIGER
        for element in self._matricePourPlateau.getMatrice():
            miniListe.append(element)
            if len(miniListe)==7:
                matrice.append(miniListe)
                miniListe=[]
        
        # A CORRIGER
        res = self.getVal(lig,col)

        if numTresor==res["tresor"]:
            Booleen=True
            res.prendreTresor()
        else:
            Booleen=False
        return Booleen

    def getCoordonneesTresor(self,numTresor):
        """
        retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
        paramètres: plateau: le plateau considéré
                    numTresor: le numéro du trésor à trouver
        resultat: un couple d'entier donnant les coordonnées du trésor ou None si
                le trésor n'est pas sur le plateau
        """
        matrice=[]
        miniListe=[]
        
        for element in self._matricePourPlateau:
            miniListe.append(element)
            if len(miniListe)==7:
                matrice.append(miniListe)
                miniListe=[]

        res=None
        for lig in range(len(matrice)):
            for carte in range(len(matrice[lig])):
                # A CORRIGER
                if matrice.getTresor(lig,carte)==numTresor:
                    res=(lig,carte)
        return res

    def getCoordonneesJoueur(self,numJoueur):
        """
        retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
        paramètres: plateau: le plateau considéré
                    numJoueur: le numéro du joueur à trouver
        resultat: un couple d'entier donnant les coordonnées du joueur ou None si
                le joueur n'est pas sur le plateau
        """
        matrice=Matrice(0,0)
        miniListe=[]
        
        for element in self._matricePourPlateau:
            miniListe.append(element)
            if len(miniListe)==7:
                # A CORRIGER
                matrice.append(miniListe)
                miniListe=[]

        colonne,ligne= 0,0
        for lig in range(matrice.getNbColonnes()):
            for col in range(matrice.getNbLignes()):
                carte=matrice.getVal(lig,col)
                if carte.possedePion(numJoueur):
                    colonne=lig
                    ligne=col
        return (colonne,ligne)
    #print(getCoordonneesJoueur(Plateau(2,24)[0],2))
    def prendrePionPlateau(self,lin,col,numJoueur):
        """
        prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
        paramètres: plateau:le plateau considéré
                    lin: numéro de la ligne où se trouve le pion
                    col: numéro de la colonne où se trouve le pion
                    numJoueur: le numéro du joueur qui correspond au pion
        Cette fonction ne retourne rien mais elle modifie le plateau
        """
        self.prendrePion(self._matricePourPlateau.getVal(lin,col), numJoueur)    

    def poserPionPlateau(self,lin,col,numJoueur):
        """
        met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
        paramètres: plateau:le plateau considéré
                    lin: numéro de la ligne où se trouve le pion
                    col: numéro de la colonne où se trouve le pion
                    numJoueur: le numéro du joueur qui correspond au pion
        Cette fonction ne retourne rien mais elle modifie le plateau
        """
        self.poserPion(self._matricePourPlateau.getVal(self,lin,col), numJoueur)

    def affichePlateau(matrice):
        afficheMatrice(matrice)

    def accessible(self,ligD,colD,ligA,colA):
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
        if len(plateau)!=7:
            matrice=[]
            miniListe=[]
            for element in plateau:
                miniListe.append(element)
                if len(miniListe)==7:
                    matrice.append(miniListe)
                    miniListe=[]
        res=False
        t=True
        marque=1
        calque=Matrice(getNbLignes(matrice),getNbColonnes(matrice))
        setVal(calque,ligD,colD,marque)
        while t==True:
            t=False
            for i in range(getNbLignes(matrice)):
                for j in range(getNbColonnes(matrice)):
                    if getVal(calque,i,j)!=0:
                        CoordonneesAutours=[(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
                        for (a,b) in CoordonneesAutours:
                            if not a>=getNbLignes(matrice) and not a<0 and not b>=getNbColonnes(matrice) and not b<0:
                                if getVal(calque,a,b)==0:
                                    if (a,b)==(i+1,j):
                                        if passageSud(getVal(matrice,i,j), getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
                                    elif (a,b)==(i,j+1):
                                        if passageEst(getVal(matrice,i,j), getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
                                    elif (a,b)==(i-1,j):
                                        if passageNord(getVal(matrice,i,j),getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
                                    elif (a,b)==(i,j-1):
                                        if passageOuest(getVal(matrice,i,j), getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
        if getVal(calque,ligA,colA)!=0:
            res=True
        return res

    def accessibleCalque(self,ligD,colD,ligA,colA):

        if len(plateau)!=7:
            matrice=[]
            miniListe=[]
            for element in plateau:
                miniListe.append(element)
                if len(miniListe)==7:
                    matrice.append(miniListe)
                    miniListe=[]
        res=False
        t=True
        marque=1
        calque=Matrice(getNbLignes(matrice),getNbColonnes(matrice))
        setVal(calque,ligD,colD,marque)
        while t==True:
            t=False
            for i in range(getNbLignes(matrice)):
                for j in range(getNbColonnes(matrice)):
                    if getVal(calque,i,j)!=0:
                        CoordonneesAutours=[(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
                        for (a,b) in CoordonneesAutours:
                            if not a>=getNbLignes(matrice) and not a<0 and not b>=getNbColonnes(matrice) and not b<0:
                                if getVal(calque,a,b)==0:
                                    if (a,b)==(i+1,j):
                                        if passageSud(getVal(matrice,i,j), getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
                                    elif (a,b)==(i,j+1):
                                        if passageEst(getVal(matrice,i,j), getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
                                    elif (a,b)==(i-1,j):
                                        if passageNord(getVal(matrice,i,j),getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
                                    elif (a,b)==(i,j-1):
                                        if passageOuest(getVal(matrice,i,j), getVal(matrice,a,b)):
                                            setVal(calque,a,b,getVal(calque,i,j)+1)
                                            t=True
        if getVal(calque,ligA,colA)!=0:
            res=True
        return calque

    def accessibleDist(self,ligD,colD,ligA,colA):
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
        calque=None
        res=None
        pos=(ligA,colA)
        Chemin=[(ligA,colA)]
        if accessible(self,ligD,colD,ligA,colA):
            calque=accessibleCalque(self,ligD,colD,ligA,colA)
            while not (ligD,colD) in Chemin:
                t=True
                ValeursACote=[(pos[0]+1,pos[1]), (pos[0]-1,pos[1]), (pos[0],pos[1]+1),(pos[0],pos[1]-1)]
                i=0
                while t==True:
                    (a,b)=ValeursACote[i]
                    if getVal(calque,a,b)==getVal(calque,Chemin[-1][0],Chemin[-1][1])-1 and getVal(calque,a,b)!=0:
                        Chemin.append((a,b))
                        pos=(a,b)
                        t=False
                    i+=1
            Chemin.reverse()
            res=Chemin
        return res


plateau(0,0)
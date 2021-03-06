# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
from random import *


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']

class Carte(object):
    def __init__(self,nord,est,sud,ouest,tresor=0,pions=[]):
        """
        constructeur
        """
        self._nord=nord
        self._est=est
        self._sud=sud
        self._ouest=ouest
        self._tresor=tresor
        self._pions=pions
        # self.murs = []
        # self.items = None

    def Carte(self, nord, est, sud, ouest, tresor=0, pions=[]):
        """
        permet de créer une carte:
        paramètres:
        nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
        tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
        pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
        """
        dico={'nord':self._nord,'est':self._est,'sud':self._sud,'ouest':self._ouest,'tresor':self._tresor,'pions':self._pions}
        return dico


    def estValide(self):
        """
        retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
        paramètre: c une carte
        """
        dico=self._nord,self._sud,self._est,self._ouest
        res=True
        cpt=0
        for elem in dico:
            if elem==True:
                cpt+=1
        if cpt>2:
            res=False
        return res

    def murNord(self):
        """
        retourne un booléen indiquant si la carte possède un mur au nord
        paramètre: c une carte
        """
        return self._nord

    def murSud(self):
        """
        retourne un booléen indiquant si la carte possède un mur au sud
        paramètre: c une carte
        """
        return self._sud

    def murEst(self):
        """
        retourne un booléen indiquant si la carte possède un mur à l'est
        paramètre: c une carte
        """
        return self._est

    def murOuest(self):
        """
        retourne un booléen indiquant si la carte possède un mur à l'ouest
        paramètre: c une carte
        """
        return self._ouest

    def getListePions(self):
        """
        retourne la liste des pions se trouvant sur la carte
        paramètre: c une carte
        """
        return self._pions

    def setListePions(self,listePions):
        """
        place la liste des pions passées en paramètre sur la carte
        paramètres: c: est une carte
                    listePions: la liste des pions à poser
        Cette fonction ne retourne rien mais modifie la carte
        """
        self._pions=listePions

    def getNbPions(self):
        """
        retourne le nombre de pions se trouvant sur la carte
        paramètre: c une carte
        """
        return len(self._pions)

    def possedePion(self,pion):
        """
        retourne un booléen indiquant si la carte possède le pion passé en paramètre
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        """
        res=False
        if pion in self._pions:
            res=True
        return res

    def getTresor(self):
        """
        retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
        paramètre: c une carte
        """
        return self._tresor

    def prendreTresor(self):
        """
        enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
        paramètre: c une carte
        résultat l'entier représentant le trésor qui était sur la carte
        """
        res=self._tresor
        self._tresor=0
        return res

    def mettreTresor(self,tresor):
        """
        met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
        paramètres: c une carte
                    tresor un entier positif
        résultat l'entier représentant le trésor qui était sur la carte
        """
        res=self._tresor
        self._tresor=tresor
        return res

    def prendrePion(self, pion):
        """
        enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        if pion in self._pions:
        	self._pions.remove(pion)

    def poserPion(self, pion):
        """
        pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        if pion not in self._pions:
    	    self._pions.append(pion)

    def tournerHoraire(self):
        """
        fait tourner la carte dans le sens horaire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        a=self._nord
        self._nord=self._ouest
        self._ouest=self._sud
        self._sud=self._est
        self._est=a


    def tournerAntiHoraire(self):
        """
        fait tourner la carte dans le sens anti-horaire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        a=self._nord
        self._nord=self._est
        self._est=self._sud
        self._sud=self._ouest
        self._ouest=a

    def tourneAleatoire(self):
        """
        faire tourner la carte d'un nombre de tours aléatoire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        for i in range(randint(1,10)):
            a=self._nord
            self._nord=self._est
            self._est=self._sud
            self._sud=self._ouest
            self._ouest=a

    #listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']

    def coderMurs(self):
        """
        code les murs sous la forme d'un entier dont le codage binaire 
        est de la forme bNbEbSbO où bN, bE, bS et bO valent 
        soit 0 s'il n'y a pas de mur dans dans la direction correspondante
        soit 1 s'il y a un mur dans la direction correspondante
        bN est le chiffre des unité, BE des dizaine, etc...
        le code obtenu permet d'obtenir l'indice du caractère semi-graphique
        correspondant à la carte dans la liste listeCartes au début de ce fichier
        paramètre c une carte
        retourne un entier indice du caractère semi-graphique de la carte
        """

        #l=[nord,est,sud,ouest]
        l=[0,0,0,0]
        i=0
        if self._nord:
    	    l[0]=1
        if self._est:
    	    l[1]=1
        if self._sud:
    	    l[2]=1
        if self._ouest: 
    	    l[3]=1
        l.reverse()
        code=str(l[0])+str(l[1])+str(l[2])+str(l[3])

        if code=='0000':
    	    i=0
        elif code=='0001':
    	    i=1
        elif code=='0010':
    	    i=2
        elif code=='0011':
    	    i=3
        elif code=='0100':
    	    i=4
        elif  code=='0101':
    	    i=5
        elif code=='0110':
    	    i=6
        elif code=='1000':
    	    i=8
        elif code=='1001':
    	    i=9
        elif code=='1010':
    	    i=10
        elif code=='1100':
    	    i=12
        elif code=='0111':
            i=7
        elif code=='1011':
            i=11
        elif code=='1101':
            i=13
        elif code=='1110':
            i=14
        elif code=='1111':
            i=15
        return i

    def decoderMurs(self,code):
        """
        positionne les murs d'une carte en fonction du code décrit précédemment
        paramètres c une carte
                   code un entier codant les murs d'une carte
        Cette fonction modifie la carte mais ne retourne rien
        """
        conversion= "{0:b}".format(code)
        conversion_4_bits= '0'*(4-len(conversion)) + conversion

        self._ouest = bool(int(conversion_4_bits[0]))
        self._sud = bool(int(conversion_4_bits[1]))
        self._est = bool(int(conversion_4_bits[2]))
        self._nord = bool(int(conversion_4_bits[3]))
    #Carte={'nord':False,'est':False,'sud':False,'ouest':True,'tresor':0,'pions':[]}


    def toChar(self):
        """
        fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
        paramètres c une carte
        """
        res='Ø'
        if listeCartes[self.coderMurs()]!='Ø':
            res=listeCartes[self.coderMurs()]
        return res

    def passageNord(self,carte2):
        """
        suppose que la carte2 est placée au nord de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le nord
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        res=False
        if not self._nord and not carte2._sud:
            res=True
        return res

    def passageSud(self,carte2):
        """
        suppose que la carte2 est placée au sud de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le sud
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        res=False
        if not self._sud and not carte2._nord:
            res=True
        return res

    def passageOuest(self,carte2):
        """
        suppose que la carte2 est placée à l'ouest de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'ouest
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        res=False
        if not self._ouest and not carte2._est:
            res=True
        return res

    def passageEst(self,carte2):
        """
        suppose que la carte2 est placée à l'est de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'est
        paramètres carte1 et carte2 deux cartes
        résultat un booléen    
        """
        res=False
        if not self._est and not carte2._ouest:
            res=True
        return res

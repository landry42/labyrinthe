# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module self._matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une self._matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

class Matrice(object):
    def __init__(self,nbLignes,nbColonnes,valeurParDefaut=0):
        """
        crée une matrice de nbLignes sur nbColonnes en mettant 
        valeurParDefaut dans chacune des cases
        """
        res = [valeurParDefaut] * nbLignes
        for i in range(nbLignes):
            res[i] = [valeurParDefaut] * nbColonnes
        self._matrice = res

    def getNbLignes(self):
        """
        retourne le nombre de lignes de cette matrice
        """
        return len(self._matrice)

    def getNbColonnes(self):
        """
        Retourne le nombre de colonnes de cette matrice.
        """
        return len(self._matrice[0])

    def getVal(self,ligne,colonne):
        """
        retourne la valeur qui se trouve en(ligne,colonne) de la matrice
        paramètres:ligne le numéro de la ligne
        colonne le numéro de la colonne
        """             
        
        return self._matrice[ligne][colonne]

    def setVal(self,ligne,colonne,valeur):
        """
        Fixe la valeur de la case aux coordonnees specifiees a la valeur specifiee.
        
        Parametres : ligne le numero de la ligne,
                     colonne le numero de la colonne, et
                     valeur la valeur a fixer.

        """
        self._matrice[ligne][colonne]=valeur


    #------------------------------------------        
    # decalagesgetNbLignes
    #------------------------------------------
    def decalageLigneAGauche(self, numLig, nouvelleValeur=0):
        """
        Permet de decaler une ligne vers la gauche en inserant une nouvelle valeur sur la droite de la dite ligne.

            Parametres : numLig la ligne a decaler, et
                        nouvelleValeur la valeur a placer.
            Resultat : la valeur ejectee apres le decalage.
        """
        ejectee=None
        self._matrice[numLig].insert(len(self._matrice[numLig]),nouvelleValeur)
        ejectee=self._matrice[numLig][0]
        self._matrice[numLig].remove(self._matrice[numLig][0])
        return ejectee

    def decalageLigneADroite(self, numLig, nouvelleValeur=0):
        """
        decale la ligne numLig d'une case vers la droite en insérant une nouvelle
            valeur pour remplacer la premiere case à gauche de cette ligne
            paramèteres: matrice la matrice considérée
                    numLig le numéro de la ligne à décaler
                    nouvelleValeur la valeur à placer
            résultat: la valeur de la case "ejectée" par le décalage
        """
        ejectee=None
        self._matrice[numLig].insert(0,nouvelleValeur)
        ejectee=self._matrice[numLig][7]
        self._matrice[numLig].pop()
        return ejectee


    def decalageColonneEnHaut(self, numCol, nouvelleValeur=0):
        """
        decale la colonne numCol d'une case vers le haut en insérant une nouvelle
        valeur pour remplacer la premiere case en bas de cette ligne
        paramèteres: self._matrice la self._matrice considérée
                    numCol le numéro de la colonne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        ejectee=None
        ejectee=self._matrice[0][numCol]
        for i in range(0,len(self._matrice)-1):
            self._matrice[i][numCol]=self._matrice[i+1][numCol]
        self._matrice[len(self._matrice)-1][numCol]=nouvelleValeur
        return ejectee,self._matrice

    #self._matrice=[[6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [8, 0, 0, 0, 0, 0, 0]]


    def decalageColonneEnBas(self, numCol, nouvelleValeur=0):
       """
        decale la colonne numCol d'une case vers le bas en insérant une nouvelle
        valeur pour remplacer la premiere case en haut de cette ligne
        paramèteres: matrice la matrice considérée
                    numCol le numéro de la colonne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """

        
       
if __name__ == "__main__":
    mat = Matrice(5,5,5)
    assert mat.getNbLignes() == 5
    mat.setVal(3,3,4)
    assert mat.getVal(3,3) == 4
    assert mat.decalageLigneAGauche(2,0) == 5
    #assert mat.decalageLigneADroite(2,0) == 5
    assert mat.
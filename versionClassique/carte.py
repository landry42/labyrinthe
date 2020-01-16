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
#carte={'nord':True,'est':False,'sud':False,'ouest':False,'tresor':0,'pions':[1]}
def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    dico={'nord':nord,'est':est,'sud':sud,'ouest':ouest,'tresor':tresor,'pions':pions}
    return dico

assert isinstance(Carte(False,False,False,True,0,[]),dict),'Erreur 1'

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    res=True
    cpt=0
    for a,b in c.items():
        if b==True:
            cpt+=1
    if cpt>2:
        res=False
    return res

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c['nord']

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c['sud']

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c['est']

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c['ouest']

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c['pions']

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c['pions']=listePions

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c['pions'])

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    return pion in c['pions']

def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c['tresor']

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c['tresor']
    c['tresor']=0
    return res

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=getTresor(c)
    c['tresor']=tresor
    return res
    """
    res=c['tresor']
    c['tresor']=tresor
    return res
    """

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion in c['pions']:
    	c['pions'].remove(pion)

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c['pions']:
    	c['pions'].append(pion)
    
def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    a=c['nord']
    c['nord']=c['ouest']
    c['ouest']=c['sud']
    c['sud']=c['est']
    c['est']=a
    return c

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    a=c['nord']
    c['nord']=c['est']
    c['est']=c['sud']
    c['sud']=c['ouest']
    c['ouest']=a
    return c
def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    for i in range(randint(1,10)):
    	a=c['nord']
    	c['nord']=c['est']
    	c['est']=c['sud']
    	c['sud']=c['ouest']
    	c['ouest']=a
    return c
#listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']

def coderMurs(c):
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
    if c['nord']:
    	l[0]=1
    if c['est']:
    	l[1]=1
    if c['sud']:
    	l[2]=1
    if c['ouest']: 
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

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    conversion= "{0:b}".format(code)
    conversion_4_bits= '0'*(4-len(conversion)) + conversion

    c["ouest"] = bool(int(conversion_4_bits[0]))
    c["sud"] = bool(int(conversion_4_bits[1]))
    c["est"] = bool(int(conversion_4_bits[2]))
    c["nord"] = bool(int(conversion_4_bits[3]))



#Carte={'nord':False,'est':False,'sud':False,'ouest':True,'tresor':0,'pions':[]}


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    res='Ø'
    if listeCartes[coderMurs(c)]!='Ø':
        res=listeCartes[coderMurs(c)]
    return res

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if not carte1['nord'] and not carte2['sud']:
        res=True
    return res

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if not carte1['sud'] and not carte2['nord']:
        res=True
    return res

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if not carte1['ouest'] and not carte2['est']:
        res=True
    return res

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    res=False
    if not carte1['est'] and not carte2['ouest']:
        res=True
    return res

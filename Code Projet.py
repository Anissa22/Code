 # -*- coding: iso-8859-1 -*-
import imageio
im = imageio.imread("D:\Cours\Telecom Bretagne\Projet DEV\Images\JAFFRE\JAFFRE027b.png") #Importation de l'image
blanc = imageio.imread("D:\Cours\Telecom Bretagne\Projet DEV\Images\Blanc.png") #Image blanche qui sert pour remplacer les lignes ou colonnes de pixels noirs
import numpy as np
from pylab import *
im2 = array(im)
blanc = imageio.imread("D:\Cours\Telecom Bretagne\Projet DEV\Images\Blanc.png") #Image blanche qui sert pour remplacer les lignes ou colonnes
blanc2 = array(blanc)




colonneGauche = int(2*im.shape[1]/3) # Un tiers de la largeur de la colonne
colonneDroit = im.shape[1] # dernière colonne
conditioncolonne = int(0,0085*im.shape[1])

while colonneDroit-colonneGauche >= conditioncolonne : # condition de sortie de la boucle
    
    finish = 0 # =1 si du texte est détecté sur une ligne
    
    noires=0
    # noires est un compteur qui compte de le nombre de pixels considérés comme noirs consécutifs sur la colonne
    blancs=0
    # blancs est un compteur qui compte de le nombre de pixels blancs consécutifs sur la colonne
    
    ligne=0
    # correspond à la ligne étudiée sur la colonne considérée
    # elle revient à 0 pour chaque changement de colonne
            
    compteur=0
    # indique de le nombre de changements de pixel noir à pixel blancs
    # tant que blancs et noires sont inférieurs à 200
    
    interrupteur=0
    # permet d'indiquer si nous sommes sur un suite d'éléments blancs ou noirs
    # 0 si la suite est blanche
    # 1 si la suite est noire
    
    colonneMilieu = int((colonneDroit+colonneGauche)/2)
    
    print('colonne', colonneMilieu)
    
    while ligne < im.shape[0] and finish == 0:
    # tant que toutes les lignes n'ont pas été parcourues ou que le bord du rectangle a été trouvé
    
    # Contenu expliqué sur la page suivante
        if interrupteur == 0 and noires != 0 : 
        # cette partie traduit le changement de pixel de blanc vers noir   
        # Si la suite est blanche et qu'un pixel noir est détecté
        
            interrupteur = 1
            # la suite devient noire
            
            compteur +=1
            # le compteur s'incremente
     
        
        elif interrupteur != 0 and noires == 0:
        # cette partie traduit le changement de pixel de noir vers blanc   
        # Si la suite est noire et qu'un pixel blanc est détecté
        
            interrupteur = 0
            # la suite devient blanche            
            
            compteur += 1
            # le compteur s'incremente
            
            
        if tuple(im[ligne][colonneMilieu])[1] > 144:
        # cette partie permet d'augmenter le nombre de noirs consécutifs
        # Si l'élément de la ligne et colonne dépasse le seuil de nuance de gris et est considéré comme noir
              
            noires+=1
            # le nombre de pixels noirs consécutifs s'incrémente
            
            blancs=0
            # le nombre de pixels blancs consécutifs revient à 0
            
            
        else:
        # cette partie permet d'augmenter le nombre de blancs consécutifs
        # Si l'élément de la ligne et colonne est noir
        
            noires=0
            # le nombre de pixels noirs consécutifs revient à 0
            
            blancs+=1
            # le nombre de pixels blancs consécutifs s'incrémente         
                        
            
        if compteur >= 8 and blancs<200 and noires<200:
        # cette partie représente la détection d'un bord
        # Si le nombre de pixels noirs ou blancs consécutifs ne sont pas trop grands
        # Et si le compteur dépasse 8

            finish = 1
            # Détection du texte
            
        elif blancs>200 or noires>200:
        # S'il y a trop de pixels de même couleur consécutifs
        
            compteur=0
            # Le compteur devient nul
            
        ligne += 1
        # La ligne est incrémenté de 1 à la fin de la boucle.

    if finish == 0: # Si aucun texte n'a été détecté sur la ligne
        colonneDroit = colonneMilieu
    else: # Si du texte a été détecté sur la ligne
        colonneGauche = colonneMilieu


im2[:,colonneMilieu + conditioncolonne : im.shape[1]]=blanc2[:,colonneMilieu + conditioncolonne : im.shape[1]]


colonneGauche = 0
colonneDroit = int(im.shape[1]/2)
while colonneDroit-colonneGauche >= 30:
    noires=0
    blancs=0
    ligne=0
    compteur=0
    interrupteur=0
    suite=0
    finish =0
    colonneMilieu = int((colonneDroit+colonneGauche)/2)
    print(colonneMilieu)
    while ligne < im.shape[0] and finish == 0:
        if interrupteur == 0 and noires != 0 :
            interrupteur = 1
            compteur +=1
        elif interrupteur != 0 and noires == 0:
            compteur += 1
            interrupteur = 0
        if tuple(im[ligne][colonneMilieu])[1] > 144:        
            noires+=1
            blancs=0
        else:
            noires=0
            blancs+=1
        if compteur >= 8 and blancs<200 and noires<200:
            finish = 1
        elif blancs>200 or noires>200:
            compteur=0
        ligne += 1
        
    if finish == 0:
        colonneGauche = colonneMilieu
    else:
        colonneDroit = colonneMilieu
        
im2[:, 0:max(colonneMilieu - 30,0)]=blanc2[:, 0:max(colonneMilieu - 30,0)]




ligne = im.shape[0]
finish = 0

while finish == 0 and ligne >= 0 :
    ligne -= 30
    noires=0
    blancs=0
    colonne=0
    compteur=0
    interrupteur=0
    print(ligne)
    while colonne < im.shape[1] and finish == 0:
        if interrupteur == 0 and noires != 0 :
            interrupteur = 1
            compteur +=1
        elif interrupteur != 0 and noires == 0:
            compteur += 1
            interrupteur = 0
        if tuple(im2[ligne][colonne]) != (255,255,255,255):        
            noires+=1
            blancs=0
        else:
            noires=0
            blancs+=1
        if compteur >= 8 and blancs<200 and noires<200:
            finish = 1
        elif blancs>200 or noires>200:
            compteur=0
        colonne += 1

im2[ligne + 30 : im.shape [0]]=blanc2[ligne + 30 : im.shape [0]]


ligne = 0
finish = 0

while finish == 0 and ligne <= im.shape[0] :
    ligne += 30
    noires=0
    blancs=0
    colonne=0
    compteur=0
    interrupteur=0
    print(ligne)
    while colonne < im.shape[1] and finish == 0:
        if interrupteur == 0 and noires != 0 :
            interrupteur = 1
            compteur +=1
        elif interrupteur != 0 and noires == 0:
            compteur += 1
            interrupteur = 0
        if tuple(im2[ligne][colonne]) != (255,255,255,255):        
            noires+=1
            blancs=0
        else:
            noires=0
            blancs+=1
        if compteur >= 8 and blancs<200 and noires<200:
            finish = 1
        elif blancs>200 or noires>200:
            compteur=0
        colonne += 1

im2[0 : ligne - 30]=blanc2[0 : ligne - 30]

# ligne1 = im.shape[0]
# finish = 0
# 
# while finish == 0 and ligne1 >= 0 :
#     ligne1 -= 100
#     noires=0
#     blancs=0
#     colonne=0
#     compteur=0
#     interrupteur=0
#     print(ligne1)
#     while colonne < im.shape[1] and finish == 0:
#         if interrupteur == 0 and noires != 0 :
#             interrupteur = 1
#             compteur +=1
#         elif interrupteur != 0 and noires == 0:
#             compteur += 1
#             interrupteur = 0
#         if tuple(im2[ligne][colonne]) != (255,255,255,255):        
#             noires+=1
#             blancs=0
#         else:
#             noires=0
#             blancs+=1
#         if compteur >= 8 and blancs<200 and noires<200:
#             finish = 1
#         elif blancs>200 or noires>200:
#             compteur=0
#         colonne += 1
# 
# 
# 
# ligne2 = 0
# finish = 0
# 
# while finish == 0 and ligne2 <= im.shape[0] :
#     ligne2 += 100
#     noires=0
#     blancs=0
#     colonne=0
#     compteur=0
#     interrupteur=0
#     print(ligne2)
#     while colonne < im.shape[1] and finish == 0:
#         if interrupteur == 0 and noires != 0 :
#             interrupteur = 1
#             compteur +=1
#         elif interrupteur != 0 and noires == 0:
#             compteur += 1
#             interrupteur = 0
#         if tuple(im2[ligne2][colonne]) != (255,255,255,255):        
#             noires+=1
#             blancs=0
#         else:
#             noires=0
#             blancs+=1
#         if compteur >= 8 and blancs<200 and noires<200:
#             finish = 1
#         elif blancs>200 or noires>200:
#             compteur=0
#         colonne += 1





# ligneHaut = max(ligne2 -1000, 0)
# ligneBas = min(ligne1 + 1000, im.shape[0])
# 
# while ligneBas - ligneHaut >= 30 :
#     noires=0
#     blancs=0
#     colonne=0
#     compteur=0
#     interrupteur=0
#     finish = 0
#     ligneMilieu = int((ligneBas+ligneHaut)/2)
#     print(ligneMilieu)
#     while colonne < im.shape[1] and finish == 0:
#         if interrupteur == 0 and noires != 0 :
#             interrupteur = 1
#             compteur +=1
#         elif interrupteur != 0 and noires == 0:
#             compteur += 1
#             interrupteur = 0
#         if tuple(im2[ligneMilieu][colonne])[1] > 144:        
#             noires+=1
#             blancs=0
#         else:
#             noires=0
#             blancs+=1
#         if compteur >= 8 and blancs<200 and noires<200:
#             finish = 1
#         elif blancs>200 or noires>200:
#             compteur=0
#         colonne += 1
#         
#     if finish == 0:
#         ligneBas = ligneMilieu
#     else:
#         ligneHaut = ligneMilieu
#         
#         
# im2[ligneMilieu + 30 : im.shape [0]]=blanc2[ligneMilieu + 30 : im.shape [0]]



# ligneHaut = max(ligne2 -1000, 0)
# ligneBas = min(ligne1 + 1000, im.shape[0])
# 
# while ligneBas - ligneHaut >= 30 :
#     noires=0
#     blancs=0
#     colonne=0
#     compteur=0
#     interrupteur=0
#     finish = 0
#     ligneMilieu = int((ligneBas+ligneHaut)/2)
#     print(ligneMilieu)
#     
#     while colonne < im.shape[1] and finish == 0:
#         if interrupteur == 0 and noires != 0 :
#             interrupteur = 1
#             compteur +=1
#         elif interrupteur != 0 and noires == 0:
#             compteur += 1
#             interrupteur = 0
#         if tuple(im2[ligneMilieu][colonne])[1] > 144:        
#             noires+=1
#             blancs=0
#         else:
#             noires=0
#             blancs+=1
#         if compteur >= 8 and blancs<200 and noires<200:
#             finish = 1
#         elif blancs>200 or noires>200:
#             compteur=0
#         colonne += 1
#         
#     if finish == 0:
#         ligneHaut = ligneMilieu
#     else:
#         ligneBas = ligneMilieu
#         
#         
# 
# im2[0 : ligneMilieu - 30]=blanc2[0 : ligneMilieu - 30]




imageio.imsave("D:\Cours\Telecom Bretagne\Projet DEV\Images\Yo1.png", im2)
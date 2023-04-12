# from chargement import *
# importation des stuctures de donnée de chargement.py, dont donjons pré-fait

def reprPersonnage(personnages):    #converti les tuples en dictionnaires
    """
    Renvoie un dictionnaire aventurier et liste de dicrionnaires dragons à partir d'une liste de listes personnages
    Une variable global niveau est également crée.
    aventurier et un item dragon = {position: (x,y), niveau}
    """
    dragons = []
    for i in personnages:
        position = i[1], i[2]
        if i[0] == 'A':
            if 'niveau' in globals():
                pass
            elif len(i) == 3:
                global niveau
                niveau = 1
            else:
                global niveau
                niveau = i[3]
            aventurier = { 'position' : (position), 'niveau' : niveau}
        elif i[0] == 'D':
            dragon = { 'position' : (position), 'niveau' : i[3]}
            dragons.append(dragon)
        # option: trésor
    return aventurier, dragons

# Gestion du donjon

def pivoter(donjon, position):
    """
    Pivote une case du donjon au coord position en décalant les valeurs vers la droite
    Modifie une valeur de donjon, ne renvoie rien
    """
    donjPivot = donjon[position[0]][position[1]]
    for i in range(4):
        donjPivot[i] = donjon[position[0]][position[1]][i-1]
    donjon[position[0]][position[1]] = donjPivot

def connecte(donjon, position1, position2):
    """
    Vérifie si 2 cases aux coords position1 et position2 sont connecté
    Renvoie True si oui, False sinon
    """
    if position1[0] == position2[0] :
        if position1[1] < position2[1]:
            if donjon[position1[0]][position1[1]][1] and donjon[position2[0]][position2[1]][3]:
                return True
        else:
            if donjon[position1[0]][position1[1]][3] and donjon[position1[0]][position2[1]][1]:
                return True
    elif position1[1] == position2[1]:
        if position1[0] < position2[0]:
            if donjon[position1[0]][position1[1]][2] and donjon[position2[0]][position2[1]][0]:
                return True
        else:
            if donjon[position1[0]][position1[1]][0] and donjon[position2[0]][position2[1]][2]:
                return True
    return False

# Intention de l'aventurier

def intention(donjon, position, dragons):
    """
    while True:
        for i in range(4):
            if
    """

# Tour de l'aventurier

def rencontre(aventurier, dragons):
    """
    Vérifie si la position de l'aventurier coincide avec celui d'un item dragon
    Si oui, assigne 'mort' à l'aventurier si son niveau est inférieur, retire l'item de la liste dragons sinon
    """
    for i in range(len(dragons)):
        if dragons[i]['position'] == aventurier['position']:
            if dragons[i]['niveau'] <= aventurier['niveau']:
                dragons.pop(i)
            else:
                aventurier = 'mort'
            break

def appliquer_chemin(aventurier, dragons, chemin):
    """
    Parcours la liste chemin et appelle la fonction rencontre, ne renvoie rien
    """
    for i in chemin:
        aventurier['position'] = i
        rencontre(aventurier, dragons)

def fin_partie(aventurier, dragons):
    """
    Renvoie -1 si la partie est perdu (l'aventurier est 'mort')
    1 si la partie est gagné (la liste dragons est vide)
    0 sinon, la partie continue
    """
    if aventurier == 'mort':
        return -1
    elif len(dragons) == 0:
        return 1
    return 0

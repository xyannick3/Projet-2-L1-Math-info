# from chargement import *
# importation des stuctures de donnée de chargement.py, dont donjons pré-fait
import collections

niveau = 0

def reprPersonnage(personnages):    #converti les tuples en dictionnaires
    """
    Renvoie un dictionnaire aventurier et liste de dicrionnaires dragons à partir d'une liste de listes personnages
    Une variable global niveau est également crée.
    aventurier et un item dragon = {position: (x,y), niveau}
    """
    global niveau
    dragons = []
    for i in personnages:
        position = i[1], i[2]
        if i[0] == 'A':
            if len(i) == 3:
                niveau = 1
            elif niveau != 0:
                pass
            else:
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
    Position = tuple(ligne, colonne)
    Modifie une valeur de donjon, ne renvoie rien
    """
    donjPivot = donjon[position[0]][position[1]]
    newcell = (donjPivot[3], donjPivot[0], donjPivot[1], donjPivot[2])
    donjon[position[0]][position[1]] = newcell

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

def cases_adjacentes(donjon, position):
    """
    Renvoie une liste des coords (x,y) des cases adjacentes à position
    """
    adjacents = []
    if connecte(donjon, position, (position[0]-1, position[1])):
        adjacents.append((position[0]-1, position[1]))
    elif connecte(donjon, position, (position[0], position[1]+1)):
        adjacents.append((position[0], position[1]+1))
    elif connecte(donjon, position, (position[0]+1, position[1])):
        adjacents.append((position[0]+1, position[1]))
    elif connecte(donjon, position, (position[0], position[1]-1)):
        adjacents.append((position[0], position[1]-1))
    return adjacents

# Intention de l'aventurier

def intention(donjon, position, dragons, visite = []): # Pour le moment, parcours en largeur
    """
    Parcours en largeur du donjon, renvoie deque qui est le chemin à prendre
    """
    deque = collections.deque()
    deque.appendleft(position)
    dragon = ((None,None),0)
    while len(deque) != 0:
        case = deque.popleft()
        for i in range(len(dragons)):
            if case == dragons[i]['position']:
                if dragons[i]['niveau'] > dragon:
                    dragon = dragons[i]
                    if i == len(dragons)-1:
                        deque.append(case)
                        return deque
        adjacents = cases_adjacentes(donjon, case)
        for i in adjacents:
            if i not in visite:
                visite.append(i)
                deque.extendleft(intention(donjon, i, dragons, visite))
        if len(deque) == 0:
            return None
        deque.appendleft(case)
        return deque

# Tour de l'aventurier

def rencontre(aventurier, dragons, pos):
    """
    Simule la rencontre entre l'aventurier et le dragon d'index pos dans "dragons
    Suppression de l'item de dragons si niveau(aventurier)>=niveau du dragon, "mort de l'aventurier sinon)
    """
    for i in len(dragons):
        if dragons[i][position] == pos:
            if dragons[i]['niveau'] <= aventurier['niveau']:
                dragons.pop(i)
                aventurier[niveau] += 1
            else:
                aventurier = 'mort'
            return None

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

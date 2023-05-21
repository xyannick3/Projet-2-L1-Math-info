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
    print(position)
    if (position[0] != 0) and connecte(donjon, position, (position[0]-1, position[1])):
        adjacents.append((position[0]-1, position[1]))
    if (position[1] != len(donjon[0])-1) and connecte(donjon, position, (position[0], position[1]+1)):
        adjacents.append((position[0], position[1]+1))
    if (position[0] != len(donjon)-1) and connecte(donjon, position, (position[0]+1, position[1])):
        adjacents.append((position[0]+1, position[1]))
    if (position[1] != 0) and connecte(donjon, position, (position[0], position[1]-1)):
        adjacents.append((position[0], position[1]-1))
    return adjacents

# Intention de l'aventurier

from queue import PriorityQueue

def intention(donjon, posAventurier, dragons):
    queue = PriorityQueue()  # Priority queue to keep track of cells to explore
    visite = set()  # Set to store visited cells

    for dragon in dragons:
        position = dragon['position']
        niveau = dragon['niveau']
        queue.put((-niveau, (posAventurier, [], position, niveau)))  # Add start cell and goals to the priority queue

    while not queue.empty():
        _, (case, chemin, dragon, niveau) = queue.get()  # Get the current cell, path, goal, and level

        # if current == goal:
        for i in dragons:
            if case == i['position']:
                return chemin + [case]  # Return the path if the goal is reached

        visite.add(case)  # Mark the current cell as visited

        voisins = listeVoisin(donjon, case)

        for voisin in voisins:
            coordsVoisin = voisin[0]

            if coordsVoisin not in visite and not presenceMur(donjon, case, coordsVoisin):
                queue.put((-niveau, (
                coordsVoisin, chemin + [case], dragon, niveau)))  # Add unvisited and unblocked neighbors to the queue

    return None  # Aucun chemin n'est trouvé

def presenceMur(donjon, case, voisin):
    row, col = case
    row_voisin, col_voisin = voisin

    if row_voisin < row:  # Voisin en haut
        return not donjon[row][col][0] or not donjon[row_voisin][col_voisin][2]
    elif row_voisin > row:  # Voisin en bas
        return not donjon[row][col][2] or not donjon[row_voisin][col_voisin][0]
    elif col_voisin > col:  # Voisin à droite
        return not donjon[row][col][1] or not donjon[row_voisin][col_voisin][3]
    elif col_voisin < col:  # Voisin à gauche
        return not donjon[row][col][3] or not donjon[row_voisin][col_voisin][1]
    else:  # Case seule
        return False


def listeVoisin(donjon, case):
    voisins = []
    row, col = case

    # Check top neighbor
    if row > 0 and donjon[row][col][0]:
        voisins.append(((row - 1, col), 'haut'))

    # Check right neighbor
    if col < len(donjon[0]) - 1 and donjon[row][col][1]:
        voisins.append(((row, col + 1), 'droite'))

    # Check bottom neighbor
    if row < len(donjon) - 1 and donjon[row][col][2]:
        voisins.append(((row + 1, col), 'bas'))

    # Check left neighbor
    if col > 0 and donjon[row][col][3]:
        voisins.append(((row, col - 1), 'gauche'))

    return voisins

# Tour de l'aventurier

def rencontre(aventurier, dragons, pos):
    """
    Simule la rencontre entre l'aventurier et le dragon d'index pos dans "dragons
    Suppression de l'item de dragons si niveau(aventurier)>=niveau du dragon, "mort de l'aventurier sinon)
    """
    for i in range(len(dragons)):
        if dragons[i]['position'] == pos: 
            if dragons[i]['niveau'] <= aventurier['niveau']:
                dragons.pop(i)
                aventurier['niveau'] += 1
            else:
                return 'mort'
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

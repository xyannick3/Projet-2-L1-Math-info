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

def intention1(donjon, pos_aventurier, dragons):
    """
    Vérifie si un dragon se situe sur la partition du donjon de l'aventurier
    Renvoie un chemin via la fonction fun.
    """
    chemin = collections.deque()
    part_donjon = tarjan(donjon)
    dragon = (-1,-1)
    for i in part_donjon:
        print("pos_aventurier :", pos_aventurier, "i est :", i)
        if pos_aventurier in i:
            print("pos aventurier dans i !")
            print("Partition :", part_donjon)
            for j in range(len(dragons)-1,1,-1):
                print("position dragon :", dragons[j]['position'])
                if dragons[j]['position'] in i:
                    dragon = dragons[j]['position']
                    break
            break
    if dragon == (-1,-1):
        return None

    chemin.extend(fun(donjon, pos_aventurier, dragon))
    return chemin

def fun(donjon, pos, dragon, visite = []):  #nom provisoire
    """
    Definition du chemin:
    """
    visite.append(pos)
    adjacents = cases_adjacentes(donjon, pos)
    for i in adjacents:
        if i not in visite:
            if dragon == i:
                return [pos,i]
            return [pos, fun(donjon,i,dragon,visite)]
    print("visite :", visite, "adjacents :", adjacents, "pos :", pos, "dragon :", dragon)


def tarjan(donjon):
    """
    Renvoie une partition des cases connexes du donjon.
    """
    visite = collections.deque()
    partition = []

    def parcours(case):
        visite.append(case)
        voisins = cases_adjacentes(donjon,case)
        for vois in voisins:
            print("vois :",vois)
            if vois not in visite:
                parcours(vois)
        c = []
        while True:
            adj = visite.pop()
            c.append(adj)
            if adj == case:
                break
        partition.append(c)
        visite.extend(c)

    for i in range(len(donjon)):
        for j in range(len(donjon[i])):
            case = (i,j)
            print("case :",case)
            if case not in visite:
                parcours(case)

    for i in range(len(partition)): #Solution peu optimisé pour doublon dans partition
        if i != len(partition)-1:
            j = i+1
            while j < len(partition[i:]):
                print("j :", j, "i :", i, "len partition :", len(partition))
                for k in partition[j]:
                    if k in partition[i]:
                        if len(partition[i]) < len(partition[j]):
                            print(partition.pop(i))
                j += 1

    return partition

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
from queue import PriorityQueue

from queue import PriorityQueue

def dfs_with_priority_v2(maze, start, goals):
    queue = PriorityQueue()  # Priority queue to keep track of cells to explore
    visited = set()  # Set to store visited cells
    
    for goal in goals:
        position = goal['position']
        level = goal['niveau']
        queue.put((-level, (start, [], position, level)))  # Add start cell and goals to the priority queue
    
    while not queue.empty():
        _, (current, path, goal, level) = queue.get()  # Get the current cell, path, goal, and level

        #if current == goal:
        for i in goals:
            if current == i['position']:
                return path + [current]  # Return the path if the goal is reached
        
        visited.add(current)  # Mark the current cell as visited
        
        neighbors = get_neighbors(maze, current)
        
        for neighbor in neighbors:
            neighbor_coords = neighbor[0]
            
            if neighbor_coords not in visited and not is_wall(maze, current, neighbor_coords):
                queue.put((-level, (neighbor_coords, path + [current], goal, level)))  # Add unvisited and unblocked neighbors to the queue

    return None  # Return None if no path is found


def is_wall(maze, current, neighbor):
    row, col = current
    neighbor_row, neighbor_col = neighbor
    
    if neighbor_row < row:  # Neighbor is above
        return not maze[row][col][0] or not maze[neighbor_row][neighbor_col][2]
    elif neighbor_row > row:  # Neighbor is below
        return not maze[row][col][2] or not maze[neighbor_row][neighbor_col][0]
    elif neighbor_col > col:  # Neighbor is to the right
        return not maze[row][col][1] or not maze[neighbor_row][neighbor_col][3]
    elif neighbor_col < col:  # Neighbor is to the left
        return not maze[row][col][3] or not maze[neighbor_row][neighbor_col][1]
    else:  # Same cell, no wall
        return False


def get_neighbors(maze, cell):
    neighbors = []
    row, col = cell
    
    # Check top neighbor
    if row > 0 and maze[row][col][0]:
        neighbors.append(((row - 1, col), 'top'))
    
    # Check right neighbor
    if col < len(maze[0]) - 1 and maze[row][col][1]:
        neighbors.append(((row, col + 1), 'right'))
    
    # Check bottom neighbor
    if row < len(maze) - 1 and maze[row][col][2]:
        neighbors.append(((row + 1, col), 'bottom'))
    
    # Check left neighbor
    if col > 0 and maze[row][col][3]:
        neighbors.append(((row, col - 1), 'left'))
    
    return neighbors
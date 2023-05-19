import os
class readin() :
    def __init__(self) :
        ...
        self.map=[]
    def translate(symbol) :
        if symbol=="═" :
            return (False,True,False,True)
        if symbol=="║" :
            return (True,False,True,False)
        if symbol=="╔" :
            return (False,True,True,False)
        if symbol=="╗" :
            return (False,False,True,True)
        if symbol=="╚" :
            return (True,True,False,False)
        if symbol=="╝" :
            return (True,False,False,True)
        if symbol=="╠" :
            return (True,True,True,False)
        if symbol=="╣" :
            return (True,False,True,True)
        if symbol=="╦" :
            return (False,True,True,True)
        if symbol=="╩" :
            return (True,True,False,True)
        if symbol=="╨" :
            return (True,False,False,False)
        if symbol=="╡" :
            return (False,False,False,True)
        if symbol=="╥" :
            return (False,False,True,False)
        if symbol=="╞" :
            return (False,True,False,False) 
        if symbol=="╬" :
            return (True,True,True,True)

    def lire(filename) :
        file = open(filename, encoding="utf8")
        filebyline=file.readlines()
        mazex=0
        mazey=0
        maze=[]
        dragons=[]
        for line in filebyline :
            if line[0]=="A" :
                # aventurier=(int(line[2]),int(line[4]))
                aventurier={'position' : (int(line[2]),int(line[4])),'niveau':1}
            if line[0]=="D" :
                # dragons.append((int(line[2]),int(line[4]),int(line[6]))) Ancien système
                dragons.append({'position' : (int(line[2]),int(line[4])),'niveau' :int(line[6])})
            else : 
                ligne=[]
                for i in range(len(line)-1) : 
                    ligne.append(readin.translate(line[i]))
                if ligne[0]!=None :
                    maze.append(ligne)
        return maze, aventurier, dragons
    def getlistofmazes() :
        entries=os.listdir('media/maps/')
        return entries

    def BooleanToText(booleaan) :
        if booleaan==(False,True,False,True) :
            return "═"
        if booleaan== (True,False,True,False):
            return "║"
        if booleaan== (False,True,True,False):
            return "╔"
        if booleaan== (False,False,True,True):
            return "╗"
        if booleaan== (True,True,False,False):
            return "╚"
        if booleaan== (True,False,False,True):
            return "╝"
        if booleaan== (True,True,True,False):
            return "╠"
        if booleaan== (True,False,True,True):
            return "╣"
        if booleaan== (False,True,True,True):
            return "╦"
        if booleaan== (True,True,False,True):
            return "╩"
        if booleaan== (True,False,False,False):
            return "╨"
        if booleaan== (False,False,False,True):
            return "╡"
        if booleaan== (False,False,True,False):
            return "╥"
        if booleaan== (False,True,False,False):
            return "╞" 
        if booleaan== (True,True,True,True):
            return "╬"
    def write(maze,aventurier,dragons) :
        with open('media/save/savedgame.txt','w',encoding="utf8") as file :
            for line in maze : 
                ligne=""
                for cell in line : 
                    ligne+=(readin.BooleanToText(cell))
                ligne+="\n"
                file.write(ligne)
            aven=f"A {aventurier['position'][0]} {aventurier['position'][1]} {aventurier['niveau']}\n"
            file.write(aven)
            for drag in dragons :
                dragon=f"D {drag['position'][0]} {drag['position'][1]} {drag['niveau']}\n"
                file.write(dragon)
    
    def liresave(filename='media/save/savedgame.txt') :
        """
        version différente pour le format de sauvegarde
        """
        file = open(filename, encoding="utf8")
        filebyline=file.readlines()
        mazex=0
        mazey=0
        maze=[]
        dragons=[]
        for line in filebyline :
            if line[0]=="A" :
                # aventurier=(int(line[2]),int(line[4]))
                aventurier={'position' : (int(line[2]),int(line[4])), 'niveau':int(line[6])}
            if line[0]=="D" :
                # dragons.append((int(line[2]),int(line[4]),int(line[6]))) Ancien système
                dragons.append({'position' : (int(line[2]),int(line[4])),'niveau' :int(line[6])})
            else : 
                ligne=[]
                for i in range(len(line)-1) : 
                    ligne.append(readin.translate(line[i]))
                if ligne[0]!=None :
                    maze.append(ligne)
        return maze, aventurier, dragons
if __name__=="__main__" :
    maze,aventurier,dragons=readin.lire("media/maps/map_test.txt")
    readin.write(maze,aventurier,dragons)
    print(readin.liresave())
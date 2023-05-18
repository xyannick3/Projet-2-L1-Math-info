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
        print(aventurier)
        return maze, aventurier, dragons
    def getlistofmazes() :
        entries=os.listdir('media/maps/')
        return entries
if __name__=="__main__" :
    #print(readin.lire("media/maps/map_test.txt"))
    print(readin.getlistofmazes())
    ...


try : import fltk as fltk 
except ImportError : import graphisme.fltk as fltk
#on considère que le labyrinthe est d'une largeur
#et d'une grandeur de 6 par défaut 
# note : tuplet des couloirs sera north; east; sud; west; 
#_______
resolution=(1000,1000)
lenghtOfTheMap=6
class graphism() :
    """
    cette classe contiendra tout les éléments d'interaction avec l'aspect graphique du projet
    """
    def __init__(self,xwindow=resolution[0],ywindow=resolution[1],widness=lenghtOfTheMap) :
        self.xwindow=xwindow
        self.ywindow=ywindow
        self.wideness=widness
        self.cellsize=min(xwindow,ywindow)//widness
    def CreateWindow(self) :
        """
        créer une fenêtre et affiche brickwall.png
        """
        fltk.cree_fenetre(self.xwindow,self.ywindow)
        fltk.image(0,0,'media/brickwall.png',ancrage='nw',tag='im',largeur=self.xwindow,hauteur=self.ywindow)
    def displayCell(self,cell,x,y) :
        """
        affiche une cellule dépendant de uplet tel que (true,true,true,true) soit une case totalement ouverte, des falses représentent de cases fermées.
        """
        i=0
        for elem in cell :
            fltk.rectangle(x*self.cellsize-self.cellsize//5,y*self.cellsize,x*self.cellsize+self.cellsize//5,y*self.cellsize+self.cellsize//5,couleur='black',remplissage='black')
            fltk.rectangle((x+1)*self.cellsize+self.cellsize//5,y*self.cellsize-self.cellsize//5,(x+1)*self.cellsize-self.cellsize//5,(y)*self.cellsize+self.cellsize//5,couleur='black',remplissage='black')
            fltk.rectangle((x+1)*self.cellsize+self.cellsize//5,(y+1)*self.cellsize+self.cellsize//5,(x+1)*self.cellsize-self.cellsize//5,self.cellsize*(y+1)-self.cellsize//5,couleur='black',remplissage='black')
            fltk.rectangle((x)*self.cellsize,(y+1)*self.cellsize-self.cellsize//5,(x)*self.cellsize-self.cellsize//5,(y+1)*self.cellsize+self.cellsize//5,couleur='black',remplissage='black')
            if not(elem) :
                
                if i==0 :
                    fltk.rectangle(x*self.cellsize,y*self.cellsize,self.cellsize*(x+1),self.cellsize*(y)+self.cellsize//7,couleur='black',remplissage='black')
                if i==1 :
                    fltk.rectangle((x+1)*self.cellsize,y*(self.cellsize),(x+1)*self.cellsize-self.cellsize//7,(y+1)*self.cellsize,couleur='black',remplissage='black')
                if i==2 :
                    fltk.rectangle((x+1)*self.cellsize,(y+1)*(self.cellsize),x*self.cellsize,(y+1)*(self.cellsize)-self.cellsize//7,couleur='black',remplissage='black')
                
                if i==3 :
                    fltk.rectangle(x*self.cellsize,(y+1)*self.cellsize,x*self.cellsize+self.cellsize//7,y*self.cellsize,couleur='black',remplissage='black')
                
            i+=1
    def displayMaze(self,Maze) :
        """
        affiche Le labyrinthe  l'entrée sera une liste de liste contenant ces uplets
        """
        x=0
        y=0
        for rangée in Maze : 
            for elem in rangée :
                self.displayCell(elem,x,y)
                x+=1
                if x>=6 :
                    x=0
            y+=1
    def mappingclick(self,mouse) :
        """
        Dans cette fonction en prend comme entrée les coordonnées du click sur le plateau et on retourne les coordonnées de la cellule qui a été cliqué
        """
        return mouse[0]//self.cellsize,mouse[1]//self.cellsize



if __name__=='__main__' :
    from random import choice
    test=graphism()
    test.CreateWindow()
    #test.displayCell(cell=(True,True,True,False),y=0,x=0)
    listetest=[]
    comb1=(True,True,True,True)
    comb2=(False,True,True,True)
    comb3=(False,False,True,True)
    comb4=(False,False,False,True)
    comb5=(False,False,False,False)
    comb6=(True,False,False,False)
    comb7=(True,True,False,False)
    comb8=(True,True,True,False)
    comb9=(True,False,False,True)
    comb10=(True,False,True,False)
    comb11=(False,True,False,True)
    comb12=(False,True,True,False)
    comb=[comb1,comb2,comb3,comb4,comb5,comb6,comb7,comb8,comb9,comb10,comb11,comb12]
    for i in range(6) :
        listetest.append([])
        for j in range(6) :
            listetest[i].append(choice(comb))
    #print(listetest)
    test.displayMaze(listetest)
    while True : 
        print(test.mappingclick(fltk.attend_clic_gauche()))
try : import fltk as fltk 
except ImportError : import graphisme.fltk as fltk
#on considère que le labyrinthe est d'une largeur
#et d'une grandeur de 6 par défaut 
# note : tuplet des couloirs sera north; east; sud; west; 
#_______
resolution=(1000,1000)
lenghtOfTheMap=6 #Ceci sera modifié plus tard pour permettre la compatibilité avec des cartes plus grandes, à noté que tout est déjà fait dans le moteur graphique;
                 #pour permettre la modif de tout les paramètres d'affichage. quelquechose à voir serait de pouvoir ajuster la taille de l'interface par rapport à 
                 #la taille de la fenêtre car la nouvelle version de fltk permet d'avoir accès à ces paramètres et de détecter leur modifications.
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
            fltk.rectangle(x*self.cellsize-self.cellsize//5,y*self.cellsize,x*self.cellsize+self.cellsize//5,y*self.cellsize+self.cellsize//5,couleur='#3B3C36',remplissage='#3B3C36')
            fltk.rectangle((x+1)*self.cellsize+self.cellsize//5,y*self.cellsize-self.cellsize//5,(x+1)*self.cellsize-self.cellsize//5,(y)*self.cellsize+self.cellsize//5,couleur='#3B3C36',remplissage='#3B3C36')
            fltk.rectangle((x+1)*self.cellsize+self.cellsize//5,(y+1)*self.cellsize+self.cellsize//5,(x+1)*self.cellsize-self.cellsize//5,self.cellsize*(y+1)-self.cellsize//5,couleur='#3B3C36',remplissage='#3B3C36')
            fltk.rectangle((x)*self.cellsize,(y+1)*self.cellsize-self.cellsize//5,(x)*self.cellsize-self.cellsize//5,(y+1)*self.cellsize+self.cellsize//5,couleur='#3B3C36',remplissage='#3B3C36')
            if not(elem) :
                
                if i==0 :
                    fltk.rectangle(x*self.cellsize,y*self.cellsize,self.cellsize*(x+1),self.cellsize*(y)+self.cellsize//7,couleur='#3B3C36',remplissage='#3B3C36')
                if i==1 :
                    fltk.rectangle((x+1)*self.cellsize,y*(self.cellsize),(x+1)*self.cellsize-self.cellsize//7,(y+1)*self.cellsize,couleur='#3B3C36',remplissage='#3B3C36')
                if i==2 :
                    fltk.rectangle((x+1)*self.cellsize,(y+1)*(self.cellsize),x*self.cellsize,(y+1)*(self.cellsize)-self.cellsize//7,couleur='#3B3C36',remplissage='#3B3C36')
                
                if i==3 :
                    fltk.rectangle(x*self.cellsize,(y+1)*self.cellsize,x*self.cellsize+self.cellsize//7,y*self.cellsize,couleur='#3B3C36',remplissage='#3B3C36')
                
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

    def knight(self,x,y,level) :
        """
        Affiche le chevalier dans la case (x;y);\nLa taille du chevalier est 4/6 la taille d'une cellule.
        """
        fltk.image(self.cellsize//2+x*self.cellsize,self.cellsize//2+y*self.cellsize,'media/Knight_s.png',ancrage='center',largeur=int(self.cellsize*(4/6)),hauteur=int(self.cellsize*(4/6)),tag='knight')
        fltk.rectangle(x*self.cellsize+int(self.cellsize*(4/6)),y*self.cellsize+int(self.cellsize*(1/6)),x*self.cellsize+int(self.cellsize*(5/6)),y*self.cellsize+int(self.cellsize*(2/6)),remplissage='white',tag="knight")
        fltk.texte(x*self.cellsize+int(self.cellsize*(4/6)),y*self.cellsize+int(self.cellsize*(1/6)),f"{level}",ancrage="nw",tag="knight",taille=int((self.cellsize*(2/6))-(self.cellsize*(1/5))))
    def dragon(self,x,y,level) :
        """
        Affiche un dragon dans la case (x,y) de niveau level;
        """
        fltk.image(self.cellsize//2+x*self.cellsize,self.cellsize//2+y*self.cellsize,'media/Dragon_s.png',ancrage='center',largeur=int(self.cellsize*(4/6)),hauteur=int(self.cellsize*(4/6)),tag=f'dragon')
        fltk.rectangle(x*self.cellsize+int(self.cellsize*(4/6)),y*self.cellsize+int(self.cellsize*(1/6)),x*self.cellsize+int(self.cellsize*(5/6)),y*self.cellsize+int(self.cellsize*(2/6)),remplissage='white',tag="dragon")
        fltk.texte(x*self.cellsize+int(self.cellsize*(4/6)),y*self.cellsize+int(self.cellsize*(1/6)),f"{level}",ancrage="nw",tag="dragon",taille=int((self.cellsize*(2/6))-(self.cellsize*(1/5))))

    def arrow(self,array:list) :
        """
        Prend en input une liste de cases (x,y). Affiche une flèche dont la destination est la première coordonnée et le point de départ la dernière coordonnée 
        la liste doit avoir au minimum deux éléments sinon index out of range error ^^. 
        la liste doit ressembler à quelquechose du genre [(x0:int,y0:int),...,(x:int,y:int)]
        """
        fltk.fleche(self.cellsize//2+array[1][0]*self.cellsize,self.cellsize//2+array[1][1]*self.cellsize,self.cellsize//2+array[0][0]*self.cellsize,self.cellsize//2+array[0][1]*self.cellsize,'red',self.cellsize//20,tag="arrow")
        fltk.ligne(self.cellsize//2+array[1][0]*self.cellsize,self.cellsize//2+array[1][1]*self.cellsize,self.cellsize//2+array[0][0]*self.cellsize,self.cellsize//2+array[0][1]*self.cellsize,'red',self.cellsize//30,tag="arrow")

        for i in range(1,len(array)-1) :
            fltk.ligne(self.cellsize//2+array[i][0]*self.cellsize,self.cellsize//2+array[i][1]*self.cellsize,self.cellsize//2+array[i+1][0]*self.cellsize,self.cellsize//2+array[i+1][1]*self.cellsize,'red',self.cellsize//30,tag="arrow")
    
    def diamond(self,x,y) :
        """
        affiche un diamand dans la position indiqué, plutôt simple ^^.
        """
        fltk.image(self.cellsize//2+x*self.cellsize,self.cellsize//2+y*self.cellsize,'media/treasure.png',ancrage='center',largeur=int(self.cellsize*(4/6)),hauteur=int(self.cellsize*(4/6)),tag='diamond')


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
    fleche=[(0,0),(0,1),(1,1),(2,1),(2,2)]
    test.arrow(fleche)
    while True : 
        data=test.mappingclick(fltk.attend_clic_gauche())
        fltk.efface('knight')
        fltk.efface('dragon')
        fltk.efface('diamond')
        #modifier ce qu'il y a ci dessous pour tester les différentes images
        #test.knight(data[0],data[1],1)
        #test.dragon(data[0],data[1],2)
        test.diamond(data[0],data[1])
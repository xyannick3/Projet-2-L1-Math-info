import graphisme.fltk as fltk
import graphisme.graph as graph
import moteur_de_jeu.engine as engine
import changement.change as change
from time import sleep

#On ajoutera au fure et à mesure les imports et le code 
#
#
#
#
#
#
if __name__=="__main__" :
    
    resolution=(1000,1000)
    test=graph.gameGraph()
    test.CreateWindow()
    menutest=graph.menu()
    menuee=True
    game=False
    firstbutton=False
    while menuee :
        ...
        menutest.button(resolution[0]//2-resolution[0]//5,resolution[0]//2-resolution[0]//20,resolution[0]//2+resolution[0]//5,resolution[0]//2+resolution[0]//20,'Save')
        menutest.button(resolution[0]//2-resolution[0]//5,resolution[0]//4-resolution[0]//20,resolution[0]//2+resolution[0]//5,resolution[0]//4+resolution[0]//20,"Play")
        menutest.button(resolution[0]//2-resolution[0]//5,resolution[0]-resolution[0]//4-resolution[0]//20,resolution[0]//2+resolution[0]//5,resolution[0]-resolution[0]//4+resolution[0]//20,"Quit")
        data=fltk.attend_clic_gauche()
        print(data)
        # print('x1',data[0]>=resolution[0]//2-resolution[0]//5,'\nx2',data[0]<=resolution[0]//2+resolution[0]//5,'\ny1',data[1]>=resolution[0]//4-resolution[0]//20,'\ny2',data[1]<=resolution[0]//4+resolution[0]//20)
        if (data[0]>=resolution[0]//2-resolution[0]//5 and data[0]<=resolution[0]//2+resolution[0]//5) and (data[1]>=resolution[0]//4-resolution[0]//20 and data[1]<=resolution[0]//4+resolution[0]//20) :
            menuee=False
            game=True
            firstbutton=True
        elif (data[0]>=resolution[0]//2-resolution[0]//5 and data[0]<=resolution[0]//2+resolution[0]//5) and (data[1]>=resolution[0]-resolution[0]//4-resolution[0]//20 and data[1]<=resolution[0]-resolution[0]//4+resolution[0]//20): 
            menuee=False
        elif (data[0]>=resolution[0]//2-resolution[0]//5 and data[0]<=resolution[0]//2+resolution[0]//5) and (data[1]>=resolution[0]//2-resolution[0]//20 and data[1]<=resolution[0]//2+resolution[0]//20) :
            menuee=False
            game=True

    fltk.efface('bouton')
    if firstbutton :
        maps=change.readin.getlistofmazes()
        nombreboutons=len(maps)
        listofx1s=[]
        listofx2s=[]
        listofy1s=[]
        listofy2s=[]
        for i in range(len(maps)) : 
            x1=resolution[0]//2-resolution[0]//5
            listofx1s.append(x1)
            y1=(resolution[0]//nombreboutons)*(i+1)
            listofy1s.append(y1)
            x2=resolution[0]//2+resolution[0]//5
            listofx2s.append(x2)
            y2=(resolution[0]//nombreboutons)*(i+1)-resolution[0]//20
            listofy2s.append(y2)
            menutest.button(x1,y1,x2,y2,maps[i])
        selectionmap=True
        while selectionmap :
            data=fltk.attend_clic_gauche()
            for i in range(len(maps)) :
                print('x1',data[0]>=listofx1s[i],'\nx2',data[0]<=listofx2s[i],'\ny1',data[1]>=listofy1s[i],'\ny2',data[1]<=listofy2s[i])
                if (data[0]>=listofx1s[i] and data[0]<=listofx2s[i]) and (data[1]<=listofy1s[i] and data[1]>=listofy2s[i]) :
                    content=change.readin.lire(f"media/maps/{maps[i]}")
                    selected=i
                    selectionmap=False
                    fltk.efface('bouton')
    else : 
        content=change.readin.liresave()
    maze=content[0]
    aventurier=content[1]
    dragons=content[2]
    test.displayMaze(maze)
    test.knight(aventurier['position'][0],aventurier['position'][1],aventurier['niveau'])
    for drag in dragons :
        test.dragon(drag['position'][0],drag['position'][1],drag['niveau'])

    while game :
        fltk.efface("arrow")
        # print("intention",engine.intention(maze,aventurier['position'],dragons)) # test
        # print("intention Tarjan",engine.intention1(maze,aventurier['position'],dragons)) # test 
        path =engine.intention(maze,aventurier['position'],dragons)
        if path!=None and len(path)!=1 :
            print(path)
            test.arrow(array=path)
            ...
        ev=fltk.attend_ev()
        print(ev)
        if ev[0]=="Quitte" :
            game=False
            change.readin.write(maze,aventurier,dragons)
        elif ev[0]=='ClicGauche' :
            data=test.mappingclick((fltk.abscisse(ev),fltk.ordonnee(ev)))
            data=[data[1],data[0]]
            #print(data)
            engine.pivoter(maze,data)
            fltk.efface('wall')
            fltk.efface('knight')
            fltk.efface('dragon')
            test.displayMaze(maze)
            test.knight(aventurier['position'][0],aventurier['position'][1],aventurier['niveau'])
            for drag in dragons :
                test.dragon(drag['position'][0],drag['position'][1],drag['niveau'])
        elif ev[0]=="Touche" :
            touche=fltk.touche(ev)
            print(touche)
            if path!=None and touche=="space" :
                for i in path : 
                    print(i)
                    aventurier['position']=i
                    fltk.efface('knight')
                    fltk.efface('dragon')
                    life=engine.rencontre(aventurier,dragons,aventurier['position'])
                    status=engine.fin_partie(aventurier,dragons)
                    test.knight(aventurier['position'][0],aventurier['position'][1],aventurier['niveau'])
                    for drag in dragons :
                        test.dragon(drag['position'][0],drag['position'][1],drag['niveau'])

                    fltk.mise_a_jour()
                    sleep(0.5)

                    print(status)
                    if life!=None : 
                        game=False
                        fltk.efface_tout()
                        test.displaybackground()
                        menutest.button(resolution[0]//2-resolution[0]//5,resolution[0]//2-resolution[0]//20,resolution[0]//2+resolution[0]//5,resolution[0]//2+resolution[0]//20,'Defeat T_T')
                        fltk.attend_ev()
                    elif status==1 :
                        game=False
                        fltk.efface_tout()
                        test.displaybackground()
                        menutest.button(resolution[0]//2-resolution[0]//5,resolution[0]//2-resolution[0]//20,resolution[0]//2+resolution[0]//5,resolution[0]//2+resolution[0]//20,'Victory !')
                        fltk.attend_ev()
            elif touche=="r" :
                fltk.efface_tout()
                print('test')
                content=change.readin.lire(f"media/maps/{maps[selected]}")
                maze=content[0]
                aventurier=content[1]
                dragons=content[2]
                test.displaybackground()
                test.displayMaze(maze)
                test.knight(aventurier['position'][0],aventurier['position'][1],aventurier['niveau'])
                for drag in dragons :
                    test.dragon(drag['position'][0],drag['position'][1],drag['niveau'])
                fltk.mise_a_jour()
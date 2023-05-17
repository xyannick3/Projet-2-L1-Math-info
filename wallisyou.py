import graphisme.fltk as fltk
import graphisme.graph as graph
import moteur_de_jeu.engine as engine
import changement.change as change

#On ajoutera au fure et à mesure les imports et le code 
#
#
#
#
#
#
if __name__=="__main__" :
    content=change.readin.lire("media/maps/map1.txt")
    maze=content[0]
    aventurier=content[1]
    dragons=content[2]
    resolution=(1000,1000)
    test=graph.gameGraph()
    test.CreateWindow()
    test.displayMaze(maze)
    test.knight(aventurier['position'][0],aventurier['position'][1],aventurier['niveau'])
    for drag in dragons :
        test.dragon(drag['position'][0],drag['position'][1],drag['niveau'])
    print('donjon=',maze)
    print('position = ',aventurier['position'])
    print('dragons=',dragons)
    while True :
        print("intention",engine.intention(maze,aventurier['position'],dragons))
        data=test.mappingclick(fltk.attend_clic_gauche())
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
    # fleche=[(0,0),(0,1),(1,1),(2,1),(2,2)]
    # test.arrow(fleche)
    # while True : 
    #     data=test.mappingclick(fltk.attend_clic_gauche())
    #     data=[data[1],data[0]]
    #     print(data)
    #     fltk.efface('knight')
    #     fltk.efface('dragon')
    #     fltk.efface('diamond')
    #     engine.pivoter(listetest,data)
    #     fltk.efface('wall')
    #     test.displayMaze(listetest)
    #     # modifier ce qu'il y a ci dessous pour tester les différentes images
    #     # test.knight(data[0],data[1],1)
    #     # test.dragon(data[0],data[1],2)
    #     # test.diamond(data[0],data[1])


    # ... # à remplir plus tard dans le projet
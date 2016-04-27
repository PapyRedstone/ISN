# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:30:43 2016

@author: alexandre.febvre
"""

def pathfinding(Map, posOrigin, posTarget):
    """
    Fonction retournant les mouvement necessaire pour atteindre l'objectif en
    utilisant l'algorithme de recherche de chemin A*
    """

    #Definition des listes necessaires
    lOpen = []      #liste contenant les points a etudier
    lClose = []     #liste contenant les points deja étudier

    def retracePath(node):
        """
        Fonction permettant de retarcer le chemin de l'arrive a l'origin
        """
        path = []       #liste contenant le chemin de la cible vers le depart
        tmp = Node()    #on definit tmp comme etant un point
        tmp.setEq(node) #et on le met égale a node
        path.append(tmp)#on l'ajoute au chemin

        #tant que le parent n'est pas le parent par defaut
        while tmp.parent != {"x":-1, "y":-1}:
            #on trouve l'index dans lOpen du parent de tmp
            index = [lClose[i].pos for i in range(len(lClose)-1)].index(tmp.parent)
            #on redefinit tmp comme etant son parent
            tmp = lClose[index]
            #on l'ajoute au chemin
            path.append(tmp)


        #ici on transforme chemin brute en un chemin explicite
        pathExplicit = [] #on definit le chemin explicite
        for i in range(len(path)-1):
            #on définit la difference de coordonée entre le point étudier et
            #son parent
            X = path[i].pos["x"] - path[i+1].pos["x"]
            Y = path[i].pos["y"] - path[i+1].pos["y"]
            #suivant la position relative on ajoute un déplacement
            if X == -1:
                pathExplicit.append("LEFT")
            elif X == 1:
                pathExplicit.append("RIGHT")
            elif Y == -1:
                pathExplicit.append("UP")
            elif Y == 1:
                pathExplicit.append("DOWN")

        #on retourne le chemin pour aller de l'origine vers la cible
        pathExplicit.reverse()
        return pathExplicit #on retourne le chemin explicite


    def addAdjacentCase(node):
        """
        Fonction permettant d'ajouter les point adjacent a node dans lOpen
        """
        for pos in ((0,1), (0,-1), (1,0), (-1,0)):
            X = node["x"]+pos[0]       #definission des coordonees du point
            Y = node["y"]+pos[1]       #a étudier
            if (X < 0 or
                X >= len(Map[0]) or
                Y < 0 or
                Y >= len(Map)):
                continue
            if Map[Y][X] == 0:     #on verifie que ce n'est pas un obstacle
                continue
            tmp = Node({"x":X, "y":Y}, node)  #on cree le node qui est valide

            if not tmp in lClose:        #on verifie qu'il n'as pas éte étudier
                if tmp in lOpen:         #si il est dans la liste a étudier
                    i = lOpen.index(tmp)
                    if lOpen[i].coutA < tmp.coutA:#si il est plus interresant
                        lOpen[i].setEq(tmp)#on redefinit son parent
                else:
                    lOpen.append(tmp)   #sinon on l'ajoute a la liste a etudier

    def heurastique(node, target):
        """
        Retourne la distance entre les deux points node et target suivant la
        distance de Manhattan
        """
        return abs(node["x"]-target["x"])+abs(node["y"]-target["y"])

    class Node:
        """
        Classe representant les points
        Il possede des coordonees et un parent défini par ses coordonées
        Il possede la distance a la cible (coutA)
        Il possede des élements de comparaison
        """
        def __init__(self,
                     pos = {"x":-1,"y":-1},
                     parent = {"x":-1,"y":-1}):
            self.pos = pos
            self.parent = parent
            self.coutA = heurastique(self.pos,posTarget)
        
        def __eq__(self,right):
            return self.pos == right.pos
        
        def __ne__(self,right):
            return self.pos != right.pos
        
        def __lt__(self,right):
            return self.coutA < right.coutA
            
        def __gt__(self,right):
            return self.coutA > right.coutA
        
        def __le__(self,right):
            return self.coutA <= right.coutA
        
        def __ge__(self,right):
            return self.coutA >= right.coutA
            
        def setEq(self,right):
            self.pos = right.pos
            self.parent = right.parent
            self.coutA = right.coutA
    """
    Debut de l'algorithme de recherche A*
    """    
    #on definit tmp comme étant un point de position posOrigin
    tmp = Node(posOrigin)
    #on ajoute a la liste des points a etudier les voisins de tmp
    addAdjacentCase(tmp.pos) 
    #on ajoute tmp a la liste des points étudier
    lClose.append(tmp)
    #tant que l'on a pas atteint la cible ou que la liste n'est pas vide
    while ((not tmp == Node(posTarget)) and len(lOpen) != 0 ):    
        #on trie la liste : le point avec le plus petit coutA a l'index 0
        lOpen.sort()
        #on recupere le point avec le meilleur coutA
        tmp = lOpen[0]
        #on ajoute a la liste des points a etudier ses voisins
        addAdjacentCase(tmp.pos)
        #on l'ajoute a la liste des points etudier
        lClose.append(tmp)
        #on le retire de la liste des points a etudier
        lOpen.remove(tmp)

        
    #si on est arrive on retourne le chemin, sinon on renvoie None
    if tmp == Node(posTarget):
        return retracePath(tmp)
    else:
        print("Pas de solutions")
        return None
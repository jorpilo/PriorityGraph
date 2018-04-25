"""
Name: Mainpy
Proyect: PriorityGraph
Autor: Jorge Pinilla López
Date: 25/04/2017
Version: 1.1
Description: Test example for PriorityGraph class
"""

from PriorityGraph import *


def main():
    matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 2, 2, 0, 0, 1, 2, 5, 12],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 5, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 8],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
              [2, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 12],
              [0, 0, 0, 1, 5, 0, 1, 0, 0, 0, 0, 1, 1, 8],
              [3, 0, 0, 0, 0, 0, 2, 2, 1, 0, 2, 0, 2, 12],
              [2, 2, 2, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 5],
              [1, 1, 1, 0, 1, 0, 5, 0, 1, 0, 0, 0, 2, 9],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0]
              ]

    nodes = [str(i) for i in range(len(matrix))]
    graph = Graph()
    for node in nodes:
        graph.addNode(node)

    traslados = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for z in range(matrix[i][j]):
                graph.addLink(str(i), str(j), i+j)
                traslados += 1



    print(traslados)
#    print(str(graph))

    routes = graph.SearchPriorityCicles()
    numtraslados = 0

    print("Numero de ciclos -> "+ str(len(routes)))
    for i in range(len(routes)):
        route = routes[i]
        print("#"+str(i) + " ----------------")
        for link in route:
            print(link)
            numtraslados += 1
    print("-------------------------------------------")
    print("Numero de traslados -> " + str(numtraslados))






if __name__ == "__main__":
    main()

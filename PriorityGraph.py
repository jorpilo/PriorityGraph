"""
Name: PriorityGraph.py
Proyect: PriorityGraph
Autor: Jorge Pinilla López
Date: 25/04/2017
Version: 1.1
Description: Priority graph class and cicle search enforcing priorities
"""

from sortedcontainers import SortedListWithKey

DEBUG = True


class Graph:
    nodes = dict()
    links = SortedListWithKey(key=lambda item: item.priority)

    def addNode(self, name):
        self.nodes[name] = self.Node(name)

    def addLink(self, base, to, priority):
        __base = self.nodes[base]
        __to = self.nodes[to]
        link = self.Link(__base, __to, priority)
        self.links.add(link)
        __base.addTo(link)
        __to.addBase(link)

    def resetGraph(self):
        clean = 0
        deadLinks = 0
        for link in self.links:
            link.used = False
            clean += 1
        for node in self.nodes.values():
            if len(node.base) == 0:
                for link in node.to:
                    link.used = True
                    deadLinks += 1
        if DEBUG:
            print("Clean links: " + str(clean))
            print("Dead links: " + str(deadLinks))

    def SearchPriorityCicles(self):
        self.resetGraph()
        result = []
        i = 0
        for link in self.links:
            if DEBUG:
                if not link.used:
                    print("traslado # " + str(i) + " / " + str(link))
                else:
                    print("  used   # " + str(i) + " / " + str(link))
            i += 1
            if not link.used:
                link.used = True
                route = self.SearchCicleRecursive(link, link.base)
                if route is not None:
                    if DEBUG:
                        print("Conseguido")
                    route.append(link)
                    result.append(route)
                else:
                    if DEBUG:
                        print ("Muerto")
                    link.used = False
        return result

    def SearchCicleRecursive(self, link, start):

        newbase = link.to
        options = filter(lambda link: link.used == False, newbase.to)
        deadlinks = []
        for option in options:
            option.used = True
            if option.to == start:
                return [option]
            else:
                route = self.SearchCicleRecursive(option, start)
                if route is not None:
                    route.append(option)
                    for link in deadlinks:
                        link.used = False
                    return route
                else:
                    deadlinks.append(option)
        for link in deadlinks:
            link.used = False
        return None

    class Node:
        name = None
        to = None
        base = None

        def __init__(self, name):
            self.name = name
            self.to = SortedListWithKey(key=lambda item: item.priority)
            self.base = []

        def addTo(self, link):
            self.to.add(link)

        def addBase(self, link):
            self.base.append(link)

        def __str__(self):
            return self.name

        def str_full(self):
            String = str(self) + " #Links: " + str(len(self.to)) + "\n"
            for link in self.to:
                String += str(link) + "\n"
            return String

    class Link:
        base = None
        to = None
        priority = None
        used = None

        def __init__(self, base, to, priority):
            self.base = base
            self.to = to
            self.priority = priority
            self.used = False

        def __str__(self):
            return str(self.base) + " --> " + str(self.to) + " cost: " + str(self.priority)

    def __str__(self):
        String = "Nodes: \n"
        String += "-------------------\n"
        for node in self.nodes.values():
            String += node.str_full() + "\n"
        String += "-------------------\n"
        String += "Links: \n"
        String += "-------------------\n"
        for link in self.links:
            String += str(link) + "\n"
        return String

import csv



def parsefile(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader, None)
        nodes = set()
        links = list()
        for row in reader:
            nodes.add(row[1])
            nodes.add(row[2])
            links.append([row[1], row[2], int(row[0])])
        return nodes, links

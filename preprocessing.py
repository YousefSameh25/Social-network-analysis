import csv

#map = {"Family members" : 5 , "Friends" : 4 , "Romantic partners" : 3 , "Work Colleagues" : 2 , "Servant-Master" : 1}
map2 = {}
def readNodes (G , path):
    # Open the CSV file for reading
    with open(path,'r') as file:
        # Create a reader object to read the CSV file
        reader = csv.reader(file)
        next(reader)
        # Iterate over each row in the CSV file
        for row in reader:
            # Print the first value in the row
            G.add_node(row[0])
def readEdges (G , path):
    w = 1
    # Open the CSV file for reading
    with open(path , 'r') as file:
        # Create a reader object to read the CSV file
        reader = csv.reader(file)
        next(reader)
        # Iterate over each row in the CSV file
        for row in reader:
            # Print the first value in the row
            G.add_edge(row[0], row[1])
            # set the weight of the edge

            if len(row) > 2:
                if row[2] in map2:
                    G[row[0]][row[1]]['weight'] = map2[row[2]]
                else:
                    map2[row[2]] = w
                    w += 1
                    G[row[0]][row[1]]['weight'] = map2[row[2]]
            else:
                G[row[0]][row[1]]['weight'] = 1
    print(map2)

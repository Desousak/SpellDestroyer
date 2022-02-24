import json

MISSPELLINGS = {}
with open("misspell.dat", "r") as file:
    lines = file.readlines()
    
    curr_line = None
    for line in lines:
        line = line[:-1]
        if (line[0] == "$" or curr_line == None):
            curr_line = line[1:]
            MISSPELLINGS[curr_line] = []
        else:
            MISSPELLINGS[curr_line].append(line)

with open("missp.json", "w+") as file:
    json.dump(MISSPELLINGS, file)
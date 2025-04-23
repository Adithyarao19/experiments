def find_all_occurrences(name, char, start=0, positions=None):
    if positions is None:
        positions = []


    #basecase
    if start >= len(name):
        return positions

    #find next occurrences starting from "start"
    index = name.find(char, start)

    if index == -1:
        return positions

    positions.append(index)
    return find_all_occurrences(name,char,index +1,positions)

name= input(" enter your full name: ")
result = find_all_occurrences(name,"a")
print(" all position of 'a':", result)
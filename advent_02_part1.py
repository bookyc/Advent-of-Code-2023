RED = 12
GREEN = 13
BLUE = 14
def do_stuff(games) -> int:
    sum_id = 0
    for line in range(len(games)):
        valid_game = True
        gamessplit = games[line].split(": ")
        subsets = gamessplit[1].split("; ")

        for i in range(len(subsets)):
            instance = subsets[i].split(", ")
            
            for j in range(len(instance)):
                pull = instance[j].split()
                if pull[1] in "green":
                    if int(pull[0]) > GREEN:
                        valid_game = False
                elif pull[1] in "red":
                    if int(pull[0]) > RED:
                        valid_game = False
                else:
                    if int(pull[0]) > BLUE:
                        valid_game = False

        if valid_game:
            sum_id += (line+1)
    return sum_id
        
    

file = open("day_two_input.txt","r")
input = []
for line in file:
    input.append(line)
print(do_stuff(input))
file.close()
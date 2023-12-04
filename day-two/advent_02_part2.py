def do_stuff(games) -> int:
    sum_cubes = 0
    for line in range(len(games)):
        highest_red = 0
        highest_blue = 0
        highest_green = 0
        gamessplit = games[line].split(": ")
        subsets = gamessplit[1].split("; ")

        for i in range(len(subsets)):
            instance = subsets[i].split(", ")
            
            for j in range(len(instance)):
                pull = instance[j].split()
                if pull[1] in "green":
                    if int(pull[0]) > highest_green:
                        highest_green = int(pull[0])
                elif pull[1] in "red":
                    if int(pull[0]) > highest_red:
                        highest_red = int(pull[0])
                else:
                    if int(pull[0]) > highest_blue:
                        highest_blue = int(pull[0])

        sum_cubes += (highest_red * highest_green * highest_blue)
    return sum_cubes

file = open("day_two_input.txt","r")
input = []
for line in file:
    input.append(line)
print(do_stuff(input))
file.close()

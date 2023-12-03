def find_values(line: str) -> str:
    first_char = ["one","two","thr","fou","fiv","six","sev","eig","nin"]
    equivalncies = ["1","2","3","4","5","6","7","8","9"]
    for i in range(len(line)):
        if line[i].isdigit():
            num1 = line[i]
            break
        elif line[i:i+3] in first_char:
            for j in range(len(first_char)):
                if first_char[j] in line[i:i+3]:
                    num1 = equivalncies[j]
            break
        
    for i in range(len(line)):
        if line[i].isdigit():
            num2 = line[i]
        elif line[i:i+3] in first_char:
            for j in range(len(first_char)):
                if first_char[j] in line[i:i+3]:
                    num2 = equivalncies[j]

    return str(num1) + str(num2)
   

def sum_of_values(calibration_values: list[str]) -> int:
    sum = 0
    for i in calibration_values:
        sum += int(i)
    return sum

def main() -> None:
    input = open("day_one_input.txt", "r")
    calibration_values = []
    for i in input:
        calibration_values.append(find_values(i))

    print(sum_of_values(calibration_values))

    input.close()

main()

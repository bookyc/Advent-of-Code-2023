def find_values(line: str) -> str:
    for i in reversed(range(len(line))):
        if line[i].isdigit():
            num1 = line[i]
    for i in range(len(line)):
        if line[i].isdigit():
            num2 = line[i]
    return num1 + num2

def sum_of_values(calibration_values: list[str]) -> int:
    sum = 0
    for i in calibration_values:
        sum += int(i)
    return sum

def main() -> None:
    input = open("day-1/day_one_input.txt", "r")
    calibration_values = []
    for i in input:
        calibration_values.append(find_values(i))

    print(sum_of_values(calibration_values))
    input.close()

main()

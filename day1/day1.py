def convert_line_to_nums(line):
    string_num_dic = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for key in string_num_dic:
        index = line.find(key)
        if index >= 0:
            line = line[:index+1] + string_num_dic[key] + line[index+1:]
            line = convert_line_to_nums(line)
    return line

f = open("input", "r")
answer = 0
for line in f:
    line = convert_line_to_nums(line)
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(char)
    answer += int(numbers[0] + numbers[-1])
print(answer)

f = open("input", "r")
answer = 0
for line in f:
    dic = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    print("---")
    print(line)
    split1 = line.split(":")
    game_str_num = split1[0]
    game_info = split1[1]
    rounds = game_info.split(";")
    for round in rounds:
        pulls_info = round.split(",")
        for pull_info in pulls_info:
            num_part = int(pull_info.strip().split(" ")[0])
            color_part = pull_info.strip().split(" ")[1]
            print(pull_info)
            if color_part == "red" and num_part > dic["red"]:
                dic["red"] = num_part
            if color_part == "green" and num_part > dic["green"]:
                dic["green"] = num_part
            if color_part == "blue" and num_part > dic["blue"]:
                dic["blue"] = num_part
    game_math = 1
    for key in dic:
        game_math = game_math*dic[key]
            
    answer += game_math
print(answer)
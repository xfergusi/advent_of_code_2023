f = open("input", "r")
answer = 0
for line in f:
    possible = True
    print(line)
    split1 = line.split(":")
    game_str_num = split1[0]
    game_info = split1[1]
    rounds = game_info.split(";")
    for round in rounds:
        pulls_info = round.split(",")
        for pull_info in pulls_info:
            num_part = pull_info.trim().split(" ")[0]
            color_part = pull_info.trim().split(" ")[1]
            if color_part == "red" and num_part > 12:
                possible = False
            if color_part == "green" and num_part > 13:
                possible = False
            if color_part == "blue" and num_part > 14:
                possible = False
    if possible:
        answer += int(game_str_num.split(" ")[1])
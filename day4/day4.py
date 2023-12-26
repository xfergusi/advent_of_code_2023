def part1():
    f = open("input", "r")
    answer = 0
    for line in f:
        your_nums_list = line.split("|")[1].split()
        win_nums_list = line.split("|")[0].split(":")[1].split()
        print(your_nums_list)
        print(win_nums_list)
        line_winning_nums = 0
        for num in win_nums_list:
            if num in your_nums_list:
                line_winning_nums+=1
        line_winning_nums-=1
        if line_winning_nums != -1:
            answer += 2**line_winning_nums
            print(line_winning_nums)
            print(2**line_winning_nums)
        else: 
            print("no matching numbers")

    return answer

def part2():
    major_dic = {}
    f = open("input", "r")
    for line in f:
        game_num = int(line.split("|")[0].split(":")[0].split()[1])
        major_dic[game_num] = 1

    f = open("input", "r")
    answer = 0
    for line in f:
        your_nums_list = line.split("|")[1].split()
        win_nums_list = line.split("|")[0].split(":")[1].split()
        game_num = int(line.split("|")[0].split(":")[0].split()[1])

        line_winning_nums = 0
        for num in win_nums_list:
            if num in your_nums_list:
                line_winning_nums+=1
        
        for y in range(line_winning_nums):
            x = y+1
            print("x" + str(x))
            major_dic[game_num + x] = major_dic[game_num + x] + major_dic[game_num]

    for key in major_dic:
        answer += major_dic[key]
    print(major_dic)
    return answer
def main():
    # print("part 1 : {} ".format(part1()))
    print("part 2 : {} ".format(part2()))

if __name__ == "__main__":
    main()
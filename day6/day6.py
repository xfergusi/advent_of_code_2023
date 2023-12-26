def part1():
    f = open("input", "r")
    times = f.readline().split(":")[1].split()
    distances = f.readline().split(":")[1].split()
    max_boy = 0

    result_number_of_ways_to_win_list = []
    for distances_index, distance in enumerate(distances):
        distance = int(distance)
        time = int(times[distances_index])
        current_number_of_ways_to_win_list = 0
        for x in range(time):
            current_speed = x + 1
            total_travelled = current_speed * (time-current_speed)
            print("total amount : {}".format(total_travelled))
            if total_travelled > distance:
                current_number_of_ways_to_win_list += 1
        result_number_of_ways_to_win_list.append(current_number_of_ways_to_win_list)
        # if max_boy < distance:
        #     max_boy = distance
        print("---------------")
        # print(time)
        # print(time_index)

    print(result_number_of_ways_to_win_list)
    answer = 1
    for x in result_number_of_ways_to_win_list:
        answer *= x
    # for x in range(max_boy):
    #     pass
    return answer

def part2():
    pass

def main():
    print("part 1 : {} ".format(part1()))
    # print("part 2 : {} ".format(part2()))

if __name__ == "__main__":
    main()
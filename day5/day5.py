def part1():
    f = open("input", "r")
    first_line = f.readline()
    # print(first_line)
    seed_map = {}

    seed_list = first_line.split(":")[1].split()
    for x in seed_list:
        seed_map[x] = []
    
    seed_to_soil_map = {}
    soil_to_fertilizer_map = {}
    fertilizer_to_water_map = {}
    water_to_light_map = {}
    light_to_temperature_map = {}
    temperature_to_humidity_map = {}
    humidity_to_location_map = {}
    for line in f:
        if "map:" in line:
            we_reached_a_def_line_part_1(f, seed_map)

    answer = 1000000000
    for key in seed_map:
        if seed_map[key][-1] < answer:
            answer = seed_map[key][-1] 
    
    return answer

def we_reached_a_def_line_part_1(f, seed_map):
    numbers_list = []
    for numbers in f:
        if len(numbers) == 1 :
            break
        numbers_list.append(numbers)
    for key in seed_map:
        if len(seed_map[key]) == 0:
            input = int(key)
        else:
            input = seed_map[key][-1]
        seed_map[key].append(find_map_part_1(input, numbers_list))

def find_map_part_1(input, numbers_list_input):
    for numbers in numbers_list_input:
        numbers_list = numbers.split()
        destination_range_start = int(numbers_list[0])
        source_range_start = int(numbers_list[1])
        range_length = int(numbers_list[2])
        if input >= source_range_start and input <= source_range_start + range_length - 1:
            return (input - source_range_start + destination_range_start)
    return input

def part2():
    pass

def main():
    print("part 1 : {} ".format(part1()))
    print("part 2 : {} ".format(part2()))

if __name__ == "__main__":
    main()
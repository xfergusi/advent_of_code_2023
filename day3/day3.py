# def 

symbols=["/","#","=","*","@","%","-","+","$","&"]

f = open("input", "r")
answer = 0
grid = []
star_dic = {}
for line in f:
    grid.append(line)

for row_index, row in enumerate(grid):
    current_num = ""
    current_star_coor = ""
    touching_symb = False
    for char_index, char in enumerate(row):
        if char.isdigit():
            current_num += char
            print("currently working on {} at [{}][{}]".format(char, row_index, char_index))
            # check if number is touching symbol
            try:
                if grid[row_index-1][char_index-1] == "*":
                    current_star_coor = "{},{}".format(row_index-1,char_index-1)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
                elif grid[row_index-1][char_index] == "*":
                    current_star_coor = "{},{}".format(row_index-1,char_index)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
                elif grid[row_index-1][char_index+1] == "*":
                    current_star_coor = "{},{}".format(row_index-1,char_index+1)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
            except:
                pass
                # print("nothing above")
                
                
            try:
                if grid[row_index][char_index-1] == "*":
                    current_star_coor = "{},{}".format(row_index,char_index-1)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
            except:
                pass
                # print("nothing left")
            
            try:
                if grid[row_index][char_index+1] == "*":
                    current_star_coor = "{},{}".format(row_index,char_index+1)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
            except:
                # print("nothing right")
                pass
            
            try:
                if grid[row_index+1][char_index-1] == "*":
                    current_star_coor = "{},{}".format(row_index+1,char_index-1)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
                if grid[row_index+1][char_index] == "*":
                    current_star_coor = "{},{}".format(row_index+1,char_index)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
                if grid[row_index+1][char_index+1] == "*":
                    current_star_coor = "{},{}".format(row_index+1,char_index+1)
                    touching_symb = True
                    print("found star at {}".format(current_star_coor))
            except:
                pass
                # print("nothing below")
        else:
            if current_num != "" and touching_symb:
                if current_star_coor in star_dic:
                    star_dic[current_star_coor].append(current_num)
                else:
                    print("current num = " + current_num)
                    star_dic[current_star_coor] = [current_num]
            current_star_coor = ""
            current_num = ""
            touching_symb = False
for key in star_dic:
    if len(star_dic[key]) == 2:
        answer += int(star_dic[key][0]) * int(star_dic[key][1])
        # print("star to check: {}".format(key))

print(answer)
# print(star_dic)
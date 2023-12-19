# def 

symbols=["/","#","=","*","@","%","-","+","$","&"]

f = open("input", "r")
answer = 0
grid = []
for line in f:
    grid.append(line)

for row_index, row in enumerate(grid):
    current_num = ""
    touching_symb = False
    for char_index, char in enumerate(row):
        if char.isdigit():
            current_num += char
            print("currently working on {} at [{}][{}]".format(char, row_index, char_index))
            # check if number is touching symbol
            try:
                if grid[row_index-1][char_index-1] in symbols:
                    touching_symb = True
                elif grid[row_index-1][char_index] in symbols:
                    touching_symb = True
                elif grid[row_index-1][char_index+1] in symbols:
                    touching_symb = True
            except:
                print("nothing above")
                
            try:
                if grid[row_index][char_index-1] in symbols:
                    touching_symb = True
            except:
                print("nothing left")
            
            try:
                if grid[row_index][char_index+1] in symbols:
                    touching_symb = True
            except:
                print("nothing right")
            
            try:
                if grid[row_index+1][char_index-1] in symbols:
                    touching_symb = True
                if grid[row_index+1][char_index] in symbols:
                    touching_symb = True
                if grid[row_index+1][char_index+1] in symbols:
                    touching_symb = True
            except:
                print("nothing below")
        else:
            if not current_num == "" and touching_symb:
                answer += int(current_num)
            current_num = ""
            touching_symb = False

print(answer)
    



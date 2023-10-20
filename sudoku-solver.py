board = [

    [0,0,7,9,0,0,0,0,4],
    [0,0,0,3,0,7,0,6,0],
    [3,4,1,6,0,0,9,2,7],
    [0,3,0,0,0,0,2,0,1],
    [0,0,8,2,0,5,6,0,0],
    [9,0,6,0,0,0,0,3,0],
    [4,1,2,0,0,3,7,9,6],
    [0,9,0,1,0,2,0,0,0],
    [7,0,0,0,0,9,5,0,0]

]

# the most confusing of all: the recursive function
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True # we finished! There are no more empty squares
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # this is the horrible recursion bit: continuously tries to use solve until no empty spaces
            if solve(bo):
                return True # breaks out, otherwise it's 0

            # backtracking and resetting to 0
            bo[row][col] = 0

    return False

def valid(bo, num, pos):

    # check row - pos is (i,j) so pos[0] is i and pos[1] is j
    for j in range(len(bo[0])):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box (div 3 and no remainder is the first box, so 0)
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False # this is counterintuitive, if we find the same number as we input (num) then it cannot fit and is False

    return True # we couldn't find it? Then let's try it!

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # end avoids the /n being added for a new row

            if j == 8:
                print(bo[i][j]) # this creates a new line after the last number in the row

            else:
                print(str(bo[i][j]) + " ", end="")

# print_board(board) # to select all instances of the same word is "CMD" + "D"

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row then column

    return None # if there are no blank squares, return False which triggers recursion


####################################
# testing it out

print_board(board)
solve(board)
print("---------------------------")
print_board(board)

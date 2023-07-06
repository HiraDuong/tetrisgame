square_size = 30
# 1 is I, 2 is J, 3 is L, 4 is O , 5 is S, 6 is T, 7 is Z 

 # Tạo một canvas widget với kích thước phù hợp
canvas_width = 10 * square_size
canvas_height = 20* square_size

global Mat_game
global Mat_menu
Mat_game = [[0]*10 for _ in range(20)]
Mat_menu = [[0]*10 for _ in range(20)]
#display next block area
for x in range(2, 8):
    for y in range(2, 8):
        Mat_menu[x][y] = 1
# btn areas 
for x in range(1, 3):
    for y in range(12, 14):
        Mat_menu[y][x] = 2
for x in range(4, 6):
    for y in range(12, 14):
        Mat_menu[y][x] = 2
for x in range(7, 9):
    for y in range(12, 14):
        Mat_menu[y][x] = 2
for x in range(4, 6):
    for y in range(15, 17):
        Mat_menu[y][x] = 2

blocks = {
# I block
'I' :[[0,0,0,0],
 [1,1,1,1]],
# J block 
'J':[[2,0,0],
 [2,2,2]],
# L block
'L':[[0,0,3],
 [3,3,3]],
# O block
'O':[[4,4],
 [4,4]],
# S block
'S':[[0,5,5],
 [5,5,0]],
# T block
'T':[[0,6,0],
 [6,6,6]],
#Z block
'Z':[[7,7,0],
 [0,7,7]]
}


block_keyss = blocks.keys()
block_keys = list(block_keyss)
print(block_keys)
print(type(block_keys))
print(block_keys[1])


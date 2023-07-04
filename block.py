square_size = 30
# 1 is I, 2 is J, 3 is L, 4 is O , 5 is S, 6 is T, 7 is Z 

 # Tạo một canvas widget với kích thước phù hợp
canvas_width = 10 * square_size
canvas_height = 20* square_size

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


block_keys = blocks.keys()
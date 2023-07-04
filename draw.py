import tkinter as tk
from block import * 


colors ={'I':'#10e6ad','J' : 'blue', 'L':'#FF8B64','O': '#FFFF00', 'S':'#7CFC00','T':'#9400D3','Z':'#FF0000' }
class Draw:
    def __init__(self) :
        pass
    
    def draw_mat(self,screen,Mat_game):
        canvas = tk.Canvas(screen, width=canvas_width, height=canvas_height,highlightthickness=0)
        canvas.grid(row=0,column=0)

        # Vẽ từng hình vuông dựa trên ma trận Mat_game
        for i in range(len(Mat_game)):
            for j in range(len(Mat_game[i])):
                x = j * square_size
                y = i * square_size
                if (Mat_game[i][j] <= 0):    
                    canvas.create_rectangle(x, y, x + square_size, y + square_size, fill="white")
                else:
                    index = Mat_game[i][j]
                    #key_block = block_keys[index-1]
                    #color = colors[key_block]
                    canvas.create_rectangle(x, y, x + square_size, y + square_size, fill="red")
       

    def draw_menu(self,screen,Mat_menu,key_block):
        canvas = tk.Canvas(screen, width=canvas_width, height=canvas_height,highlightthickness=0)
        canvas.grid(row=0,column=10)

        # Vẽ từng hình vuông dựa trên ma trận Mat_game
        for i in range(len(Mat_menu)):
            for j in range(len(Mat_menu[i])):
                x = j * square_size
                y = i * square_size
                if Mat_menu[i][j] == 1:
                    canvas.create_rectangle(x, y, x + square_size, y + square_size, fill="white")
                else:
                    canvas.create_rectangle(x, y, x + square_size, y + square_size, fill="green")
        block = blocks[key_block]
        color = colors[key_block]
        for i in range(len(block)):
            for j in range(len(block[0])):
                if len(block[0] )%2 ==1:
                    x = (j+3.5)* square_size
                    y = (i+4) *square_size
                elif block == blocks['I']:
                    x = (j+3)* square_size
                    y = (i+3.5) *square_size
                else:
                    x = (j+4)* square_size
                    y = (i+4) *square_size
                if (block[i][j] !=0):
                    canvas.create_rectangle(x, y, x + square_size, y + square_size, fill=color)
      

 
                
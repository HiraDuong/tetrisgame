
import tkinter as tk
from block import *
from draw import Draw
import random as rd
import time

global Mat_game
global Mat_menu
Mat_game = [[0]*10 for _ in range(20)]
Old_Mat = Mat_game
Mat_menu = [[0]*10 for _ in range(20)]
for x in range(2, 8):
    for y in range(2, 8):
        Mat_menu[x][y] = 1
        
current_time = int(time.time())
rd.seed(int(current_time)/31415.962458)

class Screen:
    def __init__(self):
        self.dr = Draw()
        
    # for row in Mat_game:
    #     print(row)

    # screen
    def run(self):
        def updateMat(key_block,move):
            block = blocks[key_block]
            for i in range(0,len(block)):
                for j in range(0,len(block[0])):
                    Mat_game[i][4+j] = block[i][j]
           
          
                  
        dr = self.dr
        
    # Tạo một cửa sổ gốc
        root = tk.Tk()

        # Thiết lập tiêu đề cho cửa sổ
        root.title("Tetris game")

        # Thiết lập kích thước cho cửa sổ
        root.geometry("600x600")
        
        ran_key = rd.choice(list(block_keys))
        y = -1
        x = 4
        while True:
            dr.draw_mat(root,Mat_game)
            #updateMat(ran_key,x,y)
            #move down 
            #start

            block = blocks[ran_key]
            for i in range(0,len(block)):
                for j in range(0,len(block[0])):
                    Mat_game[y+i][x+j] = block[i][j]
            #move down 
            v = 1
            if y<10 and:
                for i in range(0,len(block)):
                    for j in range(0,len(block[0])):
                        Mat_game[y+i][x+j] = 0
                y+=v
                for i in range(0,len(block)):
                    for j in range(0,len(block[0])):
                        Mat_game[y+i][x+j] = block[i][j]
            else:
                #new block
                x=4
                y =-1
                ran_key = rd.choice(list(block_keys))

            #        
            #print(ran_key)
            dr.draw_menu(root,Mat_menu,ran_key)
            root.update()
            time.sleep(1)

        # Hiển thị cửa sổ
        root.mainloop()

run = Screen()
run.run()
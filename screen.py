
import tkinter as tk
from block import *
from draw import Draw
import random as rd
import time


current_time = int(time.time())
rd.seed(int(current_time)/31415.962458)

class Screen:
    def __init__(self):
        self.dr = Draw()
        
    # for row in Mat_game:
    #     print(row)

    # screen
    
    def run(self):
        y = -1
        x = 4
        vy = 1
        vx = 1
        v = 1
        def updateMat(key_block,move):
            block = blocks[key_block]
            for i in range(0,len(block)):
                for j in range(0,len(block[0])):
                    Mat_game[i][4+j] = block[i][j]
        def check(block):
            m = len(block)
            n = len(block[0])
            for i in range(m):
                for j in range(n):
                    if block[i][j] !=0:
                        if Mat_game[y+i+v][x+j+v] + block[i][j] > block[i][j]:
                            return True
            return False

                    

        dr = self.dr
        
    # Tạo một cửa sổ gốc
        root = tk.Tk()

        # Thiết lập tiêu đề cho cửa sổ
        root.title("Tetris game")

        # Thiết lập kích thước cho cửa sổ
        root.geometry("600x600")
        
        ran_key = rd.choice(list(block_keys))
        ran_key_next = rd.choice(list(block_keys))
      
        while True:
            dr.draw_mat(root,Mat_game)
            #updateMat(ran_key,x,y)
            #move down 
            #start
            
            block = blocks[ran_key]
            #block_cp = block
            m = len(block)
            n = len(block[0])
            # change coppy block is 10 for check map
            
            # start block in map
            for i in range(m):
                for j in range(n):
                    Mat_game[y+i+v][x+j] = block[i][j]
            if y < 10:
                if True:
                    for i in range(m):
                        for j in range(n):
                            Mat_game[y+i+v][x+j] =0
                    y+=v
                    for i in range(m):
                        for j in range(n):
                            Mat_game[y+i+v][x+j] = block[i][j]
            else :
                y = -1
                x = 4
                ran_key = rd.choice(list(block_keys))
                ran_key_next = rd.choice(list(block_keys))
                   
            #print(ran_key)
            dr.draw_menu(root,Mat_menu,ran_key_next)
            root.update()
            time.sleep(0.5)

        # Hiển thị cửa sổ
        root.mainloop()

# run = Screen()
# run.run()
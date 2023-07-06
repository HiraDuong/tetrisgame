
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
   
    def check_collision(self,block):
        
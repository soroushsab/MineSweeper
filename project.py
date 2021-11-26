
from tkinter import *
from tkinter import messagebox as tkMessageBox
import random
from typing import Counter

class Mine():
    #-------------------------------------------------------------------------#
    def __init__(self):
        ##########################################################
        # define the main root
        self.root = Tk()
        # set title
        self.root.title('Soroush Minesweeper!')
        # set size and position
        w = 400
        h = 200
        self.root.geometry(self.set_size_and_positions(h,w))
        ##########################################################
        # define a frame for labels
        self.frame_lbls = Frame(self.root)
        # pack the frame
        self.frame_lbls.pack()
        # set a list of label for information
        self.lbls_info = {
            'title' : Label(self.frame_lbls, text='Soroush Minesweeper'),
            'welcome' : Label(self.frame_lbls, text='Welcome!')
        }
        # set a position for them
        self.lbls_info["title"].grid(row = 0, column = 0)
        self.lbls_info["welcome"].grid(row = 1, column = 0)
        ##########################################################
        # define a frame for buttons
        self.frame_btns = Frame(self.root)
        # pack the frame
        self.frame_btns.pack()
        # set a list of button for levels
        self.btns_lvls = {
            'easy' : Button(self.frame_btns, text='Easy', command= lambda: self.easy_game()),
            'normal' : Button(self.frame_btns, text='Normal'),
            'hard' : Button(self.frame_btns, text='Hard')
        }
        # set a position for them
        self.btns_lvls["easy"].grid(row = 0, column = 0)
        self.btns_lvls["normal"].grid(row = 0, column = 1)
        self.btns_lvls["hard"].grid(row = 0, column = 2)
        ##########################################################
        # define images
        self.images = {
            "logo": PhotoImage(file = "images/logo.gif")
        }
        ##########################################################
        # define a frame for logo and close button
        self.frame_end = Frame(self.root)
        # pack the frame
        self.frame_end.pack()
        # set a list of button for levels
        self.btn_and_lbl_ends = {
            'logo' : Label(self.frame_end, image=self.images['logo']),
            'close' : Button(self.frame_end, text='Close',command= lambda: self.close_program())
        }
        # set a position for them
        self.btn_and_lbl_ends["logo"].grid(row = 0, column = 0)
        self.btn_and_lbl_ends["close"].grid(row = 1, column = 0)
        ##########################################################

        ##########################################################
        ##########################################################
        ##########################################################
        ##########################################################
        self.root.mainloop()
    #-------------------------------------------------------------------------#
    def openOthers_inzero(self,btn):
        x = btn['x']
        y = btn['y']
        btn['state'] = '+'
        btn['btn'].config(text=str(btn['num']),bg='yellow')
        if x - 1 >= 0 and y - 1 >= 0: # check top left
            if self.btns[x-1][y-1]['state'] != '+':
                self.btns[x-1][y-1]['state'] = '+'
                self.btns[x-1][y-1]['btn'].config(text=str(self.btns[x-1][y-1]['num']),bg='yellow')
                if self.btns[x-1][y-1]['num'] == 0:
                    self.openOthers_inzero(self.btns[x-1][y-1])
        if y - 1 >= 0: # check top
            if self.btns[x][y-1]['state'] != '+':
                self.btns[x][y-1]['state'] = '+'
                self.btns[x][y-1]['btn'].config(text=str(self.btns[x][y-1]['num']),bg='yellow')
                if self.btns[x][y-1]['num'] == 0:
                    self.openOthers_inzero(self.btns[x][y-1])
        if x + 1 < self.size and y - 1 >= 0: # check top right
            if self.btns[x+1][y-1]['state'] != '+':
                self.btns[x+1][y-1]['state'] = '+'
                self.btns[x+1][y-1]['btn'].config(text=str(self.btns[x+1][y-1]['num']),bg='yellow')
                if self.btns[x+1][y-1]['num'] == 0:
                    self.openOthers_inzero(self.btns[x+1][y-1])
        if x - 1 >= 0: # check left
            if self.btns[x-1][y]['state'] != '+':
                self.btns[x-1][y]['state'] = '+'
                self.btns[x-1][y]['btn'].config(text=str(self.btns[x-1][y]['num']),bg='yellow')
                if self.btns[x-1][y]['num'] == 0:
                    self.openOthers_inzero(self.btns[x-1][y])
        if x + 1 < self.size: # check right
            if self.btns[x+1][y]['state'] != '+':
                self.btns[x+1][y]['state'] = '+'
                self.btns[x+1][y]['btn'].config(text=str(self.btns[x+1][y]['num']),bg='yellow')
                if self.btns[x+1][y]['num'] == 0:
                    self.openOthers_inzero(self.btns[x+1][y])
        if x - 1 >= 0 and y + 1 < self.size: # check bottom left
            if self.btns[x-1][y+1]['state'] != '+':
                self.btns[x-1][y+1]['state'] = '+'
                self.btns[x-1][y+1]['btn'].config(text=str(self.btns[x-1][y+1]['num']),bg='yellow')
                if self.btns[x-1][y+1]['num'] == 0:
                    self.openOthers_inzero(self.btns[x-1][y+1])
        if y + 1 < self.size: # check bottom
            if self.btns[x][y+1]['state'] != '+':
                self.btns[x][y+1]['state'] = '+'
                self.btns[x][y+1]['btn'].config(text=str(self.btns[x][y+1]['num']),bg='yellow')
                if self.btns[x][y+1]['num'] == 0:
                    self.openOthers_inzero(self.btns[x][y+1])
        if x + 1 < self.size and y + 1 < self.size: # check bottom right
            if self.btns[x+1][y+1]['state'] != '+':
                self.btns[x+1][y+1]['state'] = '+'
                self.btns[x+1][y+1]['btn'].config(text=str(self.btns[x+1][y+1]['num']),bg='yellow')
                if self.btns[x+1][y+1]['num'] == 0:
                    self.openOthers_inzero(self.btns[x+1][y+1])
    #-------------------------------------------------------------------------#
    def showAllMines(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.btns[i][j]['checkMine']:
                    self.btns[i][j]['btn'].config(text = '*',bg='orange')
    #-------------------------------------------------------------------------#
    def user_lose(self):
        res = tkMessageBox.askyesno("Game Over", 'You Lose! Play again?')
    #-------------------------------------------------------------------------#
    def set_size_and_positions(self,h,w):
        hs = self.root.winfo_screenheight()
        ws = self.root.winfo_screenwidth()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        return '%dx%d+%d+%d' % (w, h, x, y)
    #-------------------------------------------------------------------------#
    def right_click(self,i,j):
        return lambda Button: self.right_click_0(self.btns[i][j])
    #-------------------------------------------------------------------------#
    def right_click_0(self,btn):
        if self.mines_no > 0 and btn['state'] == 'O':
            btn['btn'].config(text='P')
            btn['state'] = 'P'
            self.mines_no -= 1
        elif btn['state'] == 'P':
            btn['btn'].config(text=' ')
            btn['state'] = 'O'
            self.mines_no += 1
        else:
            pass
    #-------------------------------------------------------------------------#
    def left_click(self,i,j):
        return lambda Button: self.left_click_0(self.btns[i][j])
    #-------------------------------------------------------------------------#
    def left_click_0(self,btn):
        if btn['state'] == 'P':
            pass
        elif btn['checkMine']:
            self.showAllMines()
            btn['btn'].config(bg='red')
            self.user_lose()
        elif btn['state'] == 'O':
            if btn['num'] == 0:
                self.openOthers_inzero(btn)
            else:
                btn['state'] = '+'
                btn['btn'].config(text=str(btn['num']),bg='yellow')
            
    #-------------------------------------------------------------------------#
    def set_numbers_for_btns(self):
        mines = 0
        for x in range(self.size):
            for y in range(self.size):
                if not self.btns[x][y]['checkMine']:
                    mines = 0
                    # check 8 neighboors
                    if x - 1 >= 0 and y - 1 >= 0: # check top left
                        if self.btns[x-1][y-1]['checkMine']:
                            mines += 1
                    if y - 1 >= 0: # check top
                        if self.btns[x][y-1]['checkMine']:
                            mines += 1
                    if x + 1 < self.size and y - 1 >= 0: # check top right
                        if self.btns[x+1][y-1]['checkMine']:
                            mines += 1
                    if x - 1 >= 0: # check left
                        if self.btns[x-1][y]['checkMine']:
                            mines += 1
                    if x + 1 < self.size: # check right
                        if self.btns[x+1][y]['checkMine']:
                            mines += 1
                    if x - 1 >= 0 and y + 1 < self.size: # check bottom left
                        if self.btns[x-1][y+1]['checkMine']:
                            mines += 1
                    if y + 1 < self.size: # check bottom
                        if self.btns[x][y+1]['checkMine']:
                            mines += 1
                    if x + 1 < self.size and y + 1 < self.size: # check bottom right
                        if self.btns[x+1][y+1]['checkMine']:
                            mines += 1
                    self.btns[x][y]['num'] = mines
    #-------------------------------------------------------------------------#
    def easy_game(self):
        ##########################################################
        # define the main root for easy game
        self.close_program()
        self.root = Tk()
        # set title
        self.root.title('Soroush Minesweeper!')
        # set size and position
        w = 400
        h = 400
        self.root.geometry(self.set_size_and_positions(h,w))
        ##########################################################
        # define a frame for timer and buttons
        self.first_frame = Frame(self.root)
        # pack the frame
        self.first_frame.pack()
        # set a list of label for information
        self.first_frame_set = {
            'timer' : Label(self.first_frame, text='text'),
            'back' : Button(self.first_frame, text='Back to menu'),
            'close' : Button(self.first_frame, text='Close',command= lambda: self.close_program()),
            'reset' : Button(self.first_frame, text='Reset')
        }
        # set a position for them
        self.first_frame_set["close"].grid(row = 1, column = 3)
        self.first_frame_set["back"].grid(row = 1, column = 1)
        self.first_frame_set["reset"].grid(row = 1, column = 0)
        self.first_frame_set["timer"].grid(row = 0, column = 0)
        ##########################################################
        # define another frame for game
        self.game_frame = Frame(self.root)
        # pack the frame
        self.game_frame.pack()
        # define a dictionary to set all buttons on it and set some property as well
        self.btns = dict({})
        # size of the board
        self.size = 9
        # define the number of mines in the game
        self.mines_no = 10
        list_of_mines = self.get_random_mine(self.mines_no,self.size)
        for i in range(self.size):
            for j in range(self.size):
                # at the beginning of each loop we have to define another dimension
                if j == 0 : # the first interation
                    self.btns[i] = {}
                # select randomly for mines
                checkMine = False
                if [i,j] in list_of_mines:
                    checkMine = True
                
                btn = {
                    'index' : str(i)+','+str(j),
                    'checkMine' : checkMine,
                    'state' : 'O',
                    'num' : 0,
                    'x' : i,
                    'y' : j,
                    'btn' : Button(self.game_frame,text='#',bg='white')
                }

                btn['btn'].bind('<Button-1>', self.left_click(i,j))
                btn['btn'].bind('<Button-3>', self.right_click(i,j))
                btn["btn"].grid( row = i+1, column = j )
                
                self.btns[i][j] = btn
        self.set_numbers_for_btns()
                
        ##########################################################

        ##########################################################
        ##########################################################
        ##########################################################
    #-------------------------------------------------------------------------#
    def get_random_mine(self,Mine,size):
        l = []
        for i in range(Mine):
            r = random.randrange(size*size)
            y = 0
            x = 0
            while r > size-1:
                r -= size
                x = r
                y += 1
            if [x,y] not in l:
                l.append([x,y])
            else:
                i -= 1
        return l 
    #-------------------------------------------------------------------------#
    def close_program(self):
        self.root.destroy()
    #-------------------------------------------------------------------------#
        

m = Mine()
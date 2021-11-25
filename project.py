
from tkinter import *

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
    def set_size_and_positions(self,h,w):
        hs = self.root.winfo_screenheight()
        ws = self.root.winfo_screenwidth()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        return '%dx%d+%d+%d' % (w, h, x, y)
    #-------------------------------------------------------------------------#
    def right_click_0(self,i,j):
        return lambda Button: self.right_click(self.btns[x][y])
    #-------------------------------------------------------------------------#
    def right_click(self,i,j):
        pass
    #-------------------------------------------------------------------------#
    def easy_game(self):
        ##########################################################
        # define the main root for easy game
        self.root = Tk()
        # set title
        self.root.title('Soroush Minesweeper!')
        # set size and position
        w = 400
        h = 400
        self.root.geometry(self.set_size_and_positions(h,w))
        ##########################################################
        # define some frames for timer and buttons
        self.first_frame = Frame(self.root)
        self.first_frame_1 = Frame(self.first_frame)
        self.first_frame_2 = Frame(self.first_frame)
        # pack the frame
        self.first_frame.pack()
        self.first_frame_1.pack(side='left')
        self.first_frame_2.pack(side='left')
        # set a list of label for information
        self.first_frame_set = {
            'timer' : Label(self.first_frame_1, text='text'),
            'back' : Button(self.first_frame_2, text='Back to menu'),
            'reset' : Button(self.first_frame_2, text='Reset')
        }
        # set a position for them
        self.first_frame_set["back"].grid(row = 0, column = 0)
        self.first_frame_set["reset"].grid(row = 1, column = 0)
        self.first_frame_set["timer"].grid(row = 0, column = 0)
        ##########################################################
        ##########################################################

        ##########################################################
        ##########################################################
        ##########################################################
    #-------------------------------------------------------------------------#
    def close_program(self):
        self.root.destroy()
    #-------------------------------------------------------------------------#
        

m = Mine()
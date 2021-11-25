
from tkinter import *

class Mine():
    def __init__(self,ch = ""):
        
        if ch != "":
            ch.destroy()
        self.root = Tk()
        self.root.title('Minesweeper')
        
        self.w_root = 400
        self.h_root = 400
        
        self.root.geometry('%dx%d+%d+%d' % (self.w_root, self.h_root, 
                                       ((self.root.winfo_screenwidth()/2)-(self.w_root/2))
                                       , ((self.root.winfo_screenheight()/2)-(self.h_root/2))))
        
        self.lbl_title = Label(self.root,text='Wellcome to Soroush made game!').place(x = 110,y = 25)
        self.lbl_lvl_selection = Label(self.root,text='Please select level of game you want to do: ').place(x = 90,y = 75)
        
        self.btn_easy = Button(self.root, text = "Easy!",command=lambda: self.easy_game()).place(x = 120, y = 100)
        self.btn_normal = Button(self.root, text = "Normal!",command=lambda: self.normal_game()).place(x = 170, y = 100)
        self.btn_hard = Button(self.root, text = "Hard!",command=lambda: self.hard_game()).place(x = 235, y = 100)
        
        self.btn_close = Button(self.root, text = "Close",command=lambda: self.close_program()).place(x = self.w_root - 50, y = self.h_root - 50)
        
        self.root.mainloop()

    def right_click(self,i,j):
        self.btns_text[i][j].set('P')

    def easy_game(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title('Minesweeper')
        
        self.w_root = 300
        self.h_root = 400
        
        self.root.geometry('%dx%d+%d+%d' % (self.w_root, self.h_root, 
                                       ((self.root.winfo_screenwidth()/2)-(self.w_root/2))
                                       , ((self.root.winfo_screenheight()/2)-(self.h_root/2))))

        
        self.lbl_title = Label(self.root,text='Easy!')

        self.btn_reset = Button(self.root, text = "Reset!",command=lambda: self.easy_game())

        self.btn_back = Button(self.root, text = "Back!",command=lambda: self.__init__(self.root))
        
        self.score = StringVar()
        self.score.set("0")
        
        self.lbl_score_text = Label(self.root,text="Your score: ")
        self.lbl_score = Label(self.root,textvariable= self.score)
        
        self.n_table = 10
        
        self.btns_text = [[StringVar()]*self.n_table]*self.n_table
        self.btns_game = [[0]*self.n_table]*self.n_table

        self.frame_grides = Frame(self.root)

        for i in range(self.n_table):
            for j in range(self.n_table):
                self.btns_text[i][j].set("O")
                self.btns_game[i][j] = Button(self.frame_grides, textvariable= self.btns_text[i][j])
                self.btns_game[i][j].bind("<Button-3>",self.right_click(i,j))
                self.btns_game[i][j].grid(row=i,column=j)
                # self.btns_game[i][j].place(x = 50 + i*20, y = 70 + j*20)

        self.root.focus_set()
        self.lbl_title.place(x = 10,y = 10)
        self.btn_reset.place(x = self.w_root - 50, y = 10)
        self.btn_back.place(x = self.w_root - 100, y = 10)
        self.lbl_score_text.place(x = 70,y = 10)
        self.lbl_score.place(x = 130,y = 10)
        self.frame_grides.place(x = 50,y = 70)

        # for i in range(self.n_table):
        #     for j in range(self.n_table):
        #         self.btns_game[i][j].place(x = 50 + i*20, y = 70 + j*20)


        self.root.mainloop()

    
    def normal_game(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title('Minesweeper')
        
        self.w_root = 450
        self.h_root = 450
        
        self.root.geometry('%dx%d+%d+%d' % (self.w_root, self.h_root, 
                                       ((self.root.winfo_screenwidth()/2)-(self.w_root/2))
                                       , ((self.root.winfo_screenheight()/2)-(self.h_root/2))))
        
        self.lbl_title = Label(self.root,text='Normal!').place(x = 10,y = 10)
    
        self.btn_reset = Button(self.root, text = "Reset!",command=lambda: self.normal_game()).place(x = self.w_root - 50, y = 10)
        
        self.btn_back = Button(self.root, text = "Back!",command=lambda: self.__init__(self.root)).place(x = self.w_root - 100, y = 10)
        
        self.score = 0
            
        self.lbl_title = Label(self.root,text='Your score: '+str(self.score)).place(x = 70,y = 10)
        
        self.n_table = 17
        
        self.b = [[0]*self.n_table]*self.n_table
        for i in range(self.n_table):
            for j in range(self.n_table):
                self.b[i][j] = Button(self.root, text = "#").place(x = 50 + i*20, y = 70 + j*20)
    
    def hard_game(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title('Minesweeper')
        
        self.w_root = 600
        self.h_root = 600
        
        self.root.geometry('%dx%d+%d+%d' % (self.w_root, self.h_root, 
                                       ((self.root.winfo_screenwidth()/2)-(self.w_root/2))
                                       , ((self.root.winfo_screenheight()/2)-(self.h_root/2))))
        
        self.lbl_title = Label(self.root,text='Hard!').place(x = 10,y = 10)
    
        self.btn_reset = Button(self.root, text = "Reset!",command=lambda: self.hard_game()).place(x = self.w_root - 50, y = 10)
        
        self.btn_back = Button(self.root, text = "Back!",command=lambda: self.__init__(self.root)).place(x = self.w_root - 100, y = 10)
        
        self.score = 0
            
        self.lbl_title = Label(self.root,text='Your score: '+str(self.score)).place(x = 70,y = 10)
        
        self.n_table = 25
        
        self.b = [[0]*self.n_table]*self.n_table
        for i in range(self.n_table):
            for j in range(self.n_table):
                self.b[i][j] = Button(self.root, text = "#").place(x = 50 + i*20, y = 70 + j*20)
    
        
        
    def close_program(self):
        self.root.destroy()
        
        

m = Mine()
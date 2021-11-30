
from tkinter import *
from tkinter import messagebox as tkMessageBox
import random
from datetime import datetime

class Mine():
    #-------------------------------------------------------------------------#
    def __init__(self):
        try:
            ##########################################################
            # define the main root
            self.root = Tk()
            # set title
            self.root.title('Soroush Minesweeper!')
            self.root.config(bg='white')
            self.root.eval('tk::PlaceWindow . center')
            ##########################################################
            self.records = []
            try:
                with open('saved_records.txt','r') as f:
                    for row in f:
                        self.records.append(row.split('%-%')[:-1])
                f.close
            except:
                print('no file')
            self.records = sorted(self.records,key=lambda x: (x[1]))
            ##########################################################
            # define a frame for labels
            self.frame_lbls = Frame(self.root,bg='white')
            # pack the frame
            self.frame_lbls.pack()
            # set a list of label for information
            self.lbls_info = {
                'title' : Label(self.frame_lbls, text='Soroush Minesweeper',bg='white'),
                'welcome' : Label(self.frame_lbls, text='Welcome!',bg='white')
            }
            # set a position for them
            self.lbls_info["title"].grid(row = 0, column = 0)
            self.lbls_info["welcome"].grid(row = 1, column = 0)
            ##########################################################
            # define a frame for buttons
            self.frame_btns = Frame(self.root,bg='white')
            # pack the frame
            self.frame_btns.pack()
            # set a list of button for levels
            self.btns_lvls = {
                'easy' : Button(self.frame_btns, text='Easy',bg='white', command= lambda: self.get_name_to_save('easy')),
                'normal' : Button(self.frame_btns, text='Normal',bg='white',command= lambda: self.get_name_to_save('normal')),
                'hard' : Button(self.frame_btns, text='Hard',bg='white',command= lambda: self.get_name_to_save('hard')),
                'computer' : Button(self.frame_btns, text='Computer Play',bg='white',command= lambda: self.computer_play('beginner'))
            }
            # set a position for them
            self.btns_lvls["easy"].grid(row = 0, column = 0)
            self.btns_lvls["normal"].grid(row = 0, column = 1)
            self.btns_lvls["hard"].grid(row = 0, column = 2)
            self.btns_lvls["computer"].grid(row = 0, column = 3)
            ##########################################################
            # define a frame for custom
            self.frame_btns_2 = Frame(self.root,bg='white')
            self.frame_btns_3 = Frame(self.root,bg='white')
            # pack the frame
            self.frame_btns_2.pack()
            self.frame_btns_3.pack()
            # three varoables for dimentions and mine number
            self.get_size_for_custom_x = StringVar()
            self.get_size_for_custom_y = StringVar()
            self.get_mine_for_custom = StringVar()
            # set a list of button for levels
            self.all_custom = {
                'x_lbl' : Label(self.frame_btns_2, text='Enter rows :',bg='white'),
                'x' : Entry(self.frame_btns_2, textvariable=self.get_size_for_custom_x,bg='white'),
                'y_lbl' : Label(self.frame_btns_2, text='Enter columns :',bg='white'),
                'y' : Entry(self.frame_btns_2, textvariable=self.get_size_for_custom_y,bg='white'),
                'mine_lbl' : Label(self.frame_btns_2, text='Enter number of Mines :',bg='white'),
                'mine' : Entry(self.frame_btns_2, textvariable=self.get_mine_for_custom,bg='white'),
                'custom' : Button(self.frame_btns_3, text='Custom',bg='white',command= lambda: self.get_name_to_save('custom'))
            }
            # set a position for them
            self.all_custom["x_lbl"].grid(row = 0, column = 0)
            self.all_custom["x"].grid(row = 0, column = 1)
            self.all_custom["y_lbl"].grid(row = 1, column = 0)
            self.all_custom["y"].grid(row = 1, column = 1)
            self.all_custom["mine_lbl"].grid(row = 2, column = 0)
            self.all_custom["mine"].grid(row = 2, column = 1)
            self.all_custom["custom"].grid(row = 0, column = 0)
            ##########################################################
            # for records label
            self.record_frame = Frame(self.root,bg='white')
            self.record_frame_easy = Frame(self.record_frame,bg='white')
            self.record_frame_normal = Frame(self.record_frame,bg='white')
            self.record_frame_hard = Frame(self.record_frame,bg='white')
            # pack the frame
            self.record_frame.pack()
            temp = Label(self.record_frame_easy,text='Easy',bg='white').grid(row=0,column=0)
            temp = Label(self.record_frame_normal,text='normal',bg='white').grid(row=0,column=0)
            temp = Label(self.record_frame_hard,text='hard',bg='white').grid(row=0,column=0)
            # list of records
            ii = 1
            for el in self.records:
                if el[2] == 'easy':
                    temp = Label(self.record_frame_easy,text=el[0] + ' : ' + el[1],bg='white').grid(row=ii,column=0)
                elif el[2] == 'normal':
                    temp = Label(self.record_frame_normal,text=el[0] + ' : ' + el[1],bg='white').grid(row=ii,column=0)
                elif el[2] == 'hard':
                    temp = Label(self.record_frame_hard,text=el[0] + ' : ' + el[1],bg='white').grid(row=ii,column=0)
                ii+=1
            self.record_frame_easy.pack(side = 'left')
            self.record_frame_normal.pack(side = 'left')
            self.record_frame_hard.pack(side = 'left')
            ##########################################################
            # define images
            self.images = {
                "logo": PhotoImage(file = "images/logo.gif")
            }
            ##########################################################
            # define a frame for logo and close button
            self.frame_end = Frame(self.root,bg='white')
            # pack the frame
            self.frame_end.pack()
            # set a list of button for levels
            self.btn_and_lbl_ends = {
                'logo' : Label(self.frame_end, image=self.images['logo'],bg='white'),
                # 'close' : Button(self.frame_end, text='Close',command= lambda: self.close_program()),
                'close' : Button(self.frame_end, text='Close',bg='white',command= lambda: self.close_program())
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
        except:
            print('Initial method')
    #-------------------------------------------------------------------------#
    def get_name_to_save(self,type):
        try:
            ##########################################################
            # define the main root for get name window
            self.close_program()
            self.root = Tk()
            # set title
            self.root.title('Soroush Minesweeper!')

            self.root.eval('tk::PlaceWindow . center')
            ##########################################################
            # define a frame for labels
            self.frame_get_name_0 = Frame(self.root)
            self.frame_get_name = Frame(self.root)
            # pack it
            self.frame_get_name_0.pack()
            self.frame_get_name.pack()
            # define a text variable to get name
            self.input_get_name = StringVar()
            # set of labels
            self.lbls_get_name = {
                'title': Label(self.frame_get_name_0, text='To play game you need a name to save your record in a file.'),
                'get' : Label(self.frame_get_name, text='Enter the name : '),
                'name': Entry(self.frame_get_name,textvariable=self.input_get_name)
            }
            self.lbls_get_name['title'].grid(row=0,column=0)
            self.lbls_get_name['get'].grid(row=0,column=0)
            self.lbls_get_name['name'].grid(row=0,column=1)
            ##########################################################
            # set for buttons
            self.btns_get_name = {
                'back' : Button(self.frame_get_name, text='back',command= lambda: self.go_to_menu()),
                'next': Button(self.frame_get_name, text='next',command= lambda: self.play_game(type))
            }
            self.btns_get_name['next'].grid(row=1,column=0)
            self.btns_get_name['back'].grid(row=1,column=1)
            ##########################################################
            ##########################################################
        except:
            print('Get Name Method')
    #-------------------------------------------------------------------------#
    def openOthers_inzero(self,btn):
        try:
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
            if x + 1 < self.size_x and y - 1 >= 0: # check top right
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
            if x + 1 < self.size_x: # check right
                if self.btns[x+1][y]['state'] != '+':
                    self.btns[x+1][y]['state'] = '+'
                    self.btns[x+1][y]['btn'].config(text=str(self.btns[x+1][y]['num']),bg='yellow')
                    if self.btns[x+1][y]['num'] == 0:
                        self.openOthers_inzero(self.btns[x+1][y])
            if x - 1 >= 0 and y + 1 < self.size_y: # check bottom left
                if self.btns[x-1][y+1]['state'] != '+':
                    self.btns[x-1][y+1]['state'] = '+'
                    self.btns[x-1][y+1]['btn'].config(text=str(self.btns[x-1][y+1]['num']),bg='yellow')
                    if self.btns[x-1][y+1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x-1][y+1])
            if y + 1 < self.size_y: # check bottom
                if self.btns[x][y+1]['state'] != '+':
                    self.btns[x][y+1]['state'] = '+'
                    self.btns[x][y+1]['btn'].config(text=str(self.btns[x][y+1]['num']),bg='yellow')
                    if self.btns[x][y+1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x][y+1])
            if x + 1 < self.size_x and y + 1 < self.size_y: # check bottom right
                if self.btns[x+1][y+1]['state'] != '+':
                    self.btns[x+1][y+1]['state'] = '+'
                    self.btns[x+1][y+1]['btn'].config(text=str(self.btns[x+1][y+1]['num']),bg='yellow')
                    if self.btns[x+1][y+1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x+1][y+1])
        except:
            print("Open other method")
    #-------------------------------------------------------------------------#
    def showAllMines(self):
        try:
            for i in range(self.size_x):
                for j in range(self.size_y):
                    if self.btns[i][j]['checkMine']:
                        self.btns[i][j]['btn'].config(text = '*',bg='orange')
        except:
            print("Show all Mines method")
    #-------------------------------------------------------------------------#
    def updateTimer(self):
        try:
            ts = "00:00:00"
            if self.startTime != None:
                delta = datetime.now() - self.startTime
                ts = str(delta).split('.')[0] # drop ms
                if delta.total_seconds() < 36000:
                    ts = "0" + ts # zero-pad
            self.first_frame_set["timer"].config(text = ts)
            self.first_frame.after(100, self.updateTimer)
        except:
            print('Time Updator method')
    #-------------------------------------------------------------------------#
    def checkWin(self):
        try:
            c = 0
            for i in range(self.size_x):
                for j in range(self.size_y):
                    if self.btns[i][j]['state'] == 'O' or self.btns[i][j]['state'] == 'P':
                        c+=1
            if c == self.mines_no:
                if self._g_type == 'easy' or self._g_type == 'hard' or self._g_type == 'normal':
                    self.records.append([self.input_get_name.get() , self.first_frame_set["timer"].cget('text') , self._g_type])
                if self._g_type == 'computer':
                    return False
                res = tkMessageBox.askyesno("NICE!", 'You Won! Play again?')
                if res:
                    self.reset_game()
                else:
                    self.go_to_menu()
            else:
                return True
        except:
            print('check win method')
    #-------------------------------------------------------------------------#
    def user_lose(self):
        try:
            self.checkComputer = False
            res = tkMessageBox.askyesno("Game Over", 'You Lose! Play again?')
            if res:
                self.reset_game()
            else:
                self.go_to_menu()
        except:
            print('user lose method')
    #-------------------------------------------------------------------------#
    def right_click(self,i,j):
        try:
            return lambda Button: self.right_click_0(self.btns[i][j])
        except:
            print('first right click')
    #-------------------------------------------------------------------------#
    def right_click_0(self,btn):
        try:
            if self.startTime == None:
                self.startTime = datetime.now()
            if self.flags_no > 0 and btn['state'] == 'O':
                self.lbl_extra['Flags'].config(text=str(int(self.lbl_extra['Flags'].cget("text"))+1))
                btn['btn'].config(text='P')
                btn['state'] = 'P'
                self.flags_no -= 1
            elif btn['state'] == 'P':
                self.lbl_extra['Flags'].config(text=str(int(self.lbl_extra['Flags'].cget("text"))-1))
                btn['btn'].config(text='#')
                btn['state'] = 'O'
                self.flags_no += 1
            else:
                pass
        except:
            print('final right click')
    #-------------------------------------------------------------------------#
    def left_click(self,i,j):
        try:
            return lambda Button: self.left_click_0(self.btns[i][j])
        except:
            print('first left click')
    #-------------------------------------------------------------------------#
    def left_click_0(self,btn):
        try:
            if self.startTime == None:
                self.startTime = datetime.now()
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
                self.checkWin()
        except:
            print('left click finally')
    #-------------------------------------------------------------------------#
    def set_numbers_for_btns(self):
        try:
            mines = 0
            for x in range(self.size_x):
                for y in range(self.size_y):
                    if not self.btns[x][y]['checkMine']:
                        mines = 0
                        # check 8 neighboors
                        if x - 1 >= 0 and y - 1 >= 0: # check top left
                            if self.btns[x-1][y-1]['checkMine']:
                                mines += 1
                        if y - 1 >= 0: # check top
                            if self.btns[x][y-1]['checkMine']:
                                mines += 1
                        if x + 1 < self.size_x and y - 1 >= 0: # check top right
                            if self.btns[x+1][y-1]['checkMine']:
                                mines += 1
                        if x - 1 >= 0: # check left
                            if self.btns[x-1][y]['checkMine']:
                                mines += 1
                        if x + 1 < self.size_x: # check right
                            if self.btns[x+1][y]['checkMine']:
                                mines += 1
                        if x - 1 >= 0 and y + 1 < self.size_y: # check bottom left
                            if self.btns[x-1][y+1]['checkMine']:
                                mines += 1
                        if y + 1 < self.size_y: # check bottom
                            if self.btns[x][y+1]['checkMine']:
                                mines += 1
                        if x + 1 < self.size_x and y + 1 < self.size_y: # check bottom right
                            if self.btns[x+1][y+1]['checkMine']:
                                mines += 1
                        self.btns[x][y]['num'] = mines
        except:
            print('set number for buttons method')
    #-------------------------------------------------------------------------#
    def play_game(self,type):
        try:
            ##########################################################
            if type == 'computer':
                self.input_get_name = StringVar()
                self.input_get_name.set(type)
                self._g_type = type
                # size of the board
                self.size_x = 9
                self.size_y = 9
                # define the number of mines in the game
                self.mines_no = 10
                self.flags_no = 10

            if self.input_get_name.get() == "" :
                res = tkMessageBox.askyesno("Warning", 'You need to enter a name. Do you want to try again?')
                if res:
                    self.go_to_menu()
                else:
                    self.close_program()
            else:
                # set type
                self._g_type = type
                if type == 'easy':
                    
                    # size of the board
                    self.size_x = 9
                    self.size_y = 9
                    # define the number of mines in the game
                    self.mines_no = 10
                    self.flags_no = 10
                elif type == 'normal':
                    
                    # size of the board
                    self.size_x = 16
                    self.size_y = 16
                    # define the number of mines in the game
                    self.mines_no = 25
                    self.flags_no = 25
                elif type == 'hard':
                    
                    # size of the board
                    self.size_x = 23
                    self.size_y = 23
                    # define the number of mines in the game
                    self.mines_no = 33
                    self.flags_no = 33
                elif type == 'custom':
                    if not self.get_size_for_custom_x.get().isnumeric() or not self.get_size_for_custom_y.get().isnumeric() or not self.get_mine_for_custom.get().isnumeric():
                        res = tkMessageBox.askyesno("Warning", 'You need to enter all inputs for custom play. Do you want to try again?')
                        if res:
                            self.go_to_menu()
                        else:
                            self.close_program()
                    else:
                        # size of the board
                        self.size_x = int(self.get_size_for_custom_x.get())
                        self.size_y = int(self.get_size_for_custom_y.get())
                        
                        # define the number of mines in the game
                        self.mines_no = int(self.get_mine_for_custom.get())
                        self.flags_no = int(self.get_mine_for_custom.get())
                ##########################################################
                # define the main root
                self.close_program()
                self.root = Tk()
                # set a None value for start time
                self.startTime = None
                # set title
                self.root.title('Soroush Minesweeper!')
                self.root.eval('tk::PlaceWindow . center')
                ##########################################################
                # define a frame for timer and buttons
                self.first_frame_0 = Frame(self.root)
                self.first_frame = Frame(self.root)
                # pack the frame
                self.first_frame_0.pack()
                self.first_frame.pack()
                # set a list of label for information
                self.first_frame_set = {
                    'name' : Label(self.first_frame_0, text='Welcome '+self.input_get_name.get()),
                    'timer' : Label(self.first_frame_0, text='text'),
                    'back' : Button(self.first_frame, text='Back to menu',command= lambda: self.go_to_menu()),
                    'close' : Button(self.first_frame, text='Close',command= lambda: self.close_program()),
                    'reset' : Button(self.first_frame, text='Reset',command= lambda: self.reset_game())
                }
                # set a position for them
                self.first_frame_set["name"].grid(row = 0, column = 0)
                self.first_frame_set["timer"].grid(row = 1, column = 0)
                self.first_frame_set["reset"].grid(row = 0, column = 0)
                self.first_frame_set["back"].grid(row = 0, column = 1)
                self.first_frame_set["close"].grid(row = 0, column = 2)
                ##########################################################
                # define another frame for game
                self.game_frame = Frame(self.root)
                # pack the frame
                self.game_frame.pack()
                # define a dictionary to set all buttons on it and set some property as well
                self.btns = dict({})

                list_of_mines = self.get_random_mine(self.mines_no,self.size_x,self.size_y)

                for i in range(self.size_x):
                    for j in range(self.size_y):
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
                # define another frame for details
                self.extra_detail = Frame(self.root)
                # pack the frame
                self.extra_detail.pack()
                # a set for extra details
                self.lbl_extra = {
                    'Mines_text' : Label(self.extra_detail, text='Mines : '),
                    'Mines' : Label(self.extra_detail, text=str(self.mines_no)),
                    'Flags_text' : Label(self.extra_detail, text='Flags : '),
                    'Flags' : Label(self.extra_detail, text='0')
                }
                self.lbl_extra['Mines_text'].grid(row=0,column=0)
                self.lbl_extra['Mines'].grid(row=0,column=1)
                self.lbl_extra['Flags_text'].grid(row=0,column=2)
                self.lbl_extra['Flags'].grid(row=0,column=3)
                ##########################################################
                self.updateTimer()
                ##########################################################
                ##########################################################
        except:
            print('play game')
    #-------------------------------------------------------------------------#
    def computer_play(self,level):
        try:
            self.checkComputer = True
            self.play_game('computer')
            if level == 'beginner':
                while(self.checkWin() and self.checkComputer):
                    r_i = random.randrange(self.size_x)
                    r_j = random.randrange(self.size_y)
                    self.left_click_0(self.btns[r_i][r_j])
                    
            elif level == 'mid-level':
                pass
            elif level == 'intelligent':
                pass
            if not self.checkWin():
                res = tkMessageBox.showinfo("NICE!")
                self.go_to_menu()
        except:
            print('computer play method')
    #-------------------------------------------------------------------------#
    def get_random_mine(self,Mine,size_x,size_y):
        try:
            l = []
            i = 0
            while i < Mine:
                r = random.randrange(size_x*size_y)
                y = 0
                x = 0
                while r > size_y-1:
                    r -= size_y
                    x = r
                    y += 1
                if [x,y] not in l:
                    l.append([x,y])
                    i+=1
            return l 
        except:
            print('get random mine method')
    #-------------------------------------------------------------------------#
    def close_program(self):
        try:
            try:
                file = open('saved_records.txt','w')
                for el in self.records:
                    file.write(el[0]+'%-%'+el[1]+'%-%'+el[2]+'%-%\n')
                file.close()
            except:
                print('error in save records')
            self.root.destroy()
        except:
            print('close program method')
    #-------------------------------------------------------------------------#
    def reset_game(self):
        try:
            self.play_game(self._g_type)
        except:
            print('reset method')
    #-------------------------------------------------------------------------#
    def go_to_menu(self):
        try:
            self.close_program()
            self.__init__()
        except:
            print('go to menu method')
    #-------------------------------------------------------------------------#
        

m = Mine()
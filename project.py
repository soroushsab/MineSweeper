
from time import time
from tkinter import *
from tkinter import messagebox as tkMessageBox
import random
from datetime import datetime
import functools

class Mine():
    #-------------------------------------------------------------------------#
    def __init__(self):
        try:
            ##########################################################
            # get previous recordes
            # a list to save all recordes
            self.records = []
            try:
                # read from saveed file
                with open('saved_records.txt','r') as f:
                    for row in f:
                        # I defined a way to make file readable and now I used my way to read and split
                        self.records.append(row.split('%-%')[:-1])
                f.close
            except:
                # if it is the first time just print no file
                print('no file')
            # sort file by time which is second column
            self.records = sorted(self.records,key=lambda x: (x[1]))
            ##########################################################
            # define the main root
            self.root = Tk()
            # set title
            self.root.title('Soroush Minesweeper!')
            # set back ground white
            self.root.config(bg='white')
            # set the window in center of the screen
            self.root.eval('tk::PlaceWindow . center')
            ##########################################################

            self.record_for_machine_learning = []
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
            # set a list of button
            # three button here for game levels
            # and three more for computer game levels
            self.btns_lvls = {
                'easy' : Button(self.frame_btns, text='Easy',bg='white', command= lambda: self.get_name_to_save('easy')),
                'normal' : Button(self.frame_btns, text='Normal',bg='white',command= lambda: self.get_name_to_save('normal')),
                'hard' : Button(self.frame_btns, text='Hard',bg='white',command= lambda: self.get_name_to_save('hard')),
                'computer1' : Button(self.frame_btns, text='Computer-Beginner',bg='white',command= lambda: self.computer_play('beginner')),
                'computer2' : Button(self.frame_btns, text='Computer-mid level',bg='white',command= lambda: self.computer_play('mid-level')),
                'computer3' : Button(self.frame_btns, text='Computer-Intelligent',bg='white',command= lambda: self.computer_play('intelligent'))
            }
            # set a position for them
            self.btns_lvls["easy"].grid(row = 0, column = 0)
            self.btns_lvls["normal"].grid(row = 0, column = 1)
            self.btns_lvls["hard"].grid(row = 0, column = 2)
            self.btns_lvls["computer1"].grid(row = 1, column = 0)
            self.btns_lvls["computer2"].grid(row = 1, column = 1)
            self.btns_lvls["computer3"].grid(row = 1, column = 2)
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
            # set a list of buttons, labels, and Inputs for cusrom game
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
            # list all previous records on record part
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
            # define images for my logo
            logo_img = PhotoImage(file = "images/logo.gif")
            ##########################################################
            # define a frame for logo and close button
            self.frame_end = Frame(self.root,bg='white')
            # pack the frame
            self.frame_end.pack()
            # set a list of button for levels
            self.btn_and_lbl_ends = {
                'logo' : Label(self.frame_end, image=logo_img,bg='white'),
                'close' : Button(self.frame_end, text='Close',bg='white',command= lambda: self.close_program())
            }
            # set a position for them
            self.btn_and_lbl_ends["logo"].grid(row = 0, column = 0)
            self.btn_and_lbl_ends["close"].grid(row = 1, column = 0)
            ##########################################################
            self.root.mainloop()
            ##########################################################
        except:
            print('Initial method')
    #-------------------------------------------------------------------------#
    def get_name_to_save(self,type):
        try:
            # this function is for get user name to save in the files and records
            ##########################################################
            # close previous program that was main menu
            self.close_program()
            # define the main root for get name window
            self.root = Tk()
            # set title
            self.root.title('Soroush Minesweeper!')
            # set to center
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
        except:
            print('Get Name Method')
    #-------------------------------------------------------------------------#
    def openOthers_inzero(self,btn):
        # when we click on a button that has zero number all around of this button that are zero 
        # should be opened and also open all button around these zeros
        try:
            # get the button that we clicked on it
            # get indexes
            x = btn['x']
            y = btn['y']
            # set the state as + which is opened button
            btn['state'] = '+'
            # change the background of button to yellow ( this is because of make it clear )
            btn['btn'].config(text=str(btn['num']),bg='yellow')
            # we have to check all around of the button
            # check the top left button
            if x - 1 >= 0 and y - 1 >= 0: # check top left
                # if it is not open
                if self.btns[x-1][y-1]['state'] != '+':
                    # open top left (make state as +)
                    self.btns[x-1][y-1]['state'] = '+'
                    # change background
                    self.btns[x-1][y-1]['btn'].config(text=str(self.btns[x-1][y-1]['num']),bg='yellow')
                    # if this top left button has zero bomb around it so we need to open around of that as well
                    if self.btns[x-1][y-1]['num'] == 0:
                        # call the function and pass the top left button to the function
                        self.openOthers_inzero(self.btns[x-1][y-1])
            if y - 1 >= 0: # check top
                # do the same
                if self.btns[x][y-1]['state'] != '+':
                    self.btns[x][y-1]['state'] = '+'
                    self.btns[x][y-1]['btn'].config(text=str(self.btns[x][y-1]['num']),bg='yellow')
                    if self.btns[x][y-1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x][y-1])
            if x + 1 < self.size_x and y - 1 >= 0: # check top right
                # do the same
                if self.btns[x+1][y-1]['state'] != '+':
                    self.btns[x+1][y-1]['state'] = '+'
                    self.btns[x+1][y-1]['btn'].config(text=str(self.btns[x+1][y-1]['num']),bg='yellow')
                    if self.btns[x+1][y-1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x+1][y-1])
            if x - 1 >= 0: # check left
                # do the same
                if self.btns[x-1][y]['state'] != '+':
                    self.btns[x-1][y]['state'] = '+'
                    self.btns[x-1][y]['btn'].config(text=str(self.btns[x-1][y]['num']),bg='yellow')
                    if self.btns[x-1][y]['num'] == 0:
                        self.openOthers_inzero(self.btns[x-1][y])
            if x + 1 < self.size_x: # check right
                # do the same
                if self.btns[x+1][y]['state'] != '+':
                    self.btns[x+1][y]['state'] = '+'
                    self.btns[x+1][y]['btn'].config(text=str(self.btns[x+1][y]['num']),bg='yellow')
                    if self.btns[x+1][y]['num'] == 0:
                        self.openOthers_inzero(self.btns[x+1][y])
            if x - 1 >= 0 and y + 1 < self.size_y: # check bottom left
                # do the same
                if self.btns[x-1][y+1]['state'] != '+':
                    self.btns[x-1][y+1]['state'] = '+'
                    self.btns[x-1][y+1]['btn'].config(text=str(self.btns[x-1][y+1]['num']),bg='yellow')
                    if self.btns[x-1][y+1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x-1][y+1])
            if y + 1 < self.size_y: # check bottom
                # do the same
                if self.btns[x][y+1]['state'] != '+':
                    self.btns[x][y+1]['state'] = '+'
                    self.btns[x][y+1]['btn'].config(text=str(self.btns[x][y+1]['num']),bg='yellow')
                    if self.btns[x][y+1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x][y+1])
            if x + 1 < self.size_x and y + 1 < self.size_y: # check bottom right
                # do the same
                if self.btns[x+1][y+1]['state'] != '+':
                    self.btns[x+1][y+1]['state'] = '+'
                    self.btns[x+1][y+1]['btn'].config(text=str(self.btns[x+1][y+1]['num']),bg='yellow')
                    if self.btns[x+1][y+1]['num'] == 0:
                        self.openOthers_inzero(self.btns[x+1][y+1])
        except:
            print("Open other method")
    #-------------------------------------------------------------------------#
    def showAllMines(self):
        # when the player click on a bomb the needs to show all bombs at the end
        try:
            # search for all
            for i in range(self.size_x):
                for j in range(self.size_y):
                    # if the button is a bomb make it clear
                    if self.btns[i][j]['checkMine']:
                        self.btns[i][j]['btn'].config(text = '*',bg='orange')
        except:
            print("Show all Mines method")
    #-------------------------------------------------------------------------#
    def updateTimer(self):
        try:
            # this is a timer to show the time to player
            # and this will save in the record files
            # set 0 at first
            ts = "00:00:00"
            # check if time has not started yet
            if self.startTime != None:
                # get now time and minus with the start time
                delta = datetime.now() - self.startTime
                # we dont need ms in our tiem ( just s,m, and h )
                ts = str(delta).split('.')[0]
                # to have a good look if the timer less than 10 hours the timer would be like 0:00:00
                # so we add a 0 at the end and it will be like 00:00:00
                if delta.total_seconds() < 36000:
                    ts = "0" + ts
            # check if the game has not finished yet
            if not self.game_check_finish:
                # set timer in the label
                self.first_frame_set["timer"].config(text = ts)
                # recall the function
                self.first_frame_0.after(100, self.updateTimer)
        except:
            print('Time Updator method')
    #-------------------------------------------------------------------------#
    def checkWin(self):
        # this function count number of not opened buttons if it is equal to number of mines it means
        # all are open except mines. so player will win.
        try:
            # a counter to count not opened buttons
            c = 0
            # count those buttons that are not opened (state == O) and flaged buttons (state == P)
            for i in range(self.size_x):
                for j in range(self.size_y):
                    if self.btns[i][j]['state'] == 'O' or self.btns[i][j]['state'] == 'P':
                        c+=1
            # check number of mines and not opened buttons
            if c == self.mines_no:
                # if player plays in one of the easy, hard, and normal, his/her time and name will be saved to record and show it 
                # in the record list. (this is common way because we do not need to save custom play or computer play)
                if self._g_type == 'easy' or self._g_type == 'hard' or self._g_type == 'normal':
                    self.records.append([self.input_get_name.get() , self.first_frame_set["timer"].cget('text') , self._g_type])
                # this variable defined to check that is game has been finished or not.
                self.game_check_finish = True
                # show a message with two buttons (YES and NO)
                # and ask player to play again or not
                res = tkMessageBox.askyesno("NICE!", 'You Won! Play again?')
                if res:
                    self.reset_game()
                else:
                    self.go_to_menu()
            else:
                # if the number of not opened buttons is not equal to number of mines just return true to do some actions somewhere else
                return True
        except:
            print('check win method')
    #-------------------------------------------------------------------------#
    def user_lose(self):
        try:
            # this variable defined to check that is game has been finished or not.
            self.game_check_finish = True
            # show a message with two buttons (YES and NO)
            # and ask player to play again or not
            res = tkMessageBox.askyesno("Game Over", 'You Lose! Play again?')
            if res:
                self.reset_game()
            else:
                self.go_to_menu()
        except:
            print('user lose method')
    #-------------------------------------------------------------------------#
    def right_click(self,i,j):
        """
        this is very important:
        when we dont use this function, the buttons are not working or all have the
        same reference. I tried many times to do it without this extra function but
        I couldn't. it seemed we need to have this function.
        The main reason is because of using the lambda. as we dont need to auto call
        the function so we just add lambda then the function will call when we click
        on the button.
        """
        try:
            return lambda Button: self.right_click_0(self.btns[i][j])
        except:
            print('first right click')
    #-------------------------------------------------------------------------#
    def right_click_0(self,btn):
        try:
            # if it is the first right click the timer should begin
            # and not comuter game
            if self.startTime == None and self._g_type != 'computer':
                self.startTime = datetime.now()
            # in each game we have a number of flags that we can use
            # this number should be equal to number of mines
            # now we have to add a function to check the number of flags
            # should not more than number of mines
            # at first number of flag is euql to number of mines
            # and then for each flag I minus one so the number of flag
            # should not be less than 0
            # and we can flag a not opened button so we have to check that
            # the button has not opened.
            if self.flags_no >= 0 and btn['state'] == 'O':
                # to show the flag I change the text to "P" and update the label for the number of flags
                self.lbl_extra['Flags'].config(text=str(int(self.lbl_extra['Flags'].cget("text"))+1))
                btn['btn'].config(text='P')
                # change state to "P"
                btn['state'] = 'P'
                # Flags minus one
                self.flags_no -= 1
            elif btn['state'] == 'P':
                # if it alredy is a flag try to remove flage
                # add numbre of flags, change the label for number of flags and state
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
            # same as right
            return lambda Button: self.left_click_0(self.btns[i][j])
        except:
            print('first left click')
    #-------------------------------------------------------------------------#
    def left_click_0(self,btn):
        try:
            # if it is the first left click the timer should begin
            # and not comuter game
            if self.startTime == None and self._g_type != 'computer':
                self.startTime = datetime.now()
            # if the button is flagged so the right click should not work for it
            if btn['state'] == 'P':
                pass
            # if button has mine player will lose and call lose functions
            elif btn['checkMine']:
                self.showAllMines()
                btn['btn'].config(bg='red')
                self.user_lose()
            # if it is not mine or flagged or opened
            elif btn['state'] == 'O':
                # if number of button (number of flags around it) is 0 all button around it should be open automatically 
                if btn['num'] == 0:
                    self.openOthers_inzero(btn)
                else:
                    btn['state'] = '+'
                    btn['btn'].config(text=str(btn['num']),bg='yellow')
                # after each left click that cause open a button we need to check win
                self.checkWin()
        except:
            print('left click finally')
    #-------------------------------------------------------------------------#
    def set_numbers_for_btns(self):
        try:
            # when game starts, we need to add a number for each button
            # which is number of mines around it.
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
                self.game_check_finish = False
                if self._g_type != 'computer':
                    self.updateTimer()
                ##########################################################
                ##########################################################
        except:
            print('play game')
    #-------------------------------------------------------------------------#
    def check_around(self,btn):
        try:
            number = btn['num']
            if number == 0:
                print('sa')
                return 0
            temp_list = []
            flags = 0
            x = btn['x']
            y = btn['y']
            around = 0
            if x - 1 >= 0 and y - 1 >= 0: # check top left
                if self.btns[x-1][y-1]['state'] == 'O'  :
                    around += 1
                    temp_list.append([x-1,y-1])
                elif self.btns[x-1][y-1]['state'] == 'P'  :
                    flags += 1
            if y - 1 >= 0: # check top
                if self.btns[x][y-1]['state'] == 'O'  :
                    around += 1
                    temp_list.append([x,y-1])
                elif self.btns[x][y-1]['state'] == 'P'  :
                    flags += 1
            if x + 1 < self.size_x and y - 1 >= 0: # check top right
                if self.btns[x+1][y-1]['state'] == 'O'  :
                    around += 1
                    temp_list.append([x+1,y-1])
                elif self.btns[x+1][y-1]['state'] == 'P'  :
                    flags += 1
            if x - 1 >= 0: # check left
                if self.btns[x-1][y]['state'] == 'O'  :
                    around += 1
                    temp_list.append([x-1,y])
                elif self.btns[x-1][y]['state'] == 'P'  :
                    flags += 1
            if x + 1 < self.size_x: # check right
                if self.btns[x+1][y]['state'] == 'O'  :
                    around += 1
                    temp_list.append([x+1,y])
                elif self.btns[x+1][y]['state'] == 'P'  :
                    flags += 1
            if x - 1 >= 0 and y + 1 < self.size_y: # check bottom left
                if self.btns[x-1][y+1]['state']  == 'O'  :
                    around += 1
                    temp_list.append([x-1,y+1])
                elif self.btns[x-1][y+1]['state'] == 'P'  :
                    flags += 1
            if y + 1 < self.size_y: # check bottom
                if self.btns[x][y+1]['state'] == 'O'  :
                    around += 1
                    temp_list.append([x,y+1])
                elif self.btns[x][y+1]['state'] == 'P'  :
                    flags += 1
            if x + 1 < self.size_x and y + 1 < self.size_y: # check bottom right
                if self.btns[x+1][y+1]['state'] == 'O'  :
                    around += 1
                    temp_list.append([x+1,y+1])
                elif self.btns[x+1][y+1]['state'] == 'P'  :
                    flags += 1
            #################################################################
            if flags == number:
                for i in temp_list:
                    self.left_click_0(self.btns[i[0]][i[1]])
                    pass
                return 1
            elif number-flags == around:
                for i in temp_list:
                    self.btns[i[0]][i[1]]['btn'].config(text = 'P')
                    self.btns[i[0]][i[1]]['state'] = 'P'
                    return 1
            else:
                for i in range(len(temp_list)):
                    temp_list[i] = [temp_list[i],1-((number-flags)/around)]
                temp_list = sorted(temp_list,key=lambda x: (x[1]))
                for i in temp_list:
                    if i[1] == 0:
                        self.btns[i[0][0]][i[0][1]]['state'] = 'P'
                        self.btns[i[0][0]][i[0][1]]['btn'].config(text = 'P')
                        return 1
        except:
            print('check around')
    #-------------------------------------------------------------------------#
    def get_all_opens(self):
        try:
            # for computer player mid level I need to get all opened button list
            res = []
            for i in range(self.size_x):
                for j in range(self.size_y):
                    if self.btns[i][j]['state'] == '+' and self.btns[i][j]['num'] > 0:
                        res.append(self.btns[i][j])
            return res
        except:
            print('get all opens func')
    #-------------------------------------------------------------------------#
    def b_p_computer(self):
        try:
            # randomly selection for beginner computer player
            if not self.game_check_finish:
                r_i = random.randrange(self.size_x)
                r_j = random.randrange(self.size_y)
                if self.btns[r_i][r_j]['state'] == 'O':
                    self.left_click_0(self.btns[r_i][r_j])
                    self.root.after(1000,self.b_p_computer)
                else:
                    self.b_p_computer()
            else:
                return
        except:
            print('beginner player')
    #-------------------------------------------------------------------------#
    def m_p_computer(self):
        if not self.game_check_finish:
            if self.ci == 5:
                self.temp_check = True
                self.ci = 0
            r_i = random.randrange(self.size_x)
            r_j = random.randrange(self.size_y)
            if self.btns[r_i][r_j]['state'] == 'O' and self.temp_check:
                self.left_click_0(self.btns[r_i][r_j])
                self.root.after(1000, self.m_p_computer) 
                self.temp_check = False
            else:
                opens = self.get_all_opens()
                if len(opens) < 5:
                    self.temp_check = True
                else:
                    self.ci += 1
                    re0 = False
                    for el in opens:
                        re = self.check_around(el)
                        if re == 1:
                            re0 = True
                    if not re0:
                        self.temp_check = True
                self.root.after(1000, self.m_p_computer) 
        else:
            return
    #-------------------------------------------------------------------------#
    def computer_play(self,level):
        try:
            self.level_c_p = level
            self.play_game('computer')
            if level == 'beginner':
                self.b_p_computer()  
            elif level == 'mid-level':
                self.temp_check = True
                self.ci = 0
                self.m_p_computer()
                    
            elif level == 'intelligent':
                pass
        except :
            print('computer player method')
    #-------------------------------------------------------------------------#
    def get_random_mine(self,Mine,size_x,size_y):
        try:
            # randomly select button to put mines in them
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
                # to close the program we need to save all records
                file = open('saved_records.txt','w')
                for el in self.records:
                    file.write(el[0]+'%-%'+el[1]+'%-%'+el[2]+'%-%\n')
                file.close()
            except:
                print('error in save records')
            # then close the program
            self.root.destroy()
        except:
            print('close program method')
    #-------------------------------------------------------------------------#
    def reset_game(self):
        try:
            # I defined a variable named _g_type that is type of game
            # to reset game will start with the same type of game
            # if it is computer player we need to call another func
            # which is computer player and we have another variable 
            # which is level of computer player
            if self._g_type == 'computer':
                self.computer_play(self.level_c_p)
            else:
                self.play_game(self._g_type)
        except:
            print('reset method')
    #-------------------------------------------------------------------------#
    def go_to_menu(self):
        try:
            # go to menu !
            self.close_program()
            self.__init__()
        except:
            print('go to menu method')
    #-------------------------------------------------------------------------#
        


# make an object
m = Mine()
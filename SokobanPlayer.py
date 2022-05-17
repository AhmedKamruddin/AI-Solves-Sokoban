from sre_constants import SRE_FLAG_ASCII
import tkinter
import os

class Sokoban:
    def __init__(self, level_no):
        self.level_no=level_no
        self.update_level(level_no)
              
        self.lock_movement=0
        self.x, self.y=self.get_current_position()
        
        os.system("clear")
        self.display()


    def display(self):
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if(self.level[i][j]=='W'):
                    print('▩', ' ', end='') 
                elif(self.level[i][j]=='P'):
                    print('☖', ' ', end='')
                elif(self.level[i][j]=='T'):
                    print('☖', ' ', end='')
                elif(self.level[i][j]=='B'):
                    print('▢', ' ', end='')
                elif(self.level[i][j]=='G'):
                    print('•', ' ', end='')
                elif(self.level[i][j]=='C'):
                    print('◆', ' ', end='')
                else:
                    print(' ', ' ', end='')
            print('')
        print('')
        print('')
        if self.level_no==1:
            print("<space>: restart level     <n>: next level     <backspace>: go to main screen     <esc>: exit")
        elif self.level_no==2:
            print("<space>: restart level     <b>: previous level     <backspace>: go to main screen     <esc>: exit")
        self.is_goal_reached()


    def is_goal_reached(self):
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[i])):
                if self.level[i][j] in ['G', 'T']:
                    return False
        print('')
        print('')
        print('\t\t\t\tCONGRATULATIONS! YOU HAVE BEATEN THIS LEVEL')
        self.lock_movement=1
        return True

    def update_level(self, level_no):
        self.level_no=level_no

        # P ☖ Player
        # T ☖ Player on top of Goal
        #     Empty Space
        # G • Goal
        # W ▩ Wall 
        # B ▢ Box
        # C ◆ Box@Goal

        if level_no==1:
            self.level=[[' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
                        ['W', 'W', 'W', ' ', ' ', ' ', 'W', ' '],
                        ['W', 'G', 'P', 'B', ' ', ' ', 'W', ' '],
                        ['W', 'W', 'W', ' ', 'B', 'G', 'W', ' '],
                        ['W', 'G', 'W', 'W', 'B', ' ', 'W', ' '],
                        ['W', ' ', 'W', ' ', 'G', ' ', 'W', 'W'],
                        ['W', 'B', ' ', 'C', 'B', 'B', 'G', 'W'],
                        ['W', ' ', ' ', ' ', 'G', ' ', ' ', 'W'],
                        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
        elif level_no==2:
            self.level=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', 'W', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'W', 'W', 'W', ' ', 'B', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                        [' ', ' ', 'W', ' ', ' ', 'B', ' ', ' ', 'W', ' ', ' ', 'B', 'W', ' ', 'W', ' ', 'B', 'B', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', 'W'],
                        [' ', 'W', 'W', ' ', 'W', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', ' ', ' ', ' ', ' ', 'B', ' ', 'W', ' ', 'W', ' ', ' ', 'W'],
                        [' ', 'W', ' ', ' ', 'W', 'B', ' ', ' ', ' ', 'W', ' ', 'W', 'W', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'B', 'B', 'W', ' ', 'W', ' ', ' ', 'W'],
                        [' ', 'W', ' ', ' ', ' ', ' ', 'B', 'W', 'W', ' ', 'B', ' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', 'B', ' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W'],
                        ['W', 'W', 'W', 'W', 'B', ' ', 'B', ' ', 'W', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', 'W', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'G', 'G', 'W'],
                        ['W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W', 'W', 'W', ' ', 'W', ' ', 'B', ' ', 'B', ' ', 'W', 'W', 'W', ' ', ' ', 'W', 'W', 'W', 'G', 'C', 'W'],
                        ['W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', 'B', 'B', ' ', 'P', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'G', 'G', 'G', 'G', 'W'],
                        ['W', ' ', ' ', 'W', 'W', ' ', ' ', 'W', 'W', ' ', ' ', ' ', 'B', ' ', ' ', 'W', 'B', 'W', ' ', ' ', 'W', 'W', 'G', 'G', 'G', 'G', 'C', 'G', 'W'],
                        ['W', 'W', ' ', 'W', ' ', ' ', 'B', ' ', ' ', 'W', ' ', 'W', ' ', 'B', 'W', 'W', ' ', ' ', 'W', 'W', 'G', 'G', 'G', 'G', 'C', 'G', 'W', 'W', 'W'],
                        ['W', 'W', ' ', 'W', 'W', ' ', ' ', 'B', ' ', ' ', 'W', ' ', 'B', ' ', 'W', ' ', ' ', 'W', 'G', 'G', 'G', 'G', 'C', 'G', 'W', 'W', 'W', ' ', ' '],
                        ['W', ' ', ' ', ' ', ' ', 'B', ' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', ' ', 'G', 'G', 'G', 'G', 'C', 'G', 'W', 'W', 'W', ' ', ' ', ' ', ' '],
                        ['W', ' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'G', 'G', 'C', 'G', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
                        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        ]
        self.x, self.y=self.get_current_position()
        


    def get_current_position(self):
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[0])):
                if(self.level[i][j]=='P'):
                    return i, j
       

    def move_player_up(self):
        if(self.level[self.x][self.y]=='P'):                    #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif(self.level[self.x][self.y]=='T'):                  #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.x=self.x-1

    def up(self):
        if self.level[self.x-1][self.y]==' ':                   #If top tile is an Empty Space
            self.level[self.x-1][self.y]='P'
            self.move_player_up()
            return True
        
        elif self.level[self.x-1][self.y]=='G':                 #If top tile is a Goal tile
            self.level[self.x-1][self.y]='T'
            self.move_player_up()
            return True

        elif self.level[self.x-1][self.y]=='W':                 #If top tile is a Wall
            return False

        elif self.level[self.x-1][self.y]=='B':                 #If top tile is a Box
            if self.level[self.x-2][self.y]==' ':                   #If tile above Box is an Empty Space
                self.level[self.x-2][self.y]='B'
                self.level[self.x-1][self.y]='P'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y]=='G':                 #If tile above Box is a Goal
                self.level[self.x-2][self.y]='C'
                self.level[self.x-1][self.y]='P'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y] in ['W', 'B', 'C']:   #If tile above Box is a Wall, another Box, or Box@Goal
                return False

        elif self.level[self.x-1][self.y]=='C':                 #If top tile is a Box@Goal
            if self.level[self.x-2][self.y]==' ':                   #If tile above Box@Goal is an Empty Space
                self.level[self.x-2][self.y]='B'
                self.level[self.x-1][self.y]='T'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y]=='G':                 #If tile above Box@Goal is a Goal
                self.level[self.x-2][self.y]='C'
                self.level[self.x-1][self.y]='T'
                self.move_player_up()
                return True

            elif self.level[self.x-2][self.y] in ['W', 'B', 'C']:    #If tile above Box@Goal is a Wall, another Box, or Box@Goal
                return False
            
    def move_player_down(self):
        if(self.level[self.x][self.y]=='P'):                    #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif(self.level[self.x][self.y]=='T'):                  #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.x=self.x+1
    
    def down(self):
        if self.level[self.x+1][self.y]==' ':                   #If top tile is an Empty Space
            self.level[self.x+1][self.y]='P'
            self.move_player_down()
            return True
        
        elif self.level[self.x+1][self.y]=='G':                 #If top tile is a Goal tile
            self.level[self.x+1][self.y]='T'
            self.move_player_down()
            return True

        elif self.level[self.x+1][self.y]=='W':                 #If top tile is a Wall
            return False

        elif self.level[self.x+1][self.y]=='B':                 #If top tile is a Box
            if self.level[self.x+2][self.y]==' ':                   #If tile above Box is an Empty Space
                self.level[self.x+2][self.y]='B'
                self.level[self.x+1][self.y]='P'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y]=='G':                 #If tile above Box is a Goal
                self.level[self.x+2][self.y]='C'
                self.level[self.x+1][self.y]='P'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y] in ['W', 'B', 'C']:   #If tile above Box is a Wall, another Box, or Box@Goal
                return False

        elif self.level[self.x+1][self.y]=='C':                 #If top tile is a Box@Goal
            if self.level[self.x+2][self.y]==' ':                   #If tile above Box@Goal is an Empty Space
                self.level[self.x+2][self.y]='B'
                self.level[self.x+1][self.y]='T'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y]=='G':                 #If tile above Box@Goal is a Goal
                self.level[self.x+2][self.y]='C'
                self.level[self.x+1][self.y]='T'
                self.move_player_down()
                return True

            elif self.level[self.x+2][self.y] in ['W', 'B', 'C']:    #If tile above Box@Goal is a Wall, another Box, or Box@Goal
                return False

    def move_player_left(self):
        if self.level[self.x][self.y]=='P':                     #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif self.level[self.x][self.y]=='T':                   #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.y=self.y-1

    def left(self):
        if self.level[self.x][self.y-1]==' ':                   #If left tile is an Empty Space
            self.level[self.x][self.y-1]='P'
            self.move_player_left()
            return True

        elif self.level[self.x][self.y-1]=='G':                 #If left tile is a Goal
            self.level[self.x][self.y-1]='T'
            self.move_player_left()
            return True
        
        elif self.level[self.x][self.y-1]=='W':
            return False
        
        elif self.level[self.x][self.y-1]=='B':                 #If left tile is a Box
            if self.level[self.x][self.y-2]==' ':                   #If tile left of Box is an Empty Space
                self.level[self.x][self.y-2]='B'
                self.level[self.x][self.y-1]='P'
                self.move_player_left()
                return True

            elif self.level[self.x][self.y-2]=='G':                 #If tile left of Box is a Goal
                self.level[self.x][self.y-2]='C'
                self.level[self.x][self.y-1]='P'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2] in ['W', 'B', 'C']:   #If tile left of Box is a Wall, another Box, or Box@Goal
                return False
        
        elif self.level[self.x][self.y-1]=='C':                 #If left tile is a Box@Goal
            if self.level[self.x][self.y-2]==' ':                   #If tile left of Box@Goal is an Empty Space
                self.level[self.x][self.y-2]='B'
                self.level[self.x][self.y-1]='T'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2]=='G':                 #If tile left of Box@Goal is a Goal
                self.level[self.x][self.y-2]='C'
                self.level[self.x][self.y-1]='T'
                self.move_player_left()
                return True
            
            elif self.level[self.x][self.y-2] in ['W', 'B', 'C']:   #If tile left of Box@Goal is a Wall, Box, or Box@Goal
                return False
    

    def move_player_right(self):
        if self.level[self.x][self.y]=='P':                     #If Player is on an Empty Space
            self.level[self.x][self.y]=' '
        elif self.level[self.x][self.y]=='T':                   #If Player is on a Goal
            self.level[self.x][self.y]='G'
        self.y=self.y+1
            
    def right(self):
        
        if self.level[self.x][self.y+1]==' ':                   #If right tile is an Empty Space
            self.level[self.x][self.y+1]='P'
            self.move_player_right()
            return True

        elif self.level[self.x][self.y+1]=='G':                 #If right tile is a Goal
            self.level[self.x][self.y+1]='T'
            self.move_player_right()
            return True
        
        elif self.level[self.x][self.y+1]=='W':
            return False
        
        elif self.level[self.x][self.y+1]=='B':                 #If right tile is a Box
            if self.level[self.x][self.y+2]==' ':                   #If tile right of Box is an Empty Space
                self.level[self.x][self.y+2]='B'
                self.level[self.x][self.y+1]='P'
                self.move_player_right()
                return True

            elif self.level[self.x][self.y+2]=='G':                 #If tile right of Box is a Goal
                self.level[self.x][self.y+2]='C'
                self.level[self.x][self.y+1]='P'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2] in ['W', 'B', 'C']:   #If tile right of Box is a Wall, another Box, or Box@Goal
                return False
        
        elif self.level[self.x][self.y+1]=='C':                 #If right tile is a Box@Goal
            if self.level[self.x][self.y+2]==' ':                   #If tile right of Box@Goal is an Empty Space
                self.level[self.x][self.y+2]='B'
                self.level[self.x][self.y+1]='T'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2]=='G':                 #If tile right of Box@Goal is a Goal
                self.level[self.x][self.y+2]='C'
                self.level[self.x][self.y+1]='T'
                self.move_player_right()
                return True
            
            elif self.level[self.x][self.y+2] in ['W', 'B', 'C']:   #If tile right of Box@Goal is a Wall, Box, or Box@Goal
                return False


game=Sokoban(1)  

win = tkinter.Tk()
win.geometry("0x0")
win.resizable('False', 'False')

def up(event):
    if game.lock_movement==0:
        os.system("clear")
        game.up()
        game.display()

def down(event):
    if game.lock_movement==0:
        os.system("clear")
        game.down()
        game.display()

def left(event):
    if game.lock_movement==0:
        os.system("clear")
        game.left()
        game.display()

def right(event):
    if game.lock_movement==0:
        os.system("clear")
        game.right()
        game.display()

def next_level(event):
    os.system("clear")
    game.lock_movement=0
    game.update_level(2)
    game.display()

def previous_level(event):
    os.system("clear")
    game.lock_movement=0
    game.update_level(1)
    game.display()

def go_to_main_screen(event):
    win.destroy()
    os.system("python3 MainScreen.py")

def restart_game(event):
    os.system("clear")
    game.lock_movement=0
    game.update_level(game.level_no)
    game.display()

def exit_game(event):
    win.destroy()
    os.system("clear")

win.bind("w", up)
win.bind("s", down)
win.bind("a", left)
win.bind("d", right)

win.bind("<Up>", up)
win.bind("<Down>", down)
win.bind("<Left>", left)
win.bind("<Right>", right)

win.bind("n", next_level)
win.bind("b", previous_level)
win.bind("<BackSpace>", go_to_main_screen)
win.bind("<space>", restart_game)
win.bind("<Escape>", exit_game)
    
win.mainloop()


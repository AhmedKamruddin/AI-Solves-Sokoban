import tkinter
import os

class Selection:
    def __init__(self):
        self.selection=0

    def make_selection(self, i):
        self.selection=i

    def return_selection(self):
        return self.selection

obj=Selection()

os.system("clear")

print("----------------")
print("|I want to play|")
print("----------------")
print("")
print("Make AI play")
print("")
print("")
print("<esc>: exit")

win = tkinter.Tk()
win.geometry("0x0")
win.resizable('False', 'False')

def select_top(event):
    obj.make_selection(0)
    os.system("clear")
    print("----------------")
    print("|I want to play|")
    print("----------------")
    print("")
    print("Make AI play")
    print("")
    print("")
    print("<esc>: exit")

def select_bottom(event):
    obj.make_selection(1)
    os.system("clear")
    print("")
    print("I want to play")
    print("")
    print("--------------")
    print("|Make AI play|")
    print("--------------")
    print("")
    print("<esc>: exit")

    
def choose_selection(event):
    if obj.return_selection()==0:
        win.destroy()
        os.system("python3 SokobanPlayer.py")
    elif obj.return_selection()==1:
        win.destroy()
        os.system("python3 SokobanAI.py")
    

def exit_main_screen(event):
    win.destroy()
    os.system("clear")

win.bind("<Up>", select_top)
win.bind("<Down>", select_bottom)
win.bind("<Return>", choose_selection)
win.bind("<Escape>", exit_main_screen)


win.mainloop()

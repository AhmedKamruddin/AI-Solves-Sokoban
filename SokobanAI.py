import tkinter
import os
os.system("clear")
print("Yet to come")
print("<esc>: exit     <space>: restart level     <backspace>: got to main screen")

win = tkinter.Tk()
win.geometry("0x0")
win.resizable('False', 'False')

def go_to_main_screen(event):
    win.destroy()
    os.system("python3 MainScreen.py")

def restart_game(event):
    win.destroy()
    os.system("python3 SokobanAI.py")

def exit_game(event):
    win.destroy()
    os.system("clear")

win.bind("<BackSpace>", go_to_main_screen)
win.bind("<space>", restart_game)
win.bind("<Escape>", exit_game)
    
win.mainloop()

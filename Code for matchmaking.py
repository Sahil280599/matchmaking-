import random
import time
from tkinter import Tk,Button,DISABLED

def show_symbol(x,y):
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousx = x  # first card
        previousy = y  # previous card which will flip
        first = False
    elif previousx != x or previousy != y:
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True




win= Tk()
win.title("MATCH MAKING GAME")
win.resizable(width=True, height=True) # for prevent resizing

first=True
previous_x= 0  # used to remember the card
previous_y= 0
buttons = { } # which contains buttons for particular code
buttons_symbol={ } # text on the buttons
symbols=[u'\u1F970',u'\u1F60D',u'\u1F929',u'\u1F618',u'\u1F617',u'\u263A',
        u'\u1F61A',u'\u1F619',u'\u1F972',u'\u1F60B',u'\u1F637',u'\u1F634',
        u'\u1F970',u'\u1F60D',u'\u1F929',u'\u1F618',u'\u1F617',u'\u263A',
        u'\u1F61A', u'\u1F619', u'\u1F972', u'\u1F60B', u'\u1F637',u'\u1F634'] # there is specific code for emojis

random.shuffle(symbols) #  it will shuffle all the symbols

for x in range(6):
    for y in range(4): # to plot buttons in row column
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 10, height = 8)# designed height width of buttons # show_symbol will calling the function again and again
        button.grid(column = x , row = y)
        buttons[x,y] = button # so that all the buttons will be stored in a single place
        button_symbols[x,y] = symbols.pop()



win.mainloop()

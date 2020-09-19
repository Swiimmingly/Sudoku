from tkinter import *
import tkinter.messagebox
from puzzle import ready_puzzle, solved
import random

# get solved and unsolved sudoku puzzles
unfilled = ready_puzzle()
filled = solved


root = Tk()
root.title("Sudoku")

canvas = Canvas(root, bg='slate grey', width=500, height=500)
canvas.pack(side='top', fill='both', expand='1')
grow = -1
gcol = -1

#draw sudoku grid
def grid():
    global canvas
    x = 30
    for one in range(0,500,50):
        for j in range(0,500,50):
            if one % 150 == 0 and j % 150 == 0:
                canvas.create_line(x+j, x+one, x+one, x+one, fill='Black', width=3)
                canvas.create_line(x+one, x+j, x+one, x+one, fill='Black', width=3)
            else:
                canvas.create_line(x+j, x+one, x+one, x+one, fill='Black', width=1)
                canvas.create_line(x+one, x+j, x+one, x+one, fill='Black', width=1)

# fill the grid with puzzle numbers
def game():
    global canvas
    canvas.delete('numbers')
    for i in range(81):
        row = i // 9
        col = i % 9

        x = 30 + col * 50 + 25
        y = 30 + row * 50 + 25

        if unfilled[row][col] == 0:
            canvas.create_text(x, y, text='', tags='numbers')
        else:
            canvas.create_text(x, y, text=unfilled[row][col],tags='numbers', fill='Black', font='Helvetica 18 bold')

# fill the puzzle after user input
def player_game():
    global canvas, grow, gcol

    x = 30 + gcol * 50 + 25
    y = 30 + grow * 50 + 25
    canvas.create_text(x, y, text=unfilled[grow][gcol],tags='numbers', fill='lime green', font='Helvetica 18 bold')

# get the cell user clicks on
def cellClicked(event):
    global canvas,grow,gcol

    x = event.x
    y = event.y

    if (30 < x < 510 - 30 and 30 < y < 510 - 30):
        canvas.focus_set()
    gcol = (x - 30)//50
    grow = (y - 30)//50

    highlight()

# draw highlight where user clicks
def highlight():
    global canvas,grow,gcol
    canvas.delete('square')
    if grow >= 0 and gcol >= 0:
        a = 30 + gcol * 50
        b = 30 + grow * 50
        c = 30 + (gcol + 1) * 50
        d = 30 + (grow + 1) * 50
        canvas.create_rectangle(a,b,c,d, outline='Red', tags='square', width=2)

# user number input
def keyPressed(event):
    global grow, gcol
    if grow >=0 and gcol >=0 and event.char in '123456789':
        candidate = int(event.char)
        if unfilled[grow][gcol] == 0:
            if filled[grow][gcol] == candidate:
                unfilled[grow][gcol] = candidate
                player_game()
            else:
                tkinter.messagebox.showwarning('Game','Invalid Number')
                
        
        grow = -1
        gcol = -1

        highlight()
        # if board is filled prompt game over menu
        if 0 not in unfilled:
            game_over()


def game_over():
    global root

    minimenu = Tk()
    minimenu.title("Winner")
    congrats = Label(minimenu,text='Congratulations, you won! Would you like to play again?',font='Helvetica 18 bold')
    congrats.pack()
    exit_button = Button(minimenu,width=20,height=2,text='Exit',command=minimenu.quit)
    newgame_button = Button(minimenu,width=20,height=2,text='New Game',command=new_game)
    newgame_button.pack()
    exit_button.pack()

# rerun puzzle.py if user wants new game
def new_game():
    import sys
    import os
    os.execv(sys.executable, ['python'] + sys.argv)

    

def main():

    grid()
    game()

    canvas.bind('<Button-1>', cellClicked)
    canvas.bind('<Key>', keyPressed)

    mainloop()

if __name__ == "__main__":
    main()
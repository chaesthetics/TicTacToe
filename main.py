from tkinter import * 
from tkinter import messagebox   
import tkinter as tk

root = Tk()
root.title('TicTacToe')


e = Button(root, width=35, borderwidth=5, text='Reset')
e.grid(row=0, column=0, columnspan=3) 

# Array of pattern to become a win the game
winnerPattern = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7],   # Winner in 3 patterns
                 [1, 4, 5, 6], [1, 7, 8, 9], [1, 3, 6, 9], [1, 3, 5, 7], [1, 2, 5, 8],                     # 4 patterns in 1
                 [2, 4, 5, 6], [2, 7, 8, 9], [1, 2, 4, 7], [2, 3, 6, 9], [1, 2, 5, 9], [2, 3, 5, 7],       # 4 patterns in 2
                 [3, 4, 5, 6], [3, 7, 8, 9], [1, 3, 4, 7], [2, 3, 5, 8], [1, 3, 5, 9],                     # 4 patterns in 3
                 [1, 2, 3, 4], [4, 7, 8, 9], [2, 4, 5 ,8], [3, 4, 6, 9], [1, 4, 5 ,9], [3, 4, 5, 7],       # 4 patterns in 4
                 [1, 2, 2, 5], [5, 7, 8, 9], [1, 4, 5, 7], [3, 5, 6, 9],                                   # 4 patterns in 5
                 [1, 2, 3, 6], [6, 7, 8, 9], [1, 4, 6, 7], [2, 5, 6, 8], [1, 5, 6, 9], [3, 5, 6, 7],       # 4 patterns in 6
                 [1, 2, 3, 7], [7, 4, 5, 6], [2, 5, 7, 8], [3, 6, 7, 9], [1, 5, 7, 9],                     # 4 patterns in 7
                 [1, 2, 3, 8], [4, 5, 6, 8], [1, 4, 7, 8], [3, 6, 8, 9], [1, 5, 8, 9], [3, 5, 7, 8],      # 4 patterns in 8
                 [1, 2, 3, 9], [4, 5, 6, 9], [1, 4, 7, 9], [2, 5, 8, 9], [3, 5, 7, 9]                      # 4 patterns in 9
                ]
XInputs = [] # Inputs from X user
OInputs = [] # Inputs from O user
counter = 0 

# This function will if the Input arrays is matched in the winner pattern array
def checkWinner(): 
    OInputs.sort()
    XInputs.sort()
    print(OInputs)
    if(OInputs in winnerPattern):    
        messagebox.showinfo(title="Information", message="O USER WON THE GAME!!")
    elif(XInputs in winnerPattern):
        messagebox.showinfo(title="Information", message="X USER WON THE GAME!!")

# Function to count the click of both user
def increment():
    globals()['counter']+=1
    if(counter == 9):  messagebox.showinfo(title="Information", message=" It's A DRAW")


def buttonClick(number):
    x = ''
    color = ""
    if(counter%2==1):
        x = 'X'
        color = "red"
        XInputs.append(number)
    else:
        x = 'O'    
        color = "black"
        OInputs.append(number)
    increment()
    
    if(number==1):
        button1['state'] = tk.DISABLED
        button1['padx'] = 40.6
        button1['text'] = x
        button1['bg'] = color 
        
    elif(number==2):
        button2['state'] = tk.DISABLED
        button2['padx'] = 40.6
        button2['text'] = x
        button2['bg'] = color
    elif(number==3):
        button3['state'] = tk.DISABLED
        button3['padx'] = 40.6
        button3['text'] = x
        button3['bg'] = color
    elif(number==4):
        button4['state'] = tk.DISABLED
        button4['text'] = x
        button4['bg'] = color
        button4['padx'] = 40.6

    elif(number==5):
        button5['state'] = tk.DISABLED
        button5['text'] = x
        button5['bg'] = color
        button5['padx'] = 40.6

    elif(number==6):
        button6['state'] = tk.DISABLED
        button6['text'] = x
        button6['bg'] = color
        button6['padx'] = 40.6

    elif(number==7):
        button7['state'] = tk.DISABLED
        button7['text'] = x
        button7['bg'] = color
        button7['padx'] = 40.6

    elif(number==8):
        button8['state'] = tk.DISABLED
        button8['text'] = x
        button8['bg'] = color
        button8['padx'] = 40.6

    else:
        button9['state'] = tk.DISABLED
        button9['text'] = x
        button9['bg'] = color
        button9['padx'] = 40.6       
    checkWinner()

button1 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(1))
button2 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(2))
button3 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(3))
button4 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(4))
button5 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(5))
button6 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(6))
button7 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(7))
button8 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(8))
button9 = Button(root, text=' ', padx=50, pady=40, font=('Arial', 25), command=lambda: buttonClick(9))

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)


root.mainloop()

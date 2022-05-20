import tkinter as tk
from tkinter import font
from typing import Text
# def tictactoeGUI():
# tictactoeGUI()
topleft_text = str("")
location = ["topleft", "topmid", "topright",
            "midleft", "midmid", "midright",
            "botleft", "botmid", "botright"]
Location_value = [0, 0, 0,
                  0, 0, 0,
                  0, 0, 0]

Xlist =["left", "mid", "right"]
Ylist =["top", "mid", "bot"]
turn = 0

def end():
    if Winner["text"] == "O is the winner":
        return True
    elif Winner["text"] == "X is the winner":
        return True
    else:
        return False

def Owin():
    Winner["text"] = "O is the winner"

def Xwin():
    Winner["text"] = "X is the winner"

def sum_locations(x,y,z):
    sum = (Location_value[x]+Location_value[y]+Location_value[z])

    return sum


def win():
    if sum_locations(0, 1, 2) == 3:
        Owin()
    elif sum_locations(3,4,5) == 3:
        Owin()
    elif sum_locations(6,7,8) == 3:
        Owin()
    elif sum_locations(0,3,6) == 3:
        Owin()
    elif sum_locations(1,4,7) == 3:
        Owin()
    elif sum_locations(2,5,8) == 3:
        Owin()
    elif sum_locations(0,4,8) == 3:
        Owin()
    elif sum_locations(2,4,6) == 3:
        Owin()

    if sum_locations(0, 1, 2) == 30:
        Xwin()
    elif sum_locations(3,4,5) == 30:
        Xwin()
    elif sum_locations(6,7,8) == 30:
        Xwin()
    elif sum_locations(0,3,6) == 30:
        Xwin()
    elif sum_locations(1,4,7) == 30:
        Xwin()
    elif sum_locations(2,5,8) == 30:
        Xwin()
    elif sum_locations(0,4,8) == 30:
        Xwin()
    elif sum_locations(2,4,6) == 30:
        Xwin()

# def Convert():



# exec("%s =%a" % ((Ylist(0)+Xlist(0), ))
def O_play(loc, x):
    global Location_value
    if loc["text"] == "":
        loc["text"] = "O"
        Location_value[x] =+ 1
    else:
        print("location already occupided")

def X_play(loc, x):
    global Location_value
    if loc["text"] == "":
        loc["text"] = "X"
        Location_value[x] =+ 10
    else:
        print("location already occupided")

def topleft():
    global turn
    if turn % 2 > 0:
        O_play(topleft_btn, 0)
    elif turn % 2 ==0:
        X_play(topleft_btn, 0)
    else:
        topleft_btn["text"] = ""

def topmid():
    global turn
    if turn % 2 > 0:
        O_play(topmid_btn, 1)
    elif turn % 2 ==0:
        X_play(topmid_btn, 1)
    else:
        topmid_btn["text"] = ""

def topright():
    global turn
    global Location_value
    if turn % 2 > 0:
        O_play(topright_btn, 2)
    elif turn % 2 ==0:
        X_play(topright_btn, 2)
    else:
        topright_btn["text"] = ""

def midleft():
    global turn
    if turn % 2 > 0:
        O_play(midleft_btn, 3)
    elif turn % 2 ==0:
        X_play(midleft_btn, 3)
    else:
        midleft_btn["text"] = ""


def midmid():
    global turn
    if turn % 2 > 0:
        O_play(midmid_btn, 4)

    elif turn % 2 ==0:
        X_play(midmid_btn, 4)
    else:
        midmid_btn["text"] = ""

def midright():
    global turn
    if turn % 2 > 0:
        O_play(midright_btn, 5)
    elif turn % 2 ==0:
        X_play(midright_btn, 5)
    else:
        midright_btn["text"] = ""

def botleft():
    global turn
    if turn % 2 > 0:
        O_play(botleft_btn, 6)
    elif turn % 2 ==0:
        X_play(botleft_btn, 6)
    else:
        botleft_btn["text"] = ""


def botmid():
    global turn
    if turn % 2 > 0:
        O_play(botmid_btn, 7)

    elif turn % 2 ==0:
        X_play(botmid_btn, 7)
    else:
        botmid_btn["text"] = ""

def botright():
    global turn
    if turn % 2 > 0:
        O_play(botright_btn, 8)
    elif turn % 2 ==0:
        X_play(botright_btn, 8)
    else:
        botright_btn["text"] = ""

def C_turn():
    global turn
    turn += 1
    if turn % 2 > 0:
        currentTURN["text"] = "It is Os turn"
    elif turn % 2 ==0:
        currentTURN["text"] = "It is Xs turn"
    else:
        currentTURN["text"] = ("Error "+str(turn))

# def play_check(box):
#     box()
#     C_turn()
#     win()

window =tk.Tk()
window.title('Tic Tac Toe')

Winner = tk.Label(
    pady= 5,
    height=3,
    width=10,
    wraplength=50,
    text = "No winner yet"
    )

currentTURN = tk.Label(
    pady= 5,
    height=3,
    width=10,
    text="It is Xs turn"
)
topleft_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[topleft(), C_turn(), win()]
    )

topmid_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[topmid(), C_turn(), win()]
    )

topright_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[topright(), C_turn(), win()]
    )

midleft_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[midleft(), C_turn(), win()]
    )

midmid_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[midmid(), C_turn(), win()]
    )

midright_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[midright(), C_turn(), win()]
    )

botleft_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[botleft(), C_turn(), win()]
    )

botmid_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[botmid(), C_turn(), win()]
    )

botright_btn = tk.Button(
    width=10,
    height=5,
    bg="white",
    fg="red",
    borderwidth=1, 
    relief="solid",
    text = "",
    command=lambda:[botright(), C_turn(), win()]
    )

Title = tk.Label(
    text="TIC TAC TOE",
    font=("Arial",25),
    fg="black",
    bg="grey"
)
space = tk.Label(
    width=5,
)

space2 = tk.Label(
    width=5,
)
space3 =tk.Label(
    height=2
)

Title.grid(row=0, columnspan=5, sticky="ew")

space3.grid(row=1, column=2)

topleft_btn.grid(row=2, column=1)
topmid_btn.grid(row=2, column=2)
topright_btn.grid(row=2, column=3)

midleft_btn.grid(row=3, column=1)
midmid_btn.grid(row=3, column=2)
midright_btn.grid(row=3, column=3)

botleft_btn.grid(row=4, column=1)
botmid_btn.grid(row=4, column=2)
botright_btn.grid(row=4, column=3)

currentTURN.grid(row=6, column=1)
Winner.grid(row=6, column=3)

space.grid(row=2,column=0, sticky="e")
space2.grid(row=2,column=4, sticky="w")

window.mainloop()

User = 1
Robot = 2

topleft = 0
topmid = 0
topright = 0

midleft = 0
midmid = 0
midright = 0

botleft = 0
botmid = 0
botright = 0

Ctopleft = 0
Ctopmid = 0
Ctopright = 0

Cmidleft = 0
Cmidmid = 0
Cmidright = 0

Cbotleft = 0
Cbotmid = 0
Cbotright = 0

def computer(possition = "error"):
    print("computer choose:" + possition)

def check(var = False, var2 = False):
    if(var+var2 == 0):
        return True
    else:
        return False

def fuck():
    print("something went wrong")

def failiure():
    print("incorrecnt input")

print("top left/mid/right")
print("mid left/mid/right")
print("bot left/mid/right")

x = input("make your first play")
x = str(x)
if x == "topleft":
    topleft += User
elif x == "topmid":
    topmid += User
elif x == "topright":
    topright += User
elif x == "midleft":
    midleft += User
elif x == "midmid":
    midmid += User
elif x == "midright":
    midright += User
elif x == "botleft":
    botleft += User
elif x == "botmid":
    botmid += User
elif x == "botright":
    botright += User
else:
    failiure()

print(topleft, topmid, topright)
print(midleft, midmid, midright)
print(botleft, botmid, botright)

if midmid == 0:
    Cmidmid += Robot
    computer("midmid")
elif topleft == 0:
    Ctopleft += Robot
    computer("topleft")
elif topright == 0:
    Ctopright += Robot
    computer("topright")
elif botleft == 0:
    Cbotleft += Robot
    computer("botleft")
elif botright == 0:
    Cbotright += Robot
    computer("botright")
elif topmid == 0:
    Ctopmid += Robot
    computer("topmid")
elif botmid == 0:
    Cbotmid += Robot
    computer("botmid")
elif midleft == 0:
    Cmidleft += Robot
    computer("midleft")
elif midright == 0:
    Cmidright += Robot
    computer("midright")
else:
    fuck()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

y = input("make your second play: ")
y = str(y)
if y == "topleft":
    if check(topleft, Ctopleft):
        topleft += User
elif y == "topmid":
    if check(topmid+Ctopmid):
        topmid += User
elif y == "topright":
    if check(topright+Ctopright):
        topright += User
elif y == "midleft":
    if check(midleft+Cmidleft):
        midleft += User
elif y == "midmid":
    if check(midmid+Cmidmid):
        midmid += User
elif y == "midright":
    if check(midright+Cmidright):
        midright += User
elif y == "botleft":
    if check(botleft+Cbotleft):
        botleft += User
elif y == "botmid":
    if check(botmid+Cbotmid):
        botmid += User
elif y == "botright":
    if check(botright+Cbotright):
        botright += User
else:
    failiure()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

if   2 == (topright+topleft+topmid+Ctopright+Ctopleft+Ctopmid): # top left to right
    if 2 == (Ctopright+Ctopleft+Ctopmid):
        print("fuck")
    elif check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")
    elif check(topmid, Ctopmid):
        Ctopmid += Robot
        computer("topmid")

    elif check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")
elif 2 == (midleft+midright+midmid+Cmidleft+Cmidright+Cmidmid): # mid left to right
    if check(midleft, Cmidleft):
        Cmidleft += Robot
        computer("midleft")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(midright, Cmidright):
        Cmidright += Robot
        computer("midright")

elif 2 == (botleft+botmid+botright+Cbotleft+Cbotmid+Cbotright): #bot left to right
    if check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

    elif check(botmid, Cbotmid):
        Cbotmid += Robot
        computer("botmid")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

elif 2 == (topleft+midleft+botleft+Ctopleft+Cmidleft+Cbotleft): #left top to bottom
    if 2 == (Ctopleft+Cmidleft+Cbotleft):
        print("fuck")
        check(botleft, botleft)
        Cbotleft += Robot
        computer("botleft")

    elif check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")

    elif check(midleft, Cmidleft):
        Cmidleft += Robot
        computer("midleft")

    elif check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

    else :
        check(botleft, Cbotleft)
        Cbotleft += Robot
        computer("botleft")

elif 2 == (topmid+midmid+botmid+Ctopmid+Cmidmid+Cbotmid): #mid top to bottom
    if 2 == (Ctopleft+Cmidleft+Cbotleft):
        print("fuck")
        check(botleft, botleft)
        Cbotleft += Robot
        computer("botleft")

    elif check(topmid, Ctopmid):
        Ctopmid += Robot
        computer("topmid")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(botmid, Cbotmid):
        Cbotmid += Robot
        computer("botmid")

    else :
        check(botright, Cbotright)
        Cbotright += Robot
        computer("botright")

elif 2 == (topright+midright+botright+Ctopright+Cmidright+Cbotright): #top right to bottom
    if check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")

    elif check(midright, Cmidright):
        Cmidright += Robot
        computer("midright")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

elif 2 == (topright+midmid+botleft+Ctopright+Cmidmid+Cbotleft): #top right to bottom left
    if check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

elif 2 == (topleft+midmid+botright+Ctopleft+Cmidmid+Cbotright): #top left to bottom right   
    if check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")

    elif check(midmid, Cmidmid):
        midmid += Robot
        computer("midmid")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

else:
    fuck()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

z = input("Play your third turn: ")
z = str(z)
if z == "topleft":
    if topleft == 0:
        topleft += User
elif z == "topmid":
    if topmid == 0:
        topmid += User
elif z == "topright":
    if topright == 0:
        topright += User
elif z == "midleft":
    if midleft == 0:
        midleft += User
elif z == "midmid":
    if midmid == 0:
        midmid += User
elif z == "midright":
    if midright == 0:
        midright += User
elif z == "botleft":
    if botleft == 0:
        botleft += User
elif z == "botmid":
    if botmid == 0:
        botmid += User
elif z == "botright":
    if botright == 0:
        botright += User
else:
    failiure()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)        

if   2 == (topright+topleft+topmid+Ctopright+Ctopleft+Ctopmid): # top left to right
    if check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")
    elif check(topmid, Ctopmid):
        Ctopmid += Robot
        computer("topmid")

    elif check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")


elif 2 == (midleft+midright+midmid+Cmidleft+Cmidright+Cmidmid): # mid left to right
    if check(midleft, Cmidleft):
        Cmidleft += Robot
        computer("midleft")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(midright, Cmidright):
        Cmidright += Robot
        computer("midright")

elif 2 == (botleft+botmid+botright+Cbotleft+Cbotmid+Cbotright): #bot left to right
    if check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

    elif check(botmid, Cbotmid):
        Cbotmid += Robot
        computer("botmid")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

elif 2 == (topleft+midleft+botleft+Ctopleft+Cmidleft+Cbotleft): #left top to bottom
    if check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")

    elif check(midleft, Cmidleft):
        Cmidleft += Robot
        computer("midleft")

    elif check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

elif 2 == (topmid+midmid+botmid+Ctopmid+Cmidmid+Cbotmid): #mid top to bottom
    if 2 == (Ctopmid+Cmidmid+Cbotmid):
        print("fuck")
        check(botright, Cbotright)
        Cbotright += Robot
        computer("botright")
 
    elif check(topmid, Ctopmid):
        Ctopmid += Robot
        computer("topmid")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(botmid, Cbotmid):
        Cbotmid += Robot
        computer("botmid")

elif 2 == (topright+midright+botright+Ctopright+Cmidright+Cbotright): #top right to bottom
    if check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")

    elif check(midright, Cmidright):
        Cmidright += Robot
        computer("midright")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

elif 2 == (topright+midmid+botleft+Ctopright+Cmidmid+Cbotleft): #top right to bottom left
    if check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

elif 2 == (topleft+midmid+botright+Ctopleft+Cmidmid+Cbotright): #top left to bottom right   
    if check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")

    elif check(midmid, Cmidmid):
        midmid += Robot
        computer("midmid")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

else:
    fuck()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

a = input("Play your fourth turn: ")
a = str(a)
if a == "topleft":
    if topleft == 0:
        topleft += User
elif a == "topmid":
    if topmid == 0:
        topmid += User
elif a == "topright":
    if topright == 0:
        topright += User
elif a == "midleft":
    if midleft == 0:
        midleft += User
elif a == "midmid":
    if midmid == 0:
        midmid += User
elif a == "midright":
    if midright == 0:
        midright += User
elif a == "botleft":
    if botleft == 0:
        botleft += User
elif a == "botmid":
    if botmid == 0:
        botmid += User
elif a == "botright":
    if botright == 0:
        botright += User
else:
    failiure()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

if   2 == (topright+topleft+topmid+Ctopright+Ctopleft+Ctopmid): # top left to right
    if check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")

    elif check(topmid, Ctopmid):
        Ctopmid += Robot
        computer("topmid")

    elif check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")


elif 2 == (midleft+midright+midmid+Cmidleft+Cmidright+Cmidmid): # mid left to right
    if check(midleft, Cmidleft):
        Cmidleft += Robot
        computer("midleft")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(midright, Cmidright):
        Cmidright += Robot
        computer("midright")

elif 2 == (botleft+botmid+botright+Cbotleft+Cbotmid+Cbotright): #bot left to right
    if check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

    elif check(botmid, Cbotmid):
        Cbotmid += Robot
        computer("botmid")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

elif 2 == (topleft+midleft+botleft+Ctopleft+Cmidleft+Cbotleft): #left top to bottom
    if check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")

    elif check(midleft, Cmidleft):
        Cmidleft += Robot
        computer("midleft")

    elif check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

elif 2 == (topmid+midmid+botmid+Ctopmid+Cmidmid+Cbotmid): #mid top to bottom
    if check(topmid, Ctopmid):
        Ctopmid += Robot
        computer("topmid")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(botmid, Cbotmid):
        Cbotmid += Robot
        computer("botmid")

elif 2 == (topright+midright+botright+Ctopright+Cmidright+Cbotright): #right top to bottom
    if check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")

    elif check(midright, Cmidright):
        Cmidright += Robot
        computer("midright")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

elif 2 == (topright+midmid+botleft+Ctopright+Cmidmid+Cbotleft): #top right to bottom left
    if check(topright, Ctopright):
        Ctopright += Robot
        computer("topright")

    elif check(midmid, Cmidmid):
        Cmidmid += Robot
        computer("midmid")

    elif check(botleft, Cbotleft):
        Cbotleft += Robot
        computer("botleft")

elif 2 == (topleft+midmid+botright+Ctopleft+Cmidmid+Cbotright): #top left to bottom right   
    if check(topleft, Ctopleft):
        Ctopleft += Robot
        computer("topleft")

    elif check(midmid, Cmidmid):
        midmid += Robot
        computer("midmid")

    elif check(botright, Cbotright):
        Cbotright += Robot
        computer("botright")

else:
    fuck()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

b = input("Play your another turn: ")
b = str(b)
if b == "topleft":
    if topleft == 0:
        topleft += User
elif b == "topmid":
    if topmid == 0:
        topmid += User
elif b == "topright":
    if topright == 0:
        topright += User
elif b == "midleft":
    if midleft == 0:
        midleft += User
elif b == "midmid":
    if midmid == 0:
        midmid += User
elif b == "midright":
    if midright == 0:
        midright += User
elif b == "botleft":
    if botleft == 0:
        botleft += User
elif b == "botmid":
    if botmid == 0:
        botmid += User
elif b == "botright":
    if botright == 0:
        botright += User
else:
    failiure()

print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

if(topleft+Ctopleft+topmid+Ctopmid+topright+Ctopright+midleft+Cmidleft+midmid+Cmidmid+midright+Cmidright+botleft+Cbotleft+botmid+Cbotmid+botright+Cbotright) == 13:
    print("THE END")
    print("No One Wins!!!")
    print("congrats on wasting your fucking time!")
else:
    if   2 == (topright+topleft+topmid+Ctopright+Ctopleft+Ctopmid): # top left to right
        if check(topleft, Ctopleft):
            Ctopleft += Robot
            computer("topleft")

        elif check(topmid, Ctopmid):
            Ctopmid += Robot
            computer("topmid")

        elif check(topright, Ctopright):
            Ctopright += Robot
            computer("topright")


    elif 2 == (midleft+midright+midmid+Cmidleft+Cmidright+Cmidmid): # mid left to right
        if check(midleft, Cmidleft):
            Cmidleft += Robot
            computer("midleft")

        elif check(midmid, Cmidmid):
            Cmidmid += Robot
            computer("midmid")

        elif check(midright, Cmidright):
            Cmidright += Robot
            computer("midright")

    elif 2 == (botleft+botmid+botright+Cbotleft+Cbotmid+Cbotright): #bot left to right
        if check(botleft, Cbotleft):
            Cbotleft += Robot
            computer("botleft")

        elif check(botmid, Cbotmid):
            Cbotmid += Robot
            computer("botmid")

        elif check(botright, Cbotright):
            Cbotright += Robot
            computer("botright")

    elif 2 == (topleft+midleft+botleft+Ctopleft+Cmidleft+Cbotleft): #left top to bottom
        if check(topleft, Ctopleft):
            Ctopleft += Robot
            computer("topleft")

        elif check(midleft, Cmidleft):
            Cmidleft += Robot
            computer("midleft")

        elif check(botleft, Cbotleft):
            Cbotleft += Robot
            computer("botleft")

    elif 2 == (topmid+midmid+botmid+Ctopmid+Cmidmid+Cbotmid): #mid top to bottom
        if check(topmid, Ctopmid):
            Ctopmid += Robot
            computer("topmid")

        elif check(midmid, Cmidmid):
            Cmidmid += Robot
            computer("midmid")

        elif check(botmid, Cbotmid):
            Cbotmid += Robot
            computer("botmid")

    elif 2 == (topright+midright+botright+Ctopright+Cmidright+Cbotright): #right top to bottom
        if check(topright, Ctopright):
            Ctopright += Robot
            computer("topright")

        elif check(midright, Cmidright):
            Cmidright += Robot
            computer("midright")

        elif check(botright, Cbotright):
            Cbotright += Robot
            computer("botright")

    elif 2 == (topright+midmid+botleft+Ctopright+Cmidmid+Cbotleft): #top right to bottom left
        if check(topright, Ctopright):
            Ctopright += Robot
            computer("topright")

        elif check(midmid, Cmidmid):
            Cmidmid += Robot
            computer("midmid")

        elif check(botleft, Cbotleft):
            Cbotleft += Robot
            computer("botleft")

    elif 2 == (topleft+midmid+botright+Ctopleft+Cmidmid+Cbotright): #top left to bottom right   
        if check(topleft, Ctopleft):
            Ctopleft += Robot
            computer("topleft")

        elif check(midmid, Cmidmid):
            midmid += Robot
            computer("midmid")

        elif check(botright, Cbotright):
            Cbotright += Robot
            computer("botright")

    else:
        fuck()

    print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
    print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
    print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

    b = input("Play your last turn: ")
    b = str(b)
    if b == "topleft":
        if topleft == 0:
            topleft += User
    elif b == "topmid":
        if topmid == 0:
            topmid += User
    elif b == "topright":
        if topright == 0:
            topright += User
    elif b == "midleft":
        if midleft == 0:
            midleft += User
    elif b == "midmid":
        if midmid == 0:
            midmid += User
    elif b == "midright":
        if midright == 0:
            midright += User
    elif b == "botleft":
        if botleft == 0:
            botleft += User
    elif b == "botmid":
        if botmid == 0:
            botmid += User
    elif b == "botright":
        if botright == 0:
            botright += User
    else:
        failiure()

    print(topleft+Ctopleft, topmid+Ctopmid, topright+Ctopright)
    print(midleft+Cmidleft, midmid+Cmidmid, midright+Cmidright)
    print(botleft+Cbotleft, botmid+Cbotmid, botright+Cbotright)

    if(topleft+Ctopleft+topmid+Ctopmid+topright+Ctopright+midleft+Cmidleft+midmid+Cmidmid+midright+Cmidright+botleft+Cbotleft+botmid+Cbotmid+botright+Cbotright) == 13:
        print("THE END")
        print("No One Wins!!!")
        print("congrats on wasting your fucking time!")
    else:
        print("somethingwent to shit")
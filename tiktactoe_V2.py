user = 1
robot = 10

tick = [0, 0, 0, 0, 0, 0, 0, 0, 0]
tack = ["topleft", "topmid", "topright", 
       "midleft", "midmid", "midright", 
       "botleft", "botmid", "botright"]

def failiure():
    print("incorrecnt input")

def fuck():
    print("something went wrong")

def update(array):
    i = 0
    while i <= 6:
        print(array[i], " ", array[i+1], " ", array[i+2])
        i+=3

def computer(possition = "error"):
    print("Computer Choose: " + possition)

def check(var):
    if(var == 0):
        return True
    else:
        return False

def player(tick, tack):
    y = input("Please play your turn: ")
    y = str(y)
    x = 0
    while x <= 8:
        if y == tack[x]:
            if check(tick[x]):
                tick[x] += user
                break
        else:
            x+=1
    
def sum(one, two, three, tick):
    x=0
    x = tick[one] + tick[two] + tick[three]
    return x

def calc_p2(priority, temp, x):
    if  20== temp: # two cpu 
        priority[x] = 25
    elif 12 == temp: # full
        priority[x] = 0
    elif 21 == temp: # full
        priority[x] = 0
    elif 2 == temp: # two user
        priority[x] = 20
    elif 1 == temp:
        priority[x] = 10
    elif 10 == temp:
        priority[x] = 15
    elif 11 == temp:
        priority[x] = 5
    else:
        failiure()

def calc_p(priority, tick):
    if 0 < sum(0, 1, 2, tick): # priority location 1, TOP left to right
        temp = sum(0, 1, 2, tick)
        calc_p2(priority,temp, 9)

    if 0 < sum(3, 4, 5, tick): # priority location 2, MID left to right
        temp2 = sum(3, 4, 5, tick)
        calc_p2(priority,temp2, 8)

    if 0 < sum(6, 7, 8, tick): # priority location 3, BOT left to right
        temp3 = sum(6, 7, 8, tick)
        calc_p2(priority,temp3, 2)

    if 0 < sum(0, 3, 6, tick): # priority location 4,  LEFT top to bottom
        temp4 = sum(0, 3, 6, tick)
        calc_p2(priority,temp4, 3)
        
    if 0 < sum(1, 4, 7, tick): # priority location 5, MID top to bottom
        temp5 = sum(1, 4, 7, tick)
        calc_p2(priority,temp5, 4)
        
    if 0 < sum(2, 5, 8, tick): # priority location 6, RIGHT top to bottom
        temp6 = sum(2, 5, 8, tick)
        calc_p2(priority,temp6, 5)
        
    if 0 < sum(0, 4, 8, tick): # priority location 7, DIAGONAL top left to bottom right
        temp7 = sum(8, 4, 0, tick)
        calc_p2(priority,temp7, 6)
        
    if 0 < sum(2, 4, 6, tick): # priority location 8, DIAGONAL top right to bottom left
        temp8 = sum(6, 4, 2, tick)
        calc_p2(priority,temp8, 7)

    if 0 < sum(2, 6, 8, tick): # priority location 9, botleft, botright, topright
        temp9 = sum(2, 6, 8, tick)
        calc_p2(priority,temp9, 0)
        if priority[4] == 0:
            calc_p2(priority, temp5, 0)
    
    if 0 < sum(0, 2, 6, tick): # priority location 10, botleft, botright, topright
        temp10 = sum(0, 2, 6, tick)
        calc_p2(priority,temp10, 1)
        if priority[1] == 0:
            calc_p2(priority, temp2, 1)
        
def bubblesort(arr, arr2):
    n = len(arr)
  
    for i in range(n):
  
        for j in range(0, n-i-1):
  
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

def c_play2(x, y, z, tick, tack, robot):
    if check(tick[y]):
        tick[y] += robot
        computer(tack[y])
    elif check(tick[x]):
        tick[x] += robot
        computer(tack[x])
    elif check(tick[z]):
        tick[z] += robot
        computer(tack[z])
    elif check(tick[8]):
        tick[8] += robot
        computer(tack[8])
    else:
        a = 0
        while a<=8:
            if check(tick[a]):
                tick[a] += robot
                computer(tack[z])
                break
            else:
                a+=1
    # else:
    #     print("Error 001")

def c_play(tick, tack, priotity2, robot):
    if priotity2[9] == 9:
        c_play2(0,1,2, tick, tack, robot)

    elif priotity2[9] == 8:
        c_play2(3,4,5, tick, tack, robot)

    elif priotity2[9] == 2:
        c_play2(6,7,8, tick, tack, robot)

    elif priotity2[9] == 3:
        c_play2(0,3,6, tick, tack, robot)

    elif priotity2[9] == 4:
        c_play2(1,4,7, tick, tack, robot)
        
    elif priotity2[9] == 5:
        c_play2(2,5,8, tick, tack, robot)
    
    elif priotity2[9] == 6:
        c_play2(0,4,8, tick, tack, robot)    
    
    elif priotity2[9] == 7:
        c_play2(2,4,6, tick, tack, robot)

    elif priotity2[9] == 0:
        c_play2(1,4,7, tick, tack, robot)

    elif priotity2[9] == 1:
        c_play2(3,4,5, tick, tack, robot)
    else:
        print("Error 002")


def cwin():
    return "Computer Wins"

def pwin():
    return "Player Wins"

def fix(tick):
    y = 0
    x = 0
    while x <= len(tick)-1:
        y += tick[x]
        x += 1
    if 45 == y:
        return True
    else:
        return False

def win2(temp):
    if  30== temp: 
        cwin()
        return True
    elif 3 == temp: 
        pwin()
        return True
    else:
        return False    

def win(tick):
    if 2 < sum(0, 1, 2, tick): 
        temp = sum(0, 1, 2, tick)
        if win2(temp):
            return True
        
    if 2 < sum(3, 4, 5, tick): 
        temp2 = sum(3, 4, 5, tick)
        if win2(temp2):
            return True

    if 2 < sum(6, 7, 8, tick):
        temp3 = sum(6, 7, 8, tick)
        if win2(temp3):
            return True

    if 2 < sum(0, 3, 6, tick):
        temp4 = sum(0, 3, 6, tick)
        if win2(temp4):
            return True

    if 2 < sum(1, 4, 7, tick):
        temp5 = sum(1, 4, 7, tick)
        if win2(temp5):
            return True

    if 2 < sum(2, 5, 8, tick): 
        temp6 = sum(2, 5, 8, tick)
        if win2(temp6):
            return True

    if 2 < sum(0, 4, 8, tick): 
        temp7 = sum(0, 4, 8, tick)
        if win2(temp7):
            return True

    if 2 < sum(2, 4, 6, tick): 
        temp8 = sum(2, 4, 6, tick)
        if win2(temp8):
            return True

# START-------------------------------------------------------------------------------------------------------------------------

print("top left/mid/right")
print("mid left/mid/right")
print("bot left/mid/right")

player(tick, tack) # ROUND 1---------------------------------------------------------------------------------------------

update(tick)

if tick[4] == 0:
   tick[4] += robot
   computer("midmid")
elif tick[0] == 0:
    tick[0] += robot
    computer("topleft")
elif tick[2] == 0:
    tick[2] += robot
    computer("topright")
elif tick[1] == 0:
    tick[1] += robot
    computer("topmid")
elif tick[3] == 0:
    tick[3] += robot
    computer("midleft")
elif tick[5] == 0:
    tick[5] += robot
    computer("midright")
elif tick[6] == 0:
    tick[6] += robot
    computer("botleft")
elif tick[7] == 0:
    tick[7] += robot
    computer("botmid")
elif tick[8] == 0:
    tick[8] += robot
    computer("botright")
else:
    fuck()

update(tick) # ROUND 2-------------------------------------------------------------------------------------------------

i = 0
while i < 1:

    player(tick, tack)

    update(tick) # ROUND 3---------------------------------------------------------------------------------------------

    if (win(tick)):
        print("GAME OVER!!")
        break

    priority = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    priotity2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    calc_p(priority, tick)
    bubblesort(priority, priotity2)
    # print(priority) #de bugging information
    # print(priotity2)
    # print(tack)
    c_play(tick, tack, priotity2, robot)

    update(tick) # ROUND 4---------------------------------------------------------------------------------------------

    if (win(tick)):
        print("GAME OVER!!")
        break
    if fix(tick):
        print("Game Ended In a tie, Congratulations on wasting your time")
        break
# Repeat Past rounds until game ends-----------------------------------------------------------------------------------

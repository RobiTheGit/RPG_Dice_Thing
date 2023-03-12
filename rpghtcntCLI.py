#!/usr/bin/python3
import random

def Average(lst):
    return sum(lst) / len(lst)
    
def main():
    global luck
    global mini
    global maxi
    global numlist 
    global temptnumlist 
    global mods
    global lucktype
    global die
    luck = input("Is luck True or False: ")
    if luck.upper() == "TRUE":
        luck = True
        lucktype = input("Enter 1 if luck only removes 1's, if it removes 1's and 2's, input 2: ")
        if lucktype == "1":
            lucktype = 1
        elif lucktype == '2':
            lucktype = 2
        else:
            lucktype = 1
            
        print(lucktype)
    die = input('dice to roll: ')
    mini = input("minimum number for the die: ")
    maxi = input("maximun number for the die: ")
    try:
        die = int(die)
        if die > 100:
            die = 100
    except:
        die = 1
    try:
        mini = int(mini)
    except:
        mini = 1
    try:
        maxi = int(maxi)
    except:
        maxi = 6
    
    mods = input("Roll modifiers ")
    try:
        mods = int(mods)
    except:
        mods = 0
    numlist = []
    temptnumlist = []  
    global x
    x = 0        
    while x != 100:
        for y in range(die):
            while len(temptnumlist) != die:
                num = random.randint(mini,maxi)
                if luck == True:
                    if lucktype == 1:
                        if num == 1:
                           num = random.randint(mini,maxi)
                           temptnumlist.append(num)
                        else:
                            temptnumlist.append(num)
                    if lucktype == 2:
                        if num == 1 or num == 2:
                            num = random.randint(mini,maxi)
                            temptnumlist.append(num)
                        else:
                            temptnumlist.append(num) 
                else:
                    temptnumlist.append(num)
        
        num = sum(temptnumlist)
        num += mods
        numlist.append(num)
        temptnumlist.clear()
        x += 1
    print('Rolls:')
    print(numlist, len(numlist))
    average = Average(numlist)
    print('Your average hit roll is', average)
if __name__ == '__main__':
    main()

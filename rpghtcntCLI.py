#!/usr/bin/python3
import random

def Average(lst):
    return sum(lst) / len(lst)
    
def remove1():
    try:
        numlist.remove(1)
        remove1()
    except:
        if lucktype == 2:
            remove2()
        else:
            finalize()
        
def remove2():
    try:
        numlist.remove(2)
        remove2()
    except:
        finalize() 
        
def finalize():  
    while len(numlist) != 100:
        num = random.randint(mini,maxi)
        num += mods
        numlist.append(num)
def main():
    global luck
    global mini
    global maxi
    global r1 
    global r2 
    global numlist 
    global mods
    global lucktype
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
    mini = input("minimum number for the die: ")
    maxi = input("maximun number for the die: ")
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
    global x
    x = 0        
    while x != 100:
        num = random.randint(mini,maxi)
        num += mods
        numlist.append(num)
        x += 1
    print('Normal Rolls:')
    print(numlist, len(numlist))
    average = Average(numlist)
    print('Your average hit role is', average)

    if luck == True:
        remove1()
        print('With Lucky:')
        print(numlist, len(numlist))
        average = Average(numlist)
        print('Your average hit role is', average)
    else:
        pass
if __name__ == '__main__':
    main()

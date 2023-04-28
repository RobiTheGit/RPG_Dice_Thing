import random
import rpghitcnt
import re
#This is just doing all of the math for the gui version, please don't run this on it's own, it wont do anything if you do, well acutally it will, but you wouldn't be able to tell
#Basically, it would run the simulation with the deaults, and no output, I have tested it
global opt
opt = ''
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
    global toroll
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
    try:
        mods = int(mods)
    except:
        mods = 0
    numlist = []
    temptnumlist = []     
    global x
    x = 0   
    try:
        toroll = abs(int(toroll))
        if toroll > 100:
            toroll = 100
    except:
        toroll = 1     
    while x != toroll:
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
    normal = 'Rolls:'
    numbers = f'{numlist} {len(numlist)}'
    average = Average(numlist)
    averageoutput = f'Your average hit roll is {re.sub(".0", "", str(round(average, 0)))}'
    global opt
    opt = f"""
{normal}
{numbers}
{averageoutput}
    
    """

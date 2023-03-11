import random
import rpghitcnt
#This is just doing all of the math for the gui version, please don't run this on it's own, it wont do anything if you do
global opt
global opt2
opt = ''
opt2 = ''
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
    try:
        die = int(die)
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
    normal = 'Rolls:'
    numbers = f'{numlist} {len(numlist)}'
    average = Average(numlist)
    averageoutput = f'Your average hit roll is {average}'
    global opt
    opt = f"""
{normal}
{numbers}
{averageoutput}
    
    """

import random
import rpghitcnt
#This is just doing all of the math for the gui version, please don't run this on it's own, it wont do anything if you do
global opt
global opt2
opt = ''
opt2 = ''
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
    global x
    x = 0        
    while x != 100:
        num = random.randint(mini,maxi)
        num += mods
        numlist.append(num)
        x += 1
    normal = 'Normal Rolls:'
    numbers = f'{numlist} {len(numlist)}'
    average = Average(numlist)
    averageoutput = f'Your average hit role is {average}'
    global opt
    opt = f"""
{normal}
{numbers}
{averageoutput}
    
    """
    if luck == True:
        remove1()
        withluck = 'With Lucky:'
        numbers2 = f'{numlist} {len(numlist)}'
        average2 = Average(numlist)
        averageoutput2 = f'Your average hit role is {average2}'
        global opt2
        opt2 = f"""
{withluck}
{numbers2}
{averageoutput2}
    
    """
    else:
        pass

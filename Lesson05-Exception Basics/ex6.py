import random

'''
TODO: define exception classes
'''
class HungryException(Exception):
    def __init__(self,hger):
        self.hger = str(hger)
    def __str__(self):
        return "I'm hungry(Status:" + self.hger +"),need to eat!"
class ThirstyException(Exception):
    def __init__(self,trsty):
        self.trsty = str(trsty)
    def __str__(self):
        return "I'm tirsty(Status:" + self.trsty +"),need to drink!"
class BoredException(Exception):
    def __init__(self,bor):
        self.bor = str(bor)
    def __str__(self):
        return "I'm boring(Status:" + self.bor +"),need to play!"
def check(man):
    # TODO: in what condition need to raise exception?
    if man["hunger"] < 0:
        raise HungryException(man["hunger"])
    if man["water"] < 0:
        raise ThirstyException(man["water"])
    if man["mood"] < 0:
        raise BoredException(man["mood"])
    
def play(man):
    print("playing...")
    man["hunger"] -= 15
    man["water"] -= 15
    man["mood"] += 5
    check(man)
def eat(man):
    print("eating...")
    man["hunger"] += 5
    check(man)
def drink(man):
    print("drinking...")
    man["water"] += 5
    check(man)
    
actionList = [play, eat, drink]
    
child = {"hunger": 20, "water": 20, "mood": 20}

while True:
    #cnt -= 1
    rand = random.randint(0,2)
    try:
    # TODO: 把隨機的動作用 try...except 包起來   
        actionList[rand](child)
    except HungryException as e:
        #raise HungryException()
        print(e)
        print('eating...')
        break
    except ThirstyException as e:
        #raise ThirstyException
        print(e)
        print('drinking...')
        break
    except BoredException as e:
        #raise BoredException
        print(e)
        print('playing...')
        break

    # TIPS: 記得只要抓到 exception 之後就要 break 了，不然會造成無窮迴圈
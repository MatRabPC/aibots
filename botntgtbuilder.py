from graphics import *
import random
import math

'''
Building Stuff
'''

def buildbot(win, clr):
    bot = Circle(Point(random.randint(5,15), random.randint(5,15)), radius = 1)
    bot.setFill(clr)
    bot.setOutline('white')
    bot.draw(win)

    return bot

def buildtgt(win, clr):

    tgt = Circle(Point(random.randint(5,15), random.randint(5,15)), radius = 1)
    tgt.setFill('#000')
    tgt.setOutline(clr)
    tgt.draw(win)

    return tgt


def btfactory(win, colours, nobot, notgt):

    botlot = [None] * nobot
    tgtlot = [None] * (nobot * notgt)
    loclist = list()

    tgtlot[0] = buildtgt(win, colours[0])

    for i in range(nobot):
        for j in range(1, notgt):
            tgtlot[j] = buildtgt(win, colours[i])
            loclist.append(tgtlot[j].getCenter())

        #    print loclist
         #   print tgtlot[i].getCenter()

            while tgtlot[i] in loclist: # or loopinters(tgtlot[i], loclist) :
                tgtlot[j].undraw()
                tgtlot[j] = buildtgt(win, colours[i])
                loclist.pop()
                print 'popped'
                loclist.append(tgtlot[j].getCenter())

        if i < notgt-1:
            tgtlot[i+notgt] = buildtgt(win, colours[i+1])

    for i in range(nobot):
        botlot[i] = buildbot(win, colours[i])

        while botlot[i].getCenter() in loclist:
            botlot[j] = buildbot(win, colours[i])
            loclist.pop()
            loclist.append(tgtlot[j].getCenter())

    print loclist

    return botlot, tgtlot



def noncollinit(bots, tgts):

    botco = [(0,0)] * len(bots)
    tgtco = [(0,0)] * len(tgts)

    for i in range(len(bots)):
        botco[i] = bots[i].getCenter()

    for i in range(len(tgts)):
        tgtco[i] = tgts[i].getCenter()

    for i in range(len(bots)):
     #   if botco[i] in tgtco
        pass


'''
functions
'''

def loopinters(obj, lst):

    for i in range(len(lst)):
        if objinter(obj.getCenter(), lst[i], 2):
            return True

    return False


def objinter(obj1, obj2, r):

    distance = ((obj1.getX() - obj2.getX()) ** 2 + (obj1.getY() - obj2.getY()) ** 2) ** 0.5

    return distance < r + r
'''
    r0 = r
    r1 = r
    x0,y0 = obj1.getX(), obj1.getY()
    x1,y1 = obj2.getX(), obj2.getY()

    return math.hypot(x0 - x1, y0 - y1) <= (r0 + r1)
'''

def colDetSense(obj1, obj2):

    dist = math.sqrt((obj1.getCenter().getX() - obj2.getCenter().getX()) ** 2 + (
    obj1.getCenter().getY() - obj2.getCenter().getY()) ** 2)

    if dist <= 1:
        if obj1.config["fill"] == obj2.config["outline"]:
            return True

    return False



def safeMovBotRandom(bot, sizeof):
    # randomize movement, check if within border until safe to move
    xstep = randMov()
    ystep = randMov()

    while (not checkMovLegal(xstep + bot.getCenter().getX(), ystep + +bot.getCenter().getY(), sizeof)):
        xstep = randMov()
        ystep = randMov()

    bot.move(xstep, ystep)


def checkMovLegal(x, y, sizeof):
    #the +2 is to accomodate for the radius of the bot
    if x < 0+2 or x > sizeof-2 or y < 0+2 or y > sizeof-2:
        return False
    else:
        return True


def drawCoorsOnBot(x, y, win):
    label = Text(Point(x, y), str(x)+","+str(y))
    label.setFill("white")
    label.draw(win)


# return either -1, 0 or 1
def randMov():
    rn = random.randint(-1, 1)
    return rn


#get robot co-ordinates
def updateBot(bot):
    rX = bot.getCenter().getX()
    rY = bot.getCenter().getY()
    return rX, rY



#########################
#return random coordinates in the window
def randSpawn(limit):
    rn = random.randint(0, limit)
    return rn

#return x and y position of circle objects
def updateCo(obj):
    oX = obj.getCenter().getX()
    oY = obj.getCenter().getY()
    return oX, oY


#detect collision
def colDet(obj1, obj2):
    dist = math.sqrt((obj1.getCenter().getX() - obj2.getCenter().getX()) ** 2 + (obj1.getCenter().getY() - obj2.getCenter().getY()) ** 2)
    return dist


#get target co-ordinates
def updateTgt(tgt):
    tX = tgt.getCenter().getX()
    tY = tgt.getCenter().getY()
    return tX, tY
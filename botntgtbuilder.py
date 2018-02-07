from graphics import *
import random
import math

'''
Building Stuff
'''

def buildbotr(win, clr, x, y):
    bot = Circle(Point(x, y), radius = 1)
    bot.setFill(clr)
    bot.setOutline('white')
    bot.draw(win)

    return bot

def buildtgtr(win, clr, x, y):

    tgt = Circle(Point(x, y), radius = 1)
    tgt.setFill('#000')
    tgt.setOutline(clr)
    tgt.draw(win)

    return tgt


def aifactory(win, colours, nobot, notgt):

    lower = 0
    upper = win.getHeight()
    botlot = [None] * nobot
    tgtlot = [None] * (nobot * notgt)
    loclist = list()
    xtemp = -1
    ytemp = -1
    tgton = 0

    for i in range(nobot):
        for j in range(notgt):
            while xtemp < 0:
                xtemp = random.randint(3, 10)
                ytemp = random.randint(3, 10)

               # print (xtemp, ytemp)[0]

                if (xtemp, ytemp) in loclist or loopinters((xtemp, ytemp), loclist):
                    xtemp = -1
                    ytemp = -1

            tgtlot[tgton] = buildtgtr(win, colours[i], xtemp, ytemp)
            loclist.append((tgtlot[j+i].getCenter().getX(), tgtlot[j+i].getCenter().getY()))
            tgton += 1
            print "Appened", tgtlot[j+i]
            print tgtlot
            xtemp = -1
            ytemp = -1

    print tgtlot

    for i in range(nobot):
        while xtemp < 0:
            xtemp = random.randint(3, 10)
            ytemp = random.randint(3, 10)



            if (xtemp, ytemp) in loclist or loopinters((xtemp, ytemp), loclist):
                xtemp = -1
                ytemp = -1
                print loclist, xtemp  # (xtemp, ytemp)[0]

        botlot[i] = buildbotr(win, colours[i], xtemp, ytemp)
        loclist.append((botlot[i].getCenter().getX(), botlot[i].getCenter().getY()))
        xtemp = -1
        ytemp = -1
        #botlot[i] = buildbot(win, colours[i])

    print tgtlot

    return botlot, tgtlot


'''
functions
'''

def loopinters(obj, lst):

    for i in range(len(lst)):
        if pointinter(obj, lst[i], 1):
        #if objinter(obj.getCenter(), lst[i], 2):
            return True
    return False

def pointinter(obj1, obj2, r):

    distance = ((obj1[0] - obj2[0]) ** 2 + (obj1[1] - obj2[1]) ** 2) ** 0.5
    return distance < r + r


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


# return either -1, 0 or 1
def randMov():
    rn = random.randint(-1, 1)
    return rn


#get robot co-ordinates
def updateBot(bot):
    rX = bot.getCenter().getX()
    rY = bot.getCenter().getY()
    return rX, rY


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
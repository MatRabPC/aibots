from graphics import *
import random
import math

'''
Building Stuff
'''

def buildbot(win, clr):

    #bot = Circle(Point(5,5), radius = 1)
    bot = Circle(Point(random.randint(5,10), random.randint(5,10)), radius = 1)
    bot.setFill(clr)
    bot.setOutline('white')
    #bot = Image(Point(5, 5), 'aibot.gif')
    bot.draw(win)
    return bot

def buildtgt(win, clr):

    tgt = Circle(Point(random.randint(5,10), random.randint(5,10)), radius = 1)
    tgt.setFill('white')
    tgt.setOutline(clr)
    tgt.draw(win)

    return tgt


'''
functions
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


'''
all target stuff
'''

def buildtgt(win, clr):

    tgt = Circle(Point(random.randint(5,10), random.randint(5,10)), radius = 1)
    tgt.setFill('white')
    tgt.setOutline(clr)
    tgt.draw(win)

    return tgt

#get target co-ordinates
def updateTgt(tgt):
    tX = tgt.getCenter().getX()
    tY = tgt.getCenter().getY()
    return tX, tY
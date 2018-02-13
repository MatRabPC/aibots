from graphics import *
from spillfunctions import *
import random
import math

tgtradius = 1
botradius = 1

'''
Building Stuff
'''


#builds bot
class Bots(object):
    visited = []
    tgts = 0
    bot = None
    config = []

    # The class "constructor" - It's actually an initializer
    def __init__(self, win, clr, x, y, notgts):
        self.bot = Circle(Point(x, y), radius=botradius)
        self.bot.setFill(clr)
        self.bot.setOutline('white')
        self.bot.draw(win)
        self.visited.append([x,y])
        self.tgts = notgts
        self.config = self.bot.config

    def getCenter(self):
        return self.bot.getCenter()

    def move(self, x, y):
        return self.bot.move(x, y)

def make_bot(win, clr, x, y, notgts):
    bot = Bots(win, clr, x, y, notgts)
    return bot


''''''
#build target
def buildtgtr(win, clr, x, y):

    tgt = Circle(Point(x, y), radius = tgtradius)
    tgt.setFill('#000')
    tgt.setOutline(clr)
    tgt.draw(win)

    return tgt

''''''
#attempts to build all required targets and bots without them spawning on top of each other/illegally
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

        botlot[i] = make_bot(win, colours[i], xtemp, ytemp, notgt)
        loclist.append((botlot[i].bot.getCenter().getX(), botlot[i].bot.getCenter().getY()))
        xtemp = -1
        ytemp = -1
        #botlot[i] = buildbot(win, colours[i])

    print tgtlot

    return botlot, tgtlot


'''
functions
'''
#checks if the target we found belongs to the bot--if true, picks up and removes target, lowers Bot tgt counter--
# if false, returns false (so that, if there is a communication channel, we can tell the other bots what we found)
def checkTargetFound(bot, tgtlot, tgtloclist):

    if (getLoc(bot) in tgtloclist) and (
        tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] == bot.config["fill"]):

        print('target found')
        tgtlot[tgtloclist.index(getLoc(bot))].undraw()
        tgtlot.pop(tgtloclist.index(getLoc(bot)))
        tgtloclist.pop(tgtloclist.index(getLoc(bot)))
        bot.tgts = bot.tgts - 1

        return True
    return False #return tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] #returns target outline colour


#checks if movement is within bounds
def safeMovBotRandom(bot, sizeof):
    # randomize movement, check if within border until safe to move
    xstep = randMov()
    ystep = randMov()

    while ( ( not checkMovLegal(xstep + bot.getCenter().getX(), ystep + +bot.getCenter().getY(), sizeof) ) and ( not checkVisited(bot, xstep + bot.getCenter().getX(), ystep + +bot.getCenter().getY())) ):
        xstep = randMov()
        ystep = randMov()

    return xstep, ystep


#supposed to add location to list of visited locations, then move. to be fixed
def checkLoc(bot, xstep, ystep): #needs adjustment

    bot.visited.append((xstep, ystep))
    bot.move(xstep, ystep)


# return either -1, 0 or 1
def randMov():
    rn = random.randint(-1, 1)
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


def checkVisited(bot, x, y):

   # print bot.visited
    print (x,y)

    if (x, y) in bot.visited:
        return True

    return False


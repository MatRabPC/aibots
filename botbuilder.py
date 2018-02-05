from graphics import *
import random
#from tgtbuilder import updateTgt

'''
All bot stuff
'''

def buildbot(win, clr):

    bot = Circle(Point(5,5), radius = 1)
    bot.setFill(clr)
    bot.setOutline('white')

    #bot = Image(Point(5, 5), 'aibot.gif')

    bot.draw(win)

    return bot

##################
def safeMovBotRandom(bot, sizeof):
    # randomize movement, check if within border until safe to move
    xstep = randMov()
    ystep = randMov()

    while (not checkMovLegal(xstep + bot.getCenter().getX(), ystep + +bot.getCenter().getY(), sizeof)):
        xstep = randMov()
        ystep = randMov()

    #label.undraw(win)
    bot.move(xstep, ystep)
    #label = Text(Point(xstep + bot.getCenter().getX(), ystep + +bot.getCenter().getY()), str(xstep) + "," + str(ystep))
    #label.setFill("white")
    #label.draw(win)


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


######

# return either -1, 0 or 1
def randMov():
    rn = random.randint(-1, 1)
    return rn


#get robot co-ordinates
def updateBot(bot):
    rX = bot.getCenter().getX()
    rY = bot.getCenter().getY()
    return rX, rY


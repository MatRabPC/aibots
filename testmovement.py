#TODO - make simulation terminate after an event as opposed to time
#TODO - implement Samina's changes
#TODO - collision detection with multiple targets drawn?
from graphics import *
import simpy
import random
import math



"""
DEFINE VARIABLES AND METHODS
"""


env = simpy.rt.RealtimeEnvironment(factor=0.1) #movement time
winXLL = 0
winYLL = 0
winXUR = 30 #height of the window
winYUR = 30 # width of the window
totalruntime = 70 #amount of steps the system will run for
timestep = 1 #step size
tgtradius = 0.5
botradius = 1


# return either -1, 0 or 1
def randMov():
    rn = random.randint(-1, 1)
    return rn

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



"""
CREATE VISUALS
"""


#create window
win = GraphWin('MaSaAn Bots', width = 800, height = 800) #Create window
win.setCoords(winXLL, winYLL, winXUR, winYUR) #set window coords by (x lower left, y lower left, x upper right, y upper right)
win.setBackground('black')



"""
DEFINE ROBOT MOVEMENT AND TARGET COLLECTION
"""


def robots(env):
    i = 1
    while i <= 3:
        # draw a target using circle
        tgt = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius=tgtradius)
        tgt.setFill('white')
        tgt.setOutline('blue')
        print'TARGET %d AT %d, %d' % (i, tgt.getCenter().getX(), tgt.getCenter().getY())
        tgt.draw(win)
        i += 1

    # draw a bot
    bot = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius=botradius)
    bot.setFill('blue')
    bot.setOutline('white')
    bot.draw(win)

    while True:
        bot.move(randMov(), randMov()) #assigns random movement to bot, better way to generate?
        #safeMovBotRandom()

        if colDet(bot, tgt) <= 1: #checks colission detection
            print('TARGET FOUND AT %d, %d' %updateCo(bot))
            tgt.undraw()  # remove target # we should add a globvar or something so we know its been picked up
            yield env.timeout(timestep)
        print('The bot is at %d, %d' %updateCo(bot))
        print('bot is %d away' %colDet(bot, tgt))

        yield env.timeout(timestep)



"""
RUN PROCESS
"""


env.process(robots(env)) #starting process
env.run(until=totalruntime)#run project for certain amount of time


#setting a mouse click on the window as proper exit
# does not respond until the env is finished running
win.getMouse()

"""Leftover pieces 
            
# initialize 5 targets and 1 bot?
def agentInit(colour):
    tgtDrawn = 0
    while tgtDrawn < 5:
        #draw a target using circle
        tgt = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius = tgtradius)
        tgt.setFill('white')
        tgt.setOutline(colour)
        tgt.draw(win)
        tgtDrawn += 1

    #draw a bot
    bot = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius = botradius)
    bot.setFill(colour)
    bot.setOutline('white')
    bot.draw(win)
    
    
#collision detection on exact point
if updateBot() == updateTgt():
            print('target found')

#get robot co-ordinates
def updateBot():
    rX = bot.getCenter().getX()
    rY = bot.getCenter().getY()
    return rX, rY

#get target co-ordinates
def updateTgt():
    tX = tgt.getCenter().getX()
    tY = tgt.getCenter().getY()
    return tX, tY


i = 1
while i <= 3:
    #draw a target using circle
    tgt = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius = tgtradius)
    tgt.setFill('white')
    tgt.setOutline('blue')
    print'TARGET %d AT %d, %d' %(i, tgt.getCenter().getX(), tgt.getCenter().getY())
    tgt.draw(win)
    i += 1

#draw a bot
bot = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius = botradius)
bot.setFill('blue')
bot.setOutline('white')
bot.draw(win)
botRadar = Circle(Point(bot.getCenter().getX(), bot.getCenter().getY()), radius = botradius + 10)
botRadar.setOutline('blue')
botRadar.draw(win)
"""

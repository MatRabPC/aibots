# TODO - make simulation terminate after an event as opposed to time
# TODO - implement Samina's changes
from graphics import *
from threading import Thread
import simpy
import random
import math

"""
DEFINE VARIABLES AND METHODS
"""

env = simpy.rt.RealtimeEnvironment(factor=0.1)  # movement time
winXLL = 0
winYLL = 0
winXUR = 30  # height of the window
winYUR = 30  # width of the window
totalruntime = 70  # amount of steps the system will run for
timestep = 1  # amount of steps the project will take
tgtradius = 0.5
botradius = 1


# return either -1, 0 or 1
def randMov():
    rn = random.randint(-1, 1)
    return rn


# return random coordinates in the window
def randSpawn(limit):
    rn = random.randint(0, limit)
    return rn


# return x and y position of circle objects
def updateCo(obj):
    oX = obj.getCenter().getX()
    oY = obj.getCenter().getY()
    return oX, oY


# detect collision
def colDet(obj1, obj2):
    dist = math.sqrt((obj1.getCenter().getX() - obj2.getCenter().getX()) ** 2 + (
    obj1.getCenter().getY() - obj2.getCenter().getY()) ** 2)
    return dist


"""
CREATE VISUALS
"""

# create window
win = GraphWin('MaSaAn Bots', width=1200, height=1200)  # Create window
win.setCoords(winXLL, winYLL, winXUR,
              winYUR)  # set window coords by (x lower left, y lower left, x upper right, y upper right)
win.setBackground('black')

# craw a target using circle
tgt = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius=tgtradius)
tgt.setFill('white')
tgt.setOutline('red')
tgt.draw(win)

# draw a bot
bot = Circle(Point(randSpawn(winXUR), randSpawn(winYUR)), radius=botradius)
bot.setFill('blue')
bot.setOutline('white')
bot.draw(win)

"""
DEFINE ROBOT MOVEMENT AND TARGET COLLECTION
"""


def robots(env):
    while True:
        bot.move(randMov(), randMov())  # assigns random movement to bot, better way to generate?
        # safeMovBotRandom()
        if colDet(bot, tgt) <= 1:  # checks colission detection
            print('TARGET FOUND AT %d, %d' % updateCo(bot))
            tgt.undraw()  # remove target # we should add a globvar or something so we know its been picked up
            yield env.timeout(timestep)
        print('The bot is at %d, %d' % updateCo(bot))
        print('bot is %d away' % colDet(bot, tgt))
        yield env.timeout(timestep)



"""
RUN PROCESS W/ THREADS
"""

#env.process(robots(env))  # starting process
#env.run(until=totalruntime)  # run project for certain amount of time

t = Thread(target=robots, args = (env, ))
t.start()

env.run(until=totalruntime)

# setting a mouse click on the window as proper exit
# does not respond until the env is finished running
win.getMouse()


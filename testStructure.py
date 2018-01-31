import progressbar
from graphics import *
import simpy
import random
import math

##define system variables and methods##
env = simpy.rt.RealtimeEnvironment(factor=1)  # movement time
winHeight = 10  # height of the window
winWidth = 10  # width of the window
totalruntime = 20 # amount of steps the system will run for
timestep = 1  # amount of steps the project will take

tgtradius = 0.5
botradius = 1
tgtX = 5
tgtY = 5
botX = 5
botY = 5

#test slowly going away from the target, assuming target and bot starting at same position
fact = 1 #radius away from the point the target is
test = [
    1 * fact ,0, # 1 right
    1, 0, # 2 right
    - fact - 1, 1 * fact, # 1 above
    0, 1,  # 2 above

    0, 2 * (-fact) - 1, #1 below
    0, -1, # 2 below
    -1 * fact, fact + 1, # 1 left
    -1, 0 # 2 left
]


"""
#test factors adjecent to the target, assuming target and bot starting at same position
fact = 2 #radius away from the point the target is
test = [
    1 * fact,0, # right
    -2 * fact, 0, # left
    1 * fact, 1 * fact, # up
    0, -2 * fact # down
]
"""

""" #for target at (3,3) and bot at (6,6)
#controlled move pattern
test = [
    -1, -1, #(5,5) euc dist of 2
    -1, 0, # (4,5) euc dist of 2
    0, -1,   #(4,4) euc dist of 1
    -1, 0,   #(3,4) euc dist of 1
    -1, 0,   #(2,4) euc dist of 1
    -1, -1,  #(1,3)
    1, 0,    #(2,3)
    1, 0    #(3,3) target location
]
"""

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


##CREATE VISUALS##
# create window
win = GraphWin('MaSaAn Bots', width=800, height=800)  # Create window
win.setCoords(0, 0, winHeight,
              winWidth)  # set window coords by (x lower left, y lower left, x upper right, y upper right)
win.setBackground('black')

# create a target using circle
tgt = Circle(Point(tgtX,tgtY), radius=tgtradius)
tgt.setFill('white')
tgt.setOutline('red')
tgt.draw(win)

# create a bot
bot = Circle(Point(botX,botY), radius=botradius)
bot.setFill('blue')
bot.setOutline('white')
bot.draw(win)


##DEFINE ROBOT MOVEMENT AND TARGET COLLECTION##
def robots(env, tc = 0):
    while True:
        print('The bot is at %d, %d' % updateCo(bot))
        print('bot is %d away' % colDet(bot, tgt))
        bot.move(test[tc], test[tc+1])  #run test case
        tc += 2
        if colDet(bot, tgt) <= tgtradius + botradius:  # checks colission detection
            print('TARGET FOUND AT %d, %d' % updateCo(bot))
            yield env.timeout(timestep)
        yield env.timeout(timestep)


##RUN PROCESS##
env.process(robots(env))  # starting process
env.run(until=len(test))



# setting a mouse click on the window as proper exit
# does not respond until the env is finished running
win.getMouse()

"""Leftover pieces 

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





"""
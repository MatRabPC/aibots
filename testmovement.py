from graphics import *
import simpy
import random
import math



##define system variables and methods##
env = simpy.rt.RealtimeEnvironment(factor=0.07) #movement time
winHeight = 30 #height of the window
winWidth = 30 # width of the window
totalruntime = 200 #amount of steps the system will run for
timestep = 1 #amount of steps the project will take
tgtradius = 0.5
botradius = 2


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



##CREATE VISUALS##
#create window
win = GraphWin('MaSaAn Bots', width = 800, height = 1000) #Create window
win.setCoords(0,0,winHeight,winWidth) #set window coords by (x lower left, y lower left, x upper right, y upper right)
win.setBackground('black')


#create a target using circle
tgt = Circle(Point(randSpawn(winHeight), randSpawn(winWidth)), radius = tgtradius)
tgt.setFill('white')
tgt.setOutline('red')
tgt.draw(win)


#create a bot
bot = Circle(Point(randSpawn(winHeight), randSpawn(winWidth)), radius = botradius)
bot.setFill('blue')
bot.setOutline('white')
bot.draw(win)




##DEFINE ROBOT MOVEMENT AND TARGET COLLECTION##
def robots(env):
    while True:
        bot.move(randMov(), randMov()) #assigns random movement to bot, better way to generate?
        if colDet(bot, tgt) <= 1: #checks colission detection
            print('TARGET FOUND AT %d, %d' %updateCo(bot))
            yield env.timeout(timestep)
        print('The bot is at %d, %d' %updateCo(bot))
        print('bot is %d away' %colDet(bot, tgt))
        yield env.timeout(timestep)




##RUN PROCESS##
env.process(robots(env)) #starting process
env.run(until=totalruntime)#run project for certain amount of time


#setting a mouse click on the window as proper exit
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
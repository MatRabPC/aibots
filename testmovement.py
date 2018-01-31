from graphics import *
import simpy
import random


##defining movement time##
env = simpy.rt.RealtimeEnvironment(factor=0.1)

##Create visuals##
#create window
win = GraphWin('MaSaAn Bots', width = 800, height = 1000) #Create window
win.setCoords(0,0,30,30) #set window coords by (x lower left, y lower left, x upper right, y upper right)
win.setBackground('black')


#create and place square border
border = Rectangle( Point(1,1), Point(29,29))
border.setOutline("white")
border.draw(win)


#create a target using circle
tgt = Circle(Point(3, 5), radius = 1)
tgt.setFill('white')
tgt.setOutline('red')
tgt.draw(win)


#create a bot
bot = Circle(Point(5,5), radius = 1)
bot.setFill('blue')
bot.setOutline('white')
bot.draw(win)


##define movement + basic collision detection##
def robots(env):
    while True:
        print('Step back at %d' % env.now)
        timestep = 2
        bot.move(randMov(), randMov())
        if updateBot() == updateTgt():
            print('target found')
        print('The bot is at %d, %d' %updateBot())
        yield env.timeout(timestep)


# return either -1, 0 or 1
def randMov():
    rn = random.randint(-1, 1)
    return rn


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

#detect collision
#def colDet():


#starting process and running for a certain amount of time
env.process(robots(env))
env.run(until=50)


#setting a mouse click on the window as proper exit
# does not respond until the env is finished running
win.getMouse()
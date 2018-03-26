import simpy
from environmentbuilder import *

'''
from tester import *


def inRadar(win, bot, loclist):

    points = getAllPointsInRadius(bot, win)

    for i in range(points):
        if points[i] in loclist:
            return True

    return False
'''

################################################################################################ VARS

xlower, xupper, ylower, yupper = 0, 30, 0, 30
#xlower, xupper, ylower, yupper = 0, 100, 0, 100 #larger field
totalruntime = 500 #amount of steps the system will run for
timestep = 2 #amount of steps the project will take
nobot = 1
notgt = 1
colours = ['blue', 'red', 'green', 'yellow', 'orange']
botlot = []
tgtlot = []

################################################################################################ BUILDING

win = envwindowbuilder(xlower, xupper, ylower, yupper, xupper/10)

for i in range(nobot):
    for j in range(notgt):
        tgtlot.append(buildtgtr(win, colours[i], 10, 10))#random.randint(3, 10), random.randint(3, 10)))

for i in range(nobot):
    botlot.append(make_bot(win, colours[i], 8,8, notgt))#random.randint(3, 10), random.randint(3, 10), notgt))

#loclist = getLocList(botlot, tgtlot)

tgtloclist = getTgtList(tgtlot)

print tgtloclist
win.getMouse() #waits on mouse click to begin

################################################################################################ JACK IN, MEGAMAN, EXECUTE

#print boundaryCheck(botlot[0], (-10,-10))

env = simpy.rt.RealtimeEnvironment(factor=0.5, strict=False) #movement time, **strict=false removes the realtime runtime error
env.process(robots(env, timestep, botlot, tgtlot, xupper, tgtloclist))
env.run(until=totalruntime)

print('end of event')
win.getMouse()
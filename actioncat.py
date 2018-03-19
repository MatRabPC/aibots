import simpy
from environmentbuilder import *
from tester import *


def inRadar(win, bot, loclist):

    points = getAllPointsInRadius(bot, win)

    for i in range(points):
        if points[i] in loclist:
            return True

    return False


################################################################################################ VARS

xlower, xupper, ylower, yupper = 0, 30, 0, 30
#xlower, xupper, ylower, yupper = 0, 100, 0, 100 #larger field
totalruntime = 500 #amount of steps the system will run for
timestep = 1 #amount of steps the project will take
nobot = 2
notgt = 2
colours = ['blue', 'red', 'green', 'yellow', 'orange']

################################################################################################ BUILDING

win = envwindowbuilder(xlower, xupper, ylower, yupper, xupper/10)
#botlot, tgtlot = aifactory(win, colours, nobot, notgt)
tgtlot = [buildtgtr(win, 'green', 23, 25)]
botlot = [make_bot(win, 'green', 23, 23, 1)]

getAllPointsInRadius(botlot[0], win)




#botlot, tgtlot = initbot(win, colours, nobot, notgt)
loclist = getLocList(botlot, tgtlot)
tgtloclist = getTgtList(tgtlot)

#bot = make_bot(win, 'green', 23, 23)

win.getMouse() #waits on mouse click to begin

################################################################################################ JACK IN, MEGAMAN, EXECUTE

#print(Point(5,10), botlot[1])

#k = make_bot(win, 'red', 10, 10, 2)

#if inCircle(Point(10, 11), k):
    #print 'fault'

env = simpy.rt.RealtimeEnvironment(factor=0.07, strict=False) #movement time, **strict=false removes the realtime runtime error
env.process(robots(env, timestep, botlot, tgtlot, xupper, tgtloclist))
env.run(until=totalruntime)

print('end of event')
win.getMouse()
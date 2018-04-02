import simpy
from environmentbuilder import *

################################################################################################ VARS

xlower, xupper, ylower, yupper = 0, 30, 0, 30
xlower, xupper, ylower, yupper = 0, 100, 0, 100 #larger field
totalruntime = 50000 #amount of steps the system will run for
timestep = 1 #amount of steps the project will take
nobot = 5
notgt = 5
colours = ['blue', 'red', 'green', 'yellow', 'orange']
botlot = []
tgtlot = []

################################################################################################ BUILDING

win = envwindowbuilder(xlower, xupper, ylower, yupper, xupper/10)

for i in range(nobot):
    for j in range(notgt):
        tgtlot.append(buildtgtr(win, colours[i], random.randint(3, 25), random.randint(3, 25)))#random.randint(3, 10), random.randint(3, 10)))

for i in range(nobot):
    botlot.append(make_bot(win, colours[i], random.randint(3, 55), random.randint(3, 55), notgt))#random.randint(3, 10), random.randint(3, 10), notgt))

#loclist = getLocList(botlot, tgtlot)

tgtloclist = getTgtList(tgtlot)

print tgtloclist
win.getMouse() #waits on mouse click to begin

################################################################################################ JACK IN, MEGAMAN, EXECUTE

env = simpy.rt.RealtimeEnvironment(factor=0.001, strict=False) #movement time, **strict=false removes the realtime runtime error
env.process(robots(env, timestep, botlot, tgtlot, win, tgtloclist))
env.run(until=totalruntime)

print('end of event')
winCondition(win)

win.getMouse()
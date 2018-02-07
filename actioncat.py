import simpy
from environmentbuilder import *
from botntgtbuilder import *

'''
this is the runner script
that takes all the functions from the other files
and runs them, building all the stuff
and then running the actual simulation

Current list of file dependencies listed under import sympy
'''

################################################################################################VARS

xlower, xupper, ylower, yupper = 0, 30, 0, 30
#xlower, xupper, ylower, yupper = 0, 100, 0, 100 #larger field
totalruntime = 500 #amount of steps the system will run for
timestep = 1 #amount of steps the project will take
tgtradius = 0.5
botradius = 2
nobot = 2
colours = ['blue', 'red', 'green', 'yellow', 'orange']

################################################################################################BUILDING

win = envwindowbuilder(xlower, xupper, ylower, yupper, xupper/10)


botlot = [None] * nobot
tgtlot = [None] * nobot
#'''
tgtloc = [(0, 0)] * nobot

for i in range(nobot):
    for j in range(nobot):
        tgtlot[j] = buildtgt(win, colours[i])

for i in range(nobot):
    botlot[i] = buildbot(win, colours[i])
    #bots made after, so they appear on top of targets
#'''
#botlot, tgtlot = btfactory(win, colours, 2, 2)
win.getMouse() #waits on mouse click to begin

################################################################################################JACK IN, MEGAMAN, EXECUTE

env = simpy.rt.RealtimeEnvironment(factor=0.07, strict=False) #movement time, **strict=false removes the realtime runtime error
env.process(robots(env, timestep, botlot, tgtlot, xupper))
env.run(until=totalruntime)

print('end of event')
win.getMouse()
import simpy
from environmentbuilder import *
from botbuilder import *
from tgtbuilder import *


'''
this is the runner script
that takes all the functions from the other files
and runs them, building all the stuff
and then running the actual simulation

Current list of file dependencies listed under import sympy
'''

##############################################################################################

def robots(env):
    while True:
        #bot.move(randMov(), randMov()) #assigns random movement to bot, better way to generate?
        safeMovBotRandom(bot, xupper) #still just random movement, but safe check too
        if colDet(bot, tgt) <= 1: #checks colission detection
            print('TARGET FOUND AT %d, %d' %updateCo(bot))
            yield env.timeout(timestep)

        if updateBot(bot) == updateTgt(tgt):
            print('target found')
            tgt.undraw()  # remove target # we should add a globvar or something so we know its been picked up
            yield env.timeout(timestep)

        print('The bot is at %d, %d' %updateCo(bot))
        print('bot is %d away' %colDet(bot, tgt))
        yield env.timeout(timestep)

################################################################################################

xlower, xupper, ylower, yupper = 0, 30, 0, 30
#xlower, xupper, ylower, yupper = 0, 100, 0, 100 #larger field
totalruntime = 50 #amount of steps the system will run for
timestep = 1 #amount of steps the project will take
tgtradius = 0.5
botradius = 2

################################################################################################

win = envwindowbuilder(xlower, xupper, ylower, yupper, xupper/10) #smaller size
tgt = buildtgt(win)
bot = buildbot(win, 'blue')
win.getMouse() #waits on mouse click to begin

################################################################################################

env = simpy.rt.RealtimeEnvironment(factor=0.1, strict=False) #movement time, **strict=false removes the realtime runtime error
env.process(robots(env))
env.run(until=totalruntime)#run project for certain amount of time
print('end of event')
win.getMouse() #end, wait until mouse click to close

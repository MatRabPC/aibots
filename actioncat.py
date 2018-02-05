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
##define movement + basic collision detection##
def robots(env):
    while True:
        print('Step back at %d' % env.now)
        timestep = 2

        safeMovBotRandom(bot, xupper)

        if updateBot(bot) == updateTgt(tgt):
            print('target found')
            tgt.undraw() #remove target # we should add a globvar or something so we know its been picked up
        print('The bot is at %d, %d' %updateBot(bot))
        yield env.timeout(timestep)

################################################################################################
xlower, xupper, ylower, yupper = 0, 30, 0, 30
#xlower, xupper, ylower, yupper = 0, 100, 0, 100 #larger field


win = envwindowbuilder(xlower, xupper, ylower, yupper, xupper/10) #smaller size
tgt = buildtgt(win)
bot = buildbot(win, 'blue')

win.getMouse() #waits on mouse click to begin

env = simpy.rt.RealtimeEnvironment(factor=0.1)
env.process(robots(env))
env.run(until=50)

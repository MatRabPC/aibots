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

##############################################################################################

def robots(env):
    while True:
        #bot.move(randMov(), randMov()) #assigns random movement to bot, better way to generate?

        for i in range(len(botlot)):

            safeMovBotRandom(botlot[i], xupper) #still just random movement, but safe check too

            for j in range(len(tgtlot)):
                if colDet(botlot[i], tgtlot[j]): #checks colission detection
                    print('TARGET FOUND AT %d, %d' %updateCo(botlot[i]))
                    yield env.timeout(timestep)


                if updateBot(botlot[i]) == updateTgt(tgtlot[j]) and botlot[i].config["fill"] == tgtlot[i].config["outline"]:
                    print('target found')
                    tgtlot[j].undraw()  # remove target # we should add a globvar or something so we know its been picked up
                    yield env.timeout(timestep)

                print('The bot is at %d, %d' %updateCo(botlot[i]))
                print('bot is %d away' %colDet(botlot[i], tgtlot[j]))
            yield env.timeout(timestep)

################################################################################################

xlower, xupper, ylower, yupper = 0, 30, 0, 30
#xlower, xupper, ylower, yupper = 0, 100, 0, 100 #larger field
totalruntime = 500 #amount of steps the system will run for
timestep = 1 #amount of steps the project will take
tgtradius = 0.5
botradius = 2
nobot = 5

################################################################################################

win = envwindowbuilder(xlower, xupper, ylower, yupper, xupper/10) #smaller size
#tgt = buildtgt(win)

botlot = [None] * nobot
tgtlot = [None] * nobot

for i in range(nobot):
    tgtlot[i] = buildtgt(win, 'blue')

botlot[0] = buildbot(win, 'blue')
botlot[1] = buildbot(win, 'red')
botlot[2] = buildbot(win, 'green')
botlot[3] = buildbot(win, 'black')
botlot[4] = buildbot(win, 'grey')

#print botlot[0].config["fill"]

#bot = buildbot(win, 'blue')
#sbot = buildbot(win, 'green')
win.getMouse() #waits on mouse click to begin

################################################################################################

env = simpy.rt.RealtimeEnvironment(factor=0.07, strict=False) #movement time, **strict=false removes the realtime runtime error
env.process(robots(env))
env.run(until=totalruntime)#run project for certain amount of time
print('end of event')
win.getMouse() #end, wait until mouse click to close

from graphics import *
import random

blst = []


#builds bot
class Bots(object):
    visited = []
    tgts = 0
    tgtLoc = None
    bot = None
    config = []
    radarRadius = 5
    commCo = []
    dirX = 1
    dirY = 0
    vert = 1
    stepsTaken = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, win, clr, x, y, notgts):
        self.bot = Circle(Point(x, y), radius=1)
        self.bot.setFill(clr)
        self.bot.setOutline('white')
        self.bot.draw(win)
        self.visited.append([x,y])
        self.tgts = notgts
        self.config = self.bot.config
        self.radar = Circle(Point(x, y), radius=self.radarRadius)
        self.radar.setOutline('cyan')
        self.radar.draw(win)
        self.crash = False
        self.horizon = 1
        self.holdval = 1

    def getCenter(self):
        return self.bot.getCenter()

    def getRadius(self):
        return self.bot.getRadius()

    def move(self, x, y):
        self.stepsTaken = self.stepsTaken + 1
        self.radar.move(x, y)
        blst.pop()
        blst.append((self.bot.getCenter().getX(), self.bot.getCenter().getY()))
     #   print blst
        return self.bot.move(x, y)

    def undraw(self):
        self.bot.undraw()

    def getDir(self):
        return self.dirX, self.dirY

    def removeFromBlst(self):
        blst.remove(blst.index(self.bot.getCenter().getX(), self.bot.getCenter().getY()))

def make_bot(win, clr, x, y, notgts):
    bot = Bots(win, clr, x, y, notgts)
    blst.append((bot.getCenter().getX(), bot.getCenter().getY()))
    return bot


''''''
#build target
def buildtgtr(win, clr, x, y):

    tgt = Circle(Point(x, y), radius = 1)
    tgt.setFill('#000')
    tgt.setOutline(clr)
    tgt.draw(win)



    return tgt

'''
functions
'''
#checks if the target we found belongs to the bot--if true, picks up and removes target, lowers Bot tgt counter--
# if false, returns false (so that, if there is a communication channel, we can tell the other bots what we found)
def checkTargetFound(bot, tgtlot, tgtloclist):

    if (getLoc(bot) in tgtloclist) and (
        tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] == bot.config["fill"]):

        #print('target found')
        tgtlot[tgtloclist.index(getLoc(bot))].undraw()
        tgtlot.pop(tgtloclist.index(getLoc(bot)))
        tgtloclist.pop(tgtloclist.index(getLoc(bot)))
        botRemoveTarget(bot)
        return True

    return False #return tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] #returns target outline colour


def botRemoveTarget(bot):
    bot.tgts = bot.tgts - 1  # reducing our bot's target count
    bot.tgtLoc = None
    bot.commCo = []



def checkTargetWho(point, lst, tgts, bot, botlot, sc):

        co = tgts[lst.index(point)].config["outline"]
    #    co = tgt[lst.index(getLoc(point))].config["outline"] == bot.config["fill"]):
        #print bot.config["fill"], "Found a", co , "target"
        if co == bot.config["fill"] and bot.tgtLoc is None:
            bot.tgtLoc = point
            createPath(bot, point)
           # return True

        else:
            if sc == 2 or sc == 3:
                findWhoElseTarget(point, lst, tgts, bot, botlot)


def findWhoElseTarget(point, lst, tgts, bot, botlot):
    colours = ['blue', 'red', 'green', 'yellow', 'orange']
    no = colours.index(tgts[lst.index(point)].config["outline"]) #bot no
    #publicChannel.append((colours[no], point))
    colours[no], point
    createPath(botlot[no], point)
    #createPath(botlot[no], point)
    #print bot.config["fill"], "to", colours[colours.index(tgts[lst.index(point)].config["outline"])], "your target is @", botlot[no].tgtLoc
    #print colours[colours.index(tgts[lst.index(point)].config["outline"])], "bot speaking, thanks for that, I'm heading via", botlot[no].commCo


def safeMove(bot):
    '''
    if bot.crash == True:
        bot.horizon *= -1
        bot.vert *= -1
        bot.dirX = bot.horizon
        bot.dirY = bot.vert
        bot.crash = False
        return bot.dirX, bot.dirY
        '''
    # Priority 1 - Locking bounds
    if bot.getCenter().getX() > 99:
        bot.dirX = -1
        if bot.getCenter().getY() > 99:
            bot.dirY = -1
        if bot.getCenter().getY() < 1:
            bot.dirY = 1
            return bot.dirX, bot.dirY
        return bot.dirX, bot.dirY
    elif bot.getCenter().getX() < 1:
        if bot.getCenter().getY() > 99:
            bot.dirY = -1
        if bot.getCenter().getY() < 1:
            bot.dirY = 1
        bot.dirX = 1
        return bot.dirX, bot.dirY
    elif bot.getCenter().getY() > 99:
        bot.dirY = -1
        if bot.getCenter().getX() > 99:
            bot.dirX = -1
        if bot.getCenter().getX() < 1:
            bot.dirX = 1
        return bot.dirX, bot.dirY
    elif bot.getCenter().getY() < 1:
        bot.dirY = 1
        if bot.getCenter().getX() > 99:
            bot.dirX = -1
        if bot.getCenter().getX() < 1:
            bot.dirX = 1
        return bot.dirX, bot.dirY

    if bot.crash:
        bot.vert = random.choice([-1, 1])
        bot.horizon = random.choice([-1, 1])
        bot.dirX = bot.horizon
        bot.dirY = bot.vert
        bot.crash = False

        #print "Crash avoided"
        return bot.dirX, bot.dirY

    #Priority 2 - Follow path to target
    if len(bot.commCo) > 1:
        #print "By commCO path"
        return moveByPath(bot)

    # Priotiy 3 - Automated 'snake' movement
    if bot.getCenter().getY() == 99 or bot.getCenter().getY() == 1 :
        #invert vertical direction when at the top or bottom of graph
        bot.vert *= -1

    if bot.getCenter().getY() < 95 or bot.getCenter().getY() > 5:
        bot.dirX = bot.horizon
        bot.dirY = 0

    if bot.getCenter().getX() >= 99 or bot.getCenter().getX() <= 1:
        bot.dirX = 0
        bot.dirY = bot.vert
        if bot.getCenter().getY() % 10 == 5 and bot.holdval == 1:
            bot.holdval = -1
            bot.horizon *= -1
            bot.dirX = bot.horizon
            bot.dirY = 0
        elif bot.getCenter().getY() % 10 == 5 and bot.holdval == -1:
            bot.holdval = 1

    return bot.dirX, bot.dirY



'''
build and follow path
'''
def getAllPointsInRadius(bot, lst):

    cx = int(bot.getCenter().getX())
    cy = int(bot.getCenter().getY())
    r = bot.radar.getRadius()# + 2

    for i in range(cx-r, cx+r):
        for j in range(cy-r, cy+r):

            if ((i - cx) * (i - cx) + (j - cy) * (j - cy) <= r * r):
                if (i,j) in lst:
                  #  print "Found you @ ", (i, j)
                    if bot.tgtLoc is None:
                        return (i, j)

                elif (i, j) in blst and (abs(cx - i) > 5) and (abs(cy - j) > 5) and (not ((i, j) == (cx, cy))):
                    bot.crash = True
                   # print bot.getCenter(), "finds", (i, j)
                #    time.sleep(3)



    return False


def createPath(bot, point):

    curr = (bot.getCenter().getX(), bot.getCenter().getY())
    xsteps = []
    ysteps = []
    path = []
    x = int(point[0] - curr[0])
    y = int(point[1] - curr[1])

    if x > 0:
        for i in range(abs(x)):
            xsteps.append(1)

    if x < 0:
        for i in range(abs(x)):
            xsteps.append(-1)

    if y > 0:
        for i in range(abs(y)):
            ysteps.append(1)

    if y < 0:
        for i in range(abs(y)):
            ysteps.append(-1)

    if not x == 0:
        for i in range(abs(x)):
            path.append((xsteps[i], 0))

   # print path

    if not y == 0:
        for i in range(abs(y)):
            path.append((0, ysteps[i]))

        if y > 0:
            path.append((0, 1))

        if y < 0:
            path.append((0, -1))

    if y == 0:
        if x > 0:
            path.append((1, 0))

        if x < 0:
            path.append((-1, 0))

    bot.commCo = path
    bot.tgtLoc = point

  #  print path
    return path


def moveByPath(bot):
    if not bot.commCo:
        bot.tgtLoc = None
        return 0, 0

    nextx = bot.commCo[0][0] - bot.getCenter().getX()
    nexty = bot.commCo[0][1] - bot.getCenter().getY()
    coo = bot.commCo.pop(0)
   # print "Popped", coo

    return coo[0], coo[1]



'''
build lists
'''


def getLocList(botlot):

    list = []
    for i in range(len(botlot)):
        list.append(getLoc(botlot[i]))


    return list


def getTgtList(tgtlot):

    list = []
    for i in range(len(tgtlot)):
        list.append(getLoc(tgtlot[i]))
    return list


def getLoc(obj):
    tX = obj.getCenter().getX()
    tY = obj.getCenter().getY()
    return (tX, tY)
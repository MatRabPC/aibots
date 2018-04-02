from graphics import *
import random

tgtradius = 1
botradius = 1

publicChannel = []

'''
If multiple targets belonging to one bot appear in its radar, it gets super confused and spazzes out
'''

'''
Building Stuff
'''

#builds bot
class Bots(object):
    visited = []
    tgts = 0
    tgtLoc = None
    bot = None
    config = []
    radarRadius = 7
    commCo = []
    dirX = 1
    dirY = 0
    vert = 1

    # The class "constructor" - It's actually an initializer
    def __init__(self, win, clr, x, y, notgts):
        self.bot = Circle(Point(x, y), radius=botradius)
        self.bot.setFill(clr)
        self.bot.setOutline('white')
        self.bot.draw(win)
        self.visited.append([x,y])
        self.tgts = notgts
        self.config = self.bot.config
        self.radar = Circle(Point(x, y), radius=self.radarRadius)
        self.radar.setOutline('cyan')
        self.radar.draw(win)

    def getCenter(self):
        return self.bot.getCenter()

    def getRadius(self):
        return self.bot.getRadius()

    def move(self, x, y):
        self.radar.move(x, y)
        return self.bot.move(x, y)

    def undraw(self):
        self.bot.undraw()

    def getDir(self):
        return self.dirX, self.dirY

def make_bot(win, clr, x, y, notgts):
    bot = Bots(win, clr, x, y, notgts)
    return bot


''''''
#build target
def buildtgtr(win, clr, x, y):

    tgt = Circle(Point(x, y), radius = tgtradius)
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

    colours = ['blue', 'red', 'green', 'yellow', 'orange']

    if (getLoc(bot) in tgtloclist) and (
        tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] == bot.config["fill"]):

        print('target found')
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


def checkVisited(bot, x, y): #curently not being used

   # print bot.visited
    print (x,y)

    if (x, y) in bot.visited: #check if in bot visited list
        return True

    return False



def checkTargetWho(point, lst, tgts, bot, botlot):

        co = tgts[lst.index(point)].config["outline"]
    #    co = tgt[lst.index(getLoc(point))].config["outline"] == bot.config["fill"]):
        print bot.config["fill"], "Found a", co , "target"
        if co == bot.config["fill"]:
            bot.tgtLoc = point
            print createPath(bot, point)
           # return True

        else:
            findWhoElseTarget(point, lst, tgts, bot, botlot)
      #  no = tgts[lst.index(point)].config["outline"]


     #   return True
    #return False #return tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] #returns target outline colour


def findWhoElseTarget(point, lst, tgts, bot, botlot):
    colours = ['blue', 'red', 'green', 'yellow', 'orange']
    no = colours.index(tgts[lst.index(point)].config["outline"]) #bot no
    #publicChannel.append((colours[no], point))
    print colours[no], point
    print createPath(botlot[no], point)
    #createPath(botlot[no], point)
    #print bot.config["fill"], "to", colours[colours.index(tgts[lst.index(point)].config["outline"])], "your target is @", botlot[no].tgtLoc
    #print colours[colours.index(tgts[lst.index(point)].config["outline"])], "bot speaking, thanks for that, I'm heading via", botlot[no].commCo


def safeMove(bot):
    if len(bot.commCo) > 1:
        print "By commCO path"
        return moveByPath(bot)

    x,y = random.randint(-1,1), random.randint(-1,1)
    #while (radarCheckBounds(bot)):
        #boundaryCheck(bot, (x,y))):# or (not radarCheck(bot)):
     #   x, y = random.randint(-1, 1), random.randint(-1, 1)

    #print (x+bot.getCenter().getX(),y+bot.getCenter().getY())
    return x, y


'''
build and follow path
'''
def getAllPointsInRadius(bot, lst):

    cx = int(bot.getCenter().getX())
    cy = int(bot.getCenter().getY())
    r = bot.radar.getRadius()# + 2
    points = []
   # print cx, cy

    for i in range(cx-r, cx+r):
        for j in range(cy-r, cy+r):
            x = i-bot.getRadius()
            y = j - bot.getRadius()

            #if (i-r > 0 and j - r > 0):
            if ((i - cx) * (i - cx) + (j - cy) * (j - cy) <= r * r):
                #if radarCheckBounds(bot, (i,j)):
                 #   print "Boundary detected"
                #points.append(Point(i,j)) #if within, append as Point
                if (i,j) in lst:
                    print "Found you @ ", (i, j)
                    if bot.tgtLoc is None:
                        return (i, j)

    return False


def radarCheckBounds(bot, point):

    if (-1 == point[0]) or (-1 == point[1]) or (32 == point[0]) or (32 == point[1]): #we check if the bounds is in radius by checking the sides
        #print "Boundary detected"
        return True

    return False
   # print bot.getCenter(), xf, xb, yf, yb


def createPath(bot, point):
   # if not bot.commCo:
    #    print "Busy going to", bot.tgtLoc
     #   return False

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

    print path
    return path


def moveByPath(bot):
    if not bot.commCo:
        bot.tgtLoc = None
        return 0, 0

    nextx = bot.commCo[0][0] - bot.getCenter().getX()
    nexty = bot.commCo[0][1] - bot.getCenter().getY()
    coo = bot.commCo.pop(0)
    print "Popped", coo

    return coo[0], coo[1]
    #return nextx, nexty



'''
build lists
'''


def getLocList(botlot, tgtlot):

    list = []
    for i in range(len(botlot)):
        list.append(getLoc(botlot[i]))

    for i in range(len(tgtlot)):
        list.append(getLoc(tgtlot[i]))

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

'''
def safeMove(bot):

    if len(bot.commCo) > 1:
        #if a target path exists, take target path first
        print "By commCO path"
        return moveByPath(bot)

    #automated snake movement
    if bot.getCenter().getY() > 95 or bot.getCenter().getY() < 5:
        #invert vertical direction when at the top or bottom of graph
        Bots.vert *= -1

    if bot.getCenter().getX() < 5:
        Bots.dirX = 0
        Bots.dirY = Bots.vert
        if bot.getCenter().getY() % 15  == 10:
            Bots.dirX = 1
            Bots.dirY = 0

    elif bot.getCenter().getX() >= 95:
        Bots.dirX = 0
        Bots.dirY = Bots.vert
        if bot.getCenter().getY() % 15 == 0 :
            Bots.dirX = -1
            Bots.dirY = 0

    return Bots.dirX, Bots.dirY

'''
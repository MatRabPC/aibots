from graphics import *
import random
import math

tgtradius = 1
botradius = 1

'''
Building Stuff
'''

#builds bot
class Bots(object):
    visited = []
    tgts = 0
    bot = None
    config = []
    radarRadius = 3
    commCo = []

    # The class "constructor" - It's actually an initializer
    def __init__(self, win, clr, x, y, notgts):
        self.bot = Circle(Point(x, y), radius=botradius)
        self.bot.setFill(clr)
        self.bot.setOutline('white')
        self.bot.draw(win)
        self.visited.append([x,y])
        self.tgts = notgts
        self.config = self.bot.config
        self.radar = Circle(Point(x, y), radius= self.radarRadius)
        self.radar.setOutline('cyan')
        self.radar.draw(win)

    def getCenter(self):
        return self.bot.getCenter()

    def getRadius(self):
        return self.bot.getRadius()

    def move(self, x, y):
        return self.bot.move(x, y)

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

    if (getLoc(bot) in tgtloclist) and (
        tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] == bot.config["fill"]):

        print('target found')
        tgtlot[tgtloclist.index(getLoc(bot))].undraw()
        tgtlot.pop(tgtloclist.index(getLoc(bot)))
        tgtloclist.pop(tgtloclist.index(getLoc(bot)))
        bot.tgts = bot.tgts - 1

        return True
    return False #return tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] #returns target outline colour


def checkVisited(bot, x, y):

   # print bot.visited
    print (x,y)

    if (x, y) in bot.visited:
        return True

    return False




def getAllPointsInRadius(bot, lst):

    cx = int(bot.getCenter().getX())
    cy = int(bot.getCenter().getY())
    r = bot.radar.getRadius()# + 2
    points = []
    print cx, cy

    for i in range(cx-r, cx+r):
        for j in range(cy-r, cy+r):
            x = i-bot.getRadius()
            y = j - bot.getRadius()

            #if (i-r > 0 and j - r > 0):
            if ((i - cx) * (i - cx) + (j - cy) * (j - cy) <= r * r):
                #points.append(Point(i,j)) #if within, append as Point
                if (i,j) in lst:
                    print "Found you @ ", (i, j)
                    return (i, j)
    return False


def checkTargetWho(point, lst, tgts, bot):

        co = tgts[lst.index(point)].config["outline"]
    #    co = tgt[lst.index(getLoc(point))].config["outline"] == bot.config["fill"]):

        if co == bot.config["fill"]:
            bot.commCo = point
            '''
            print('target found')
            tgts[lst.index(point)].undraw()
            tgts.pop(lst.index(point))
            lst.pop(lst.index(point))
            bot.tgts = bot.tgts - 1
'''
       # else:


     #   return True
    #return False #return tgtlot[tgtloclist.index(getLoc(bot))].config["outline"] #returns target outline colour




def radarCheck(bot, tgtlst):
    #return True

    frontx = bot.radar.getCenter().getX() + bot.radar.getRadius()
    backx = bot.radar.getCenter().getX() - bot.radar.getRadius()
    fronty = bot.radar.getCenter().getY() + bot.radar.getRadius()
    backy = bot.radar.getCenter().getY() - bot.radar.getRadius()

   # print radar2(bot, 3)

    po = [(frontx, fronty), (frontx, backy), (backx, fronty), (backx, backy)]
    print po

    for i in range(4):
        #Point(po[i][0], po[i][1]).draw
        if po[i] in tgtlst:
            print "Found you at", po[i]
            return True

    return False
   # print bot.getCenter(), xf, xb, yf, yb




def boundaryCheck(bot, step):
    x = bot.getCenter().getX()
    y = bot.getCenter().getY()

#    radarCheck(bot)
    if (x+step[0] < 2 or x+step[0] > 15) and (y+step[1] < 2 or y+step[1] > 15):
        return False
    return True


def safeMove(bot):
    if len(bot.commCo) > 1:
        print "By commCO path"
        return moveByPath(bot)

    x,y = random.randint(-1,1), random.randint(-1,1)
    while (not boundaryCheck(bot, (x,y))):# or (not radarCheck(bot)):
        x, y = random.randint(-1, 1), random.randint(-1, 1)

    #print (x+bot.getCenter().getX(),y+bot.getCenter().getY())
    return x, y


def createPath(bot, point):
    curr = (bot.getCenter().getX(), bot.getCenter().getY())
    xsteps = []
    ysteps = []
    path = []


    if point[0] - curr[0] > 0:
        for i in range(int(point[0] - curr[0])):
            xsteps.append(1)

    if point[1] - curr[1] > 0:
        for i in range(int(point[1] - curr[1])):
            ysteps.append(1)

    if len(xsteps) > len(ysteps):
        for i in range(len(xsteps)):
            if i < len(ysteps): #in range
                path.append((xsteps[i], ysteps[i]))
            else:
                path.append((xsteps[i], 0))

    if len(xsteps) < len(ysteps):
        for i in range(len(ysteps)):
            if i < len(ysteps): #in range
                path.append((xsteps[i], ysteps[i]))
            else:
                path.append((0, ysteps[i]))

    q=len(path)-1
    path.append((path[q][0] - point[0], path[q][1] - point[1]))
    bot.commCo = path
    bot.tgtLoc = point

    return path


def moveByPath(bot):
    nextx = bot.commCo[0][0] - bot.getCenter().getX()
    nexty = bot.commCo[0][1] - bot.getCenter().getY()
    coo = bot.commCo.pop(0)
    print "Popped", coo

    return coo[0], coo[1]
    #return nextx, nexty



'''
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

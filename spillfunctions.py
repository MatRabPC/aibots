


'''
This is a side script that's just full of the silly functions
that Samina makes that are probably only used once but
just save that much confusion

Pay this little mind, as you would Samina herself.

Very little indeed.
'''



def loopinters(obj, lst):

    for i in range(len(lst)):
        if pointinter(obj, lst[i], 1):
        #if objinter(obj.getCenter(), lst[i], 2):
            return True
    return False

def pointinter(obj1, obj2, r):

    distance = ((obj1[0] - obj2[0]) ** 2 + (obj1[1] - obj2[1]) ** 2) ** 0.5
    return distance < r + r


def checkMovLegal(x, y, sizeof):
    #the +2 is to accomodate for the radius of the bot
    if x < 0+2 or x > sizeof-2 or y < 0+2 or y > sizeof-2:
        return False
    else:
        return True


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

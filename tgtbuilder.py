from graphics import *

'''
all target stuff
'''

def buildtgt(win):

    tgt = Circle(Point(3, 5), radius = 1)
    tgt.setFill('white')
    tgt.setOutline('red')
    tgt.draw(win)

    return tgt

#get target co-ordinates
def updateTgt(tgt):
    tX = tgt.getCenter().getX()
    tY = tgt.getCenter().getY()
    return tX, tY
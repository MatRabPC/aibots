from botntgtbuilder import *
from deliverables import *

def envwindowbuilder(xlower, xupper, ylower, yupper, winborder):

    ##Create visuals##
    #create window
    win = GraphWin('MaSaAn Bots', width = 1000, height = 1000) #Create window #I had to make a square, the tilt was bothering me, sorry
    win.setCoords(xlower-winborder, ylower-winborder, xupper+winborder, yupper+winborder) #set window coords by (x lower left, y lower left, x upper right, y upper right)
    win.setBackground('black')
    #win.setCoords(100, 100, 200, 200)#win.winfo_width()/2, win.winfo_height()/2)

    #create and place square border
    border = Rectangle(Point(xlower+1, ylower+1), Point(xupper-1, yupper-1))
    border.setOutline("white")
    border.draw(win)

    zerolabel = Text(Point(0, 0), "0")
    zerolabel.setFill("white")
    zerolabel.draw(win)

    for i in range(xlower+1, xupper+1):
        if not i%10: #skip 0 and non-tenth numbers
            xaxis = Text(Point(-2,i), str(i))
            yaxis = Text(Point(i, -2), str(i))
            xaxis.setFill("white")
            xaxis.draw(win)
            yaxis.setFill("white")
            yaxis.draw(win)

    for i in range(xlower+1, xupper):
        if not i%10:
            graphlines = Line(Point(i,0),Point(i,xupper-1))
            graphlines.setFill("white")
            graphlines.draw(win)

    for j in range(ylower+1, yupper):
        if not j%10:
            graphlines = Line(Point(0,j),Point(xupper-1,j))
            graphlines.setFill("white")
            graphlines.draw(win)

    #'''
    #test dotted line
    for i in range(xlower+1, xupper-1):
        for j in range(ylower + 1, yupper - 1):
            if i%10 and j%10:
                graphdot = Point(i, j)
                graphdot.setFill("white")
                graphdot.draw(win)
    #'''

    win.getMouse() #click to end set up pause
    return win

winOrder = []

def winCondition(win, botlot, iterationNum, scenario):
    winList = Text(Point(50, 105), winOrder)
    winList.setFill("white")
    winList.setSize(25)
    winList.draw(win)

    fullMakeandWritetoCSV(botlot, scenario, iterationNum)

    win.getMouse()






#####################################################################

def robots(env, timestep, botlot, tgtlot, win, tgtloclist, iterationNum, scenario):
    while True:
        for i in range(len(botlot)):
            if botlot[i].tgts == 0:
                continue


            xstep, ystep = safeMove(botlot[i])
            botlot[i].move(xstep, ystep)
            p = getAllPointsInRadius(botlot[i], tgtloclist)

            if not p == False:
                checkTargetWho(p, tgtloclist, tgtlot, botlot[i], botlot)
                print "bot at:", botlot[i].getCenter()


            if checkTargetFound(botlot[i], tgtlot, tgtloclist):
                yield env.timeout(timestep)

            if botlot[i].tgts == 0:
                print botlot[i].config["fill"], "bot all targets found"
                botlot[i].removeFromBlst
                del blst[0:len(blst) - 1]
                winOrder.append(botlot[i].config["fill"])

                #if we stop when one bot gets all its targets
                '''
                winCondition(win, botlot, iterationNum, scenario)
                return 
                '''

            #if all bots collect all targets
            if len(winOrder) == 5:
                winCondition(win, botlot, iterationNum, scenario)
                return



            yield env.timeout(timestep)

#####################################################################
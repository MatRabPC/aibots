from botntgtbuilder import *

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


#####################################################################

def robots(env, timestep, botlot, tgtlot, xupper, tgtloclist):

    while True:

        for i in range(len(botlot)):
            #bot = botlot[i]

            xstep, ystep = safeMove(botlot[i])#BotRandom(botlot[i], xupper) #still just random movement, but safe check too
            print "XYstep:", xstep, ystep
            botlot[i].move(xstep, ystep)
            botlot[i].radar.move(xstep, ystep)
            p = getAllPointsInRadius(botlot[i], tgtloclist)

          #  print tgtlot

            if not p == False:
                checkTargetWho(p, tgtloclist, tgtlot, botlot[i])
                print createPath(botlot[i], p)
              #  print p
              #  botlot[i].move(botlot[i].commCo[0], botlot[i].commCo[1])
              #  botlot[i].radar.move(botlot[i].commCo[0], botlot[i].commCo[1])
                print "bot at:", botlot[i].getCenter()
                
           # if radarCheck(botlot[i], tgtloclist):
                #time.sleep(5)

            #checkLoc(botlot[i], xstep, ystep) #here is what moves us, see botntgtbuilder.py

            if checkTargetFound(botlot[i], tgtlot, tgtloclist):
                yield env.timeout(timestep)
                #if botlot[i].notgts == 0:
                 #   break

              #  print('The bot is at %d, %d' %updateCo(botlot[i]))
              #  print('bot is %d away' %colDet(botlot[i], tgtlot[j]))

            if botlot[i].tgts == 0:
                print botlot[i], "Targets Found"
                del botlot[i]

            if len(botlot) < 1:
                yield env.timeout(timestep)
                print "END"
                break

            yield env.timeout(timestep)

#####################################################################
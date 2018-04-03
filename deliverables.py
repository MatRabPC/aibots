from math import sqrt
import csv

'''
a. a= Scenario number (1,2 or 3)
b. b= Iteration number
c. c= Agent number
d. d= Number of collected targets by the agent
e. e= Number of steps taken by the agent at the end of iteration
f. Agent happiness: f=d/(e+1)
g. g= Maximum happiness in each iteration
h. h= Minimum happiness in each iteration
i. i= Average happiness in each iteration
j. j= Standard deviation of happiness in each iteration
k. Agent competitiveness: k=(f-h)/(g-h)
'''


def fillLine(bot, scenario, iteration):
    t1 = []
    t2 = []
    happiness = []
    lineText = []

    for i in range(1, 6):
        a = scenario
        b = iteration
        c = i#bot[i-1].config["fill"]
        d = getTargetsCollected(bot[i-1], 5)
        e = getSteps(bot[i-1])
        f = calculateHappiness(d, e)
        t1.append([a, b, c, d, e])
        happiness.append(f)
        print t1, happiness

    #print lineText[4]

    for m in range(1, 6):
        g = maxHappiness(happiness)
        h = minHappiness(happiness)
        i = aveHappiness(happiness)
        j = stdHappiness(happiness, i)
        k = (f-h)/(g-h)

        t2.append([happiness[m-1],g, h, i, j, k])

    for i in range(5):
        lineText.append([t1[i][0], t1[i][1], t1[i][2], t1[i][3], t1[i][4], happiness[i], t2[i][0], t2[i][1], t2[i][2], t2[i][3], t2[i][4]])

    return lineText



def getTargetsCollected(bot, tgtMax):
    return tgtMax - bot.tgts

def getSteps(bot):
    return bot.stepsTaken

def calculateHappiness(d, e):
    return round(float(d/(e+1.0)), 4)

def agentCompetitiveness(f, h, g):
    return float((f-h)/(g-h))

def maxHappiness(lst):
    return max(lst)

def minHappiness(lst):
    return min(lst)

def aveHappiness(lst):
    return round(float(sum(lst)) / max(len(lst), 1), 4)

def stdHappiness(lst, mean):
    return round(float(sqrt(sum((x - mean) ** 2 for x in lst) / len(lst))), 4)

def writeToCSV(text):
    with open('G9_1.csv','a') as file:
        for line in text:
            file.write(str(line)[1:-1])
            file.write('\n')
    file.close()

  #  readCSV()

def readCSV():
    i = []
    k = []
    with open('G9_1.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            t = ', '.join(row)
         #   print t.strip().split(",")
            #line.append([t.split(',')])
            line = t.split(',')
            i.append(line[8])
            k.append(line[10])
    print i, k
    csvfile.close()

'''
    with open('G9_2.csv','a') as file:
        for line in i:
            file.write(str(line))
            file.write('\n')
    file.close()
    '''


def fullMakeandWritetoCSV(botlot, scenario, iterationNum):
  #  for i in range(len(botlot)):
    a = fillLine(botlot, scenario, iterationNum)
    #print fillLine(botlot, scenario, iterationNum)
    writeToCSV(a)
    return a
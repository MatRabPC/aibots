from actioncat import actionKitty
import csv

def ave(lst):
    return round(float(sum(lst)) / max(len(lst), 1), 4)

def readCSV():
    i = []
    k = []
    with open('G9_1.csv', 'rb') as f:

        #'''
        spamreader = csv.reader(f, delimiter=',', quotechar='|')
        for row in spamreader:
            t = ', '.join(row)
         #   print t.strip().split(",")
            #line.append([t.split(',')])
            line = t.split(',')
            i.append(line[8][1:])
            k.append(line[10][1:])
   # print i, k

    for m in range(len(i)):
        i[m].replace(',', '')
        i[m].replace(' ', '')
        print i[m]
        i[m] = float(i[m])

        k[m].replace(',', '')
        k[m].replace(' ', '')
        print k[m]
        k[m] = float(k[m])

    i1 = ave(i[0:49])
    i2 = ave(i[50:99])
    i3 = ave(i[100:149])

    k1 = ave(k[0:49])
    k2 = ave(k[50:99])
    k3 = ave(k[100:149])

    full = []

    full.append([1, i1, k1])
    full.append([2, i2, k2])
    full.append([3, i3, k3])


    with open('G9_2.csv','a') as file:
        for line in full:
            file.write(str(line)[1:-1])
            file.write('\n')
    file.close()





#for sc in range(1,4):
 #   for i in range(1, 6):
  #    actionKitty(sc, i)
 #       '''
#readCSV()
actionKitty(1, 1) #scenario 1, iteration 1
actionKitty(2, 1) #scenario 2, iteration 1
actionKitty(3, 1) #scenario 3, iteration 1
#Finding distance between 2 shapes in Nth dimension

import math

#Min
def dmin(a, b):
    min = 1000000000
    for ea in a:
        for eb in b:
            d = math.dist(ea,eb)
            if d < min:
                min = d
    return round(min , 2)

#Max
def dmax(a, b):
    max = 0
    for ea in a:
        for eb in b:
            d = math.dist(ea,eb)
            if d > max:
                max = d
    return round(max , 2)

#Avg
def davg(a, b):
    c = 0
    sum = 0
    for ea in a:
        for eb in b:
            c+=1 
            d = math.dist(ea,eb)
            sum = d + sum
    return round(sum/c , 2)

#Mean
def dmean(a, b):
    ma = []
    for i in range(dim):
        sum = 0
        for j in range(len(a)):
            sum = a[j][i] + sum
        ma.append(sum / dim)
    
    mb = []
    for i in range(dim):
        sum = 0
        for j in range(len(b)):
            sum = b[j][i] + sum
        mb.append(sum / dim)

    d = math.dist(ma, mb)
    return round(d , 2)


str = "x"
dim = 0
counter = 1
curr = "A"
a = []
b = []
dim = int(input("Dimension:"))
print("======================================================")
print("ENTER POINTS IN FORMAT: (X,Y,Z...)")
shapes = [a,b]
#Set up shapes from input
for shape in shapes:
    while str != "" or len(shape) == 0:
        str = input("Input point {} in Class {}: ".format(counter, curr))
        v = []
        str = str.replace(" ", "")
        str = str.replace("(", "")
        str = str.replace(")", "")
        l = str.split(",")
        for e in l:
            if e.isdigit():
                v.append(int(e))
        if len(str) == 0:
            if len(shape) == 0:
                print("Error please enter atleast 1 coordinate!")
            continue
        elif len(v) != dim:
            print("Error please enter {} dimensions!".format(dim))
        else:
            shape.append(v)
            counter += 1
    str = "x"
    curr = "B"
    counter = 1
print("======================STATISTICS======================")
stats = []
stats.append(dmin(a,b))
print("dMin: {}".format(stats[0]))

stats.append(dmax(a,b))
print("dMax: {}".format(stats[1]))

stats.append(davg(a,b))
print("dAvg: {}".format(stats[2]))

stats.append(dmean(a,b))
print("dMean: {}".format(stats[3]))
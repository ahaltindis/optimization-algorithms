import sys, getopt

from random import random
from math import exp
from numpy import mean, std

def simulated_ann(kA, maxIter, x1, x2):
    # parameters
    Ts = 600
    alfa = 0.8

    # borders
    lB = (-10)*kA
    hB = (10)*kA

    # produce S
    S = [x1, x2]
    oCost = cost(S)

    # start iteration
    bC = 0
    curI = 1
    while curI < maxIter:
        nS = produceNeighboor(S, lB, hB)
        nCost = cost(nS)

        delta = nCost - oCost

        if delta < 0 or exp(-delta/Ts) > random():
            bC = nCost
            S = nS
            oCost = nCost
        Ts *= alfa
        curI += 1
    return bC

def produceNeighboor(s, lb, hb):
    ns = [0, 0]

    ns[0] = s[0] + lb+(hb-lb)*random()
    ns[1] = s[1] + lb+(hb-lb)*random()

    return ns

def cost(s):
    x1 = s[0]
    x2 = s[1]
    return 100*((x1**2 - x2)**2) + (1 - x1)**2

def calcAll(ck, ci, cx1, cx2):
    print("========================================")
    print ("x1:",cx1, " x2:",cx2, " kA:",ck, " maxI:", ci)
    print("---------------------------")
    allCost = []

    for i in range(30):
        allCost.append(simulated_ann(ck, ci, cx1, cx2))

    print("mean:", mean(allCost))
    print("std:", std(allCost))

def main(argv):
    ak = 0
    ai = 0
    ax1 = 0
    ax2 = 0

    try:
        opts, args = getopt.getopt(argv,"hk:i:x1:x2:",["ka=","it=","x1=","x2="])
    except getopt.GetoptError:
        print ("usage: simulated_ann.py -k <kA> -i <maxIteration> --x1 <x1> --x2 <x2>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("usage: simulated_ann.py -k <kA> -i <maxIteration> --x1 <x1> --x2 <x2>")
            sys.exit()
        elif opt in ("-k", "--ka"):
            ak = float(arg)
        elif opt in ("-i", "--it"):
            ai = int(arg)
        elif opt in ("-x1", "--x1"):
            ax1 = int(arg)
        elif opt in ("-x2", "--x2"):
            ax2 = int(arg)

    calcAll(ak, ai, ax1, ax2)

if __name__ == "__main__":
    main(sys.argv[1:])


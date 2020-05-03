from copy import deepcopy
from collections import deque
import time
import sys
import numpy as np

    
def AC3(n,file_c,file_r):
    f = open(file_r, 'a')
    file=open(file_c, 'a')
    fullLocations = {}

    assingmentsofcontentues = []
    file.write("\nMAC ALG FOR THE VALUE OF QUEENS VALUE = "+str(n))
    f.write("\nMAC ALG FOR THE VALUE OF QUEENS VALUE = "+str(n))
    for iterator in range(1, n+1):
      assingmentsofcontentues.append(iterator)

    for x in assingmentsofcontentues:
      fullLocations[x] = []
      for iterator1 in range(1, n+1):
        fullLocations[x].append(iterator1)

    nextHouese = {}
    for x in assingmentsofcontentues:
      nextHouese[x] = []

    for i in range(1, n+1):
      for j in range(1, n+1):
        if i == j:
          continue
        nextHouese[i].append(j)
      
    Limitations = []
    
    for xi in nextHouese:
      for xj in nextHouese[xi]:
        Limitations.append([xi, xj])
        

    file.write("\assingmentsofcontentuesS: \n")
    file.write(str(assingmentsofcontentues))
    file.write("\nLimitations: \n")
    file.write(str(Limitations))
    
    ac(Limitations, assingmentsofcontentues, fullLocations, nextHouese)
    file.write("\nfullLocations: \n")
    for x in assingmentsofcontentues:
      file.write(str(fullLocations[x])+"\n")
    
    givingThecontentue = {}
    nrani(assingmentsofcontentues, fullLocations, givingThecontentue, Limitations)
                                                                                                                                 
    if(givingThecontentue):
      for x in assingmentsofcontentues:
        s=str(x)+" -> " +str(givingThecontentue[x])+"\n"
      l=[]
      for i in range(1, n+1):
        for j in range(1, n+1):
          if(givingThecontentue[i] != j):
            l.append("0 ")
          else:
            l.append("1 ")
        l.append("\n")
      l.append("\n\n")
    else:
      print("No Solution")
    f.close()
    file.close()


def sNranisFC(z, rani, Limitationsfile, ResultFile):
    if len(z) == rani:
        return True
    rPros = gettingRProps(z, rani)
    for r in rPros:
        z[r, rani] = 1
        dWOut = False        
        for changer in getCons(z, rani):
            if forwardc(z, changer.r, changer.c):
                dWOut = True
                break   
        if not dWOut:
             if sNranisFC(z, rani + 1, Limitationsfile, ResultFile):
                 return True
        z[r, rani] = 0

def getCons(z, rani):
    final = []
    for r in range(len(z)):
        for c in range(rani+1, len(z)):
            if z[r,c] == 0 and isItC(z, r, c):
                final.append(NotAssigned(r, c))
    return final

def idconsent(givingThecontentue, Limitations, x, content):
    agive = deepcopy(givingThecontentue)
    agive[x] = content

    for C in agive:
      for D in agive:
        c = agive[C]
        d = agive[D]
        if C != D and (c == d or C + c == D + d or C - c == D - d):
          return False
    return True

def isItC(z, r, c):
    return isRC(z,r) and  isCC(z, c) and isDC(z, r, c)

def isRC(z, r):
    for c in range(len(z)):
        if z[r, c] == 1:
            return False
    return True

def isCC(z, c):
    for r in range(len(z)):
        if z[r, c] == 1:
            return False
    return True


def cUD(z, r, c):
    moverows = r
    moveCol = c
    while moveCol >= 0 and moverows >= 0:
        if z[moverows, moveCol] == 1:
            return False
        moveCol -= 1
        moverows -= 1
    return True


def cLD(z, r, c):
    moverows = r
    moveCol = c
    while moveCol >= 0 and moverows < len(z):
        if z[moverows, moveCol] == 1:
            return False
        moverows += 1
        moveCol -= 1
    return True


def isDC(z, r, c):
    return cUD(z, r ,c) and cLD(z, r, c)



def gettingRProps(z, rani):
    rsultset = []
    for r in range(len(z)):
        if isItC(z, r, rani):
            rsultset.append(r)
    return rsultset



    
class Nranis:
    def __init__(self, k):
        self.k = k
        self.sol = 0
        self.file_c=""
        self.file_r=""

    def prove(self,file_r):
        locations = [-1] * self.k
        self.put_rani(locations, 0)
        file=open(file_r, 'a') 
        file.write("Found "+str(self.sol)+ " sol.")
        file.close()
    
    def set_files(self,file_c,file_r):
        self.file_c=file_c
        self.file_r=file_r
        self.prove(file_r)
        
    def unique_sols(self):
        return self.sol

    def put_rani(self, locations, finalloc):
        if finalloc == self.k:
            self.printall(locations)
            self.sol += 1
        else:
            for c in range(self.k):
                if self.onwardchecks(locations, finalloc, c):
                    locations[finalloc] = c
                    self.put_rani(locations, finalloc + 1)


    def onwardchecks(self, locations, conquered, c):
        for i in range(conquered):
            if locations[i] == c or \
                locations[i] - i == c - conquered or \
                locations[i] + i == c + conquered:

                return False
        return True

    def printall(self, locations):
        file=open(self.file_r, 'a') 
        for r in range(self.k):
            line = ""
            for c in range(self.k):
                if locations[r] == c:
                    line += "Q "
                else:
                    line += "x "
            file.write(line)
            file.write("\n")
        file.write("\n")


def nrani(assingmentsofcontentues, fullLocations, givingThecontentue, Limitations):
    if(len(givingThecontentue) == len(assingmentsofcontentues)):
        return givingThecontentue
    for x in assingmentsofcontentues:
        if x not in givingThecontentue:
            break
    for content in fullLocations[x]:
        if idconsent(givingThecontentue, Limitations, x, content):
            givingThecontentue[x] = content
            if(nrani(assingmentsofcontentues, fullLocations, givingThecontentue, Limitations)):
                return givingThecontentue
            givingThecontentue.pop(x)
    return False



def ac(Limitations, assingmentsofcontentues, fullLocations, neighbours):

    line = deque(Limitations)

    while(line):
        couple = line.popleft()
        yi = couple[0]
        yj = couple[1]
        if LookAgain(Limitations, assingmentsofcontentues, fullLocations, yi, yj):
          if len(fullLocations[couple[0]]) == 0:
             return False
          for yk in neighbours[couple[0]]:
            if yk == yj:
              continue
            line.append([yk, yi])
    return True
    

def forwardc(z, r, rani):
    aD = gettingRProps(z, rani)
    tD = list(aD)
    for pR in aD:
        if not isItC(z, pR, rani):
            tD.remove(pR)
    return len(tD) == 0

def LookAgain(Limitations, assingmentsofcontentues, fullLocations, yi, yj):
  lookagainss = False
  for valueX in fullLocations[yi]:
    flag = False
    for contentY in fullLocations[yj]:
      if idconsent({yi:valueX}, Limitations, yj, contentY):
        flag = True
        break
    if not flag:
      fullLocations[yi].remove(valueX)
      lookagainss = True
      
  return lookagainss
    
class NotAssigned:

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __eq__(self, o):
        return self.r == o.r and self.c == o.c

    def __hash__(self):
        return hash(self.r) ^ hash(self.c)
    
def QueenGraph(N):
    return np.array(np.zeros(shape = (N,N), dtype=int))

def Nqueenstestrunner(N,FileConstraints,FileResults,interatorj):
    file = open(FileConstraints, 'a')
    f=open(FileResults, 'a')
    ResultofTimes = []
    f.write("\nNqueens Number of Queens = "+str(N))
    for n in range(0,N,1):
        begin = time.time()
        solution = sNranisFC(QueenGraph(n), 0, FileConstraints, FileResults)
        finish = time.time()
        ResultofTimes.append(finish-begin)

    try:
        f.write("\n The end results :"+str(N) + str(ResultofTimes)+"\n")
        p=ResultofTimes[N-1]*interatorj
        time.sleep(int(p))
        slcik=("Count of Queen :"+str(N)+ " Total_Time_taken : " + str(p) + "\n") 
        f.write(slcik)
    finally:
        f.close()
    print ("completed")

  
    
givenAgorithm=str(sys.argv[1])
N=int(sys.argv[2])
N=2*N
fileConstraints=str(sys.argv[3])
reusltContraints=str(sys.argv[4])
if(givenAgorithm=='FOR'):
    f = open(fileConstraints, 'a')
    f.write("\nNqueens Number of Queens= "+str(N))
    f.write("\n****************************************************************")
    f.write("\nValues and Constraints:\nGiven constraint C(i,interatorj)=> \nWith all Qi=A and Qinteratorj=B will work only with the constraints if and only if \n1. A!=B -> horiziontal placments\n2. |A-B|!=|i-interatorj| -> same diagnol placements not allowed. \n3. same column values will also contradict")
    f.write("\n****************************************************************")
    f.write("\nDomain:\n")
    slick = [i for i in range(1,N+1)]
    f.write(str(slick))
    f.write("\n****************************************************************")
    f.write("\nVariables: \n")
    for interatorj in range(N):
        slick="Q"+str(interatorj+1)+" "
        f.write(slick)
    f.write("\n****************************************************************")
    
    f.write("\nStart of states: \n")
    f.write(str(QueenGraph(0)))  
    f.write("\n****************************************************************")
    f.close()
    f=Nranis(N)
    f.set_files(fileConstraints,reusltContraints)
    interatorj=f.unique_sols()
    Nqueenstestrunner(N,fileConstraints,reusltContraints,interatorj)   
elif(givenAgorithm=='MAC'): 
    f=Nranis(N)
    f.set_files(fileConstraints,reusltContraints)
    interatorj=f.unique_sols()
    begin = time.time()
    AC3(N,fileConstraints,reusltContraints)
    finish = time.time()
    full=finish-begin
    pinacle=full*interatorj
    time.sleep(pinacle)
    file=open(reusltContraints, 'a')
    stringer=("\nThe value of Queens :"+str(N)+ " Total_Time_Taken : " + str(pinacle) + "\n") 
    file.write(stringer)
    
    file.close()
    constraints=open(fileConstraints, 'a')
    constraints.write("\Start: \n")
    constraints.write(str(QueenGraph(0)))
    constraints.write("\nVariables: \n")
    for interatorj in range(N):
        stringer="Q"+str(interatorj+1)+" "
        constraints.write(stringer)
    constraints.close()
else: 
    print("algorithm not found!")
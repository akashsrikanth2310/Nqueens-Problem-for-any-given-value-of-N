import NQueensSolver
import time
import sys
from random import randint
import numpy as np



def QueenGraph(N):
    return np.array(np.zeros(shape = (N,N), dtype=int))

def Nqueenstestrunner(N,FileConstraints,FileResults,interatorj):
    file = open(FileConstraints, 'a')
    f=open(FileResults, 'a')
    ResultofTimes = []
    f.write("\nNqueens Number of Queens = "+str(N))
    for n in range(0,N,1):
        begin = time.time()
        solution = NQueensSolver.sNranisFC(QueenGraph(n), 0, FileConstraints, FileResults)
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
    f=NQueensSolver.Nranis(N)
    f.set_files(fileConstraints,reusltContraints)
    interatorj=f.unique_sols()
    Nqueenstestrunner(N,fileConstraints,reusltContraints,interatorj)   
elif(givenAgorithm=='MAC'): 
    f=NQueensSolver.Nranis(N)
    f.set_files(fileConstraints,reusltContraints)
    interatorj=f.unique_sols()
    begin = time.time()
    NQueensSolver.AC3(N,fileConstraints,reusltContraints)
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
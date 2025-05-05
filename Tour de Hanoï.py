import time
import csv 
def hanoi(n,A,B,C):
    if (n==1):
        print("Transfère de ",A,"vers",C)
    else:
        hanoi(n-1,A,C,B)
        print("Transfère de", A , "vers", C)
        hanoi(n-1,B,A,C)   

def tempsH(n,A,B,C):
    #début du programme (chronomètre)
    debut = time.time()
    
    hanoi(n,A,B,C)
    
    #Fin du programme (chronomètre)
    fin = time.time()
    return round((fin-debut),6)

t=[]
t.append((1,tempsH(1,"A","B","C")))
t.append((2,tempsH(2,"A","B","C")))

for i in range(5,20,5):
    temp = tempsH(i,"A","B","C")
    t.append((i,temp))

for x in t:
    print(x[0]," : ",x[1])
    
"""
def Hanoi(n,A,B,C):
    
    if n!=0:
        if P = A:
            Hanoi(n-1,A)
        else
            Hanoi(n-1,I)
            Déplacer le disque P vers A
            Hanoi()


def Hanoi(n,A,B,C):
    if n!=0:
        if P = A
            Hanoi(n-1,A)
        else
            Hanoi(n-1,I)
            Déplacer le disque P vers A
            Hanoi()

def hanoi3(n,A,B,C)
    if (n=1):
        écrire("Transfère de ",A,"vers",C)
    else:
        hanoi3(n-1,A,C,B)
        écrire("Transfère de", A , "vers", C)
        hanoi(n-1,B,A,C)
        
def tower_of_hanoi(n, source, destination, helper):
	if n==1:
		print ("Move disk 1 from peg", source," to peg", destination)
		return
	tower_of_hanoi(n-1, source, helper, destination)
	print ("Move disk",n," from peg", source," to peg", destination)
	tower_of_hanoi(n-1, helper, destination, source)		
# n = number of disks
n = 3
tower_of_hanoi(n,' A','B','C')

"""

def printMv(fr,to):
    print(" move from " + str(fr) + " to " + str(to))
    
def Towers(n, fr, to, spare):
    if n==1:
        printMv(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(3,1,3,2))        
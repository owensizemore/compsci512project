import sys

def SortingFiveNumbers():
    for line in sys.stdin:
        num=list(map(int,line.split()))
        
        num.sort()
        num.reverse()
        print(' '.join(map(str,num)))
        
            
                
    
SortingFiveNumbers()
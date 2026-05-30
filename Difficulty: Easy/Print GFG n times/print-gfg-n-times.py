n = int(input())

# Code here
def GFG(n):
    if n==0:
        return
    print("GFG",end=" ")
    GFG(n-1)
    
GFG(n)  

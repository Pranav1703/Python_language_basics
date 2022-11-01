#Take the input
n = int(input())


#initialize the variable sm with value zero.
sm = 0

for i in range(0,n+1):
    
    if(i % 2 == 0):
        sm += i

#print the value of sum.        
print(sm)

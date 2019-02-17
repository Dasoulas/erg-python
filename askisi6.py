import random
x=input("Δώσε τον αριθμό των γραμμών ")
y=input("Δώσε τον αριθμό των στηλών ")
b=input("Δώσε τον αριθμό των βομβών")
k=x*y
m=["-","*"]
while k<b:
    b=input("Δώσε τον αριθμό των βομβών")
A=[]
sb=0
for i in range (x):
    L=[]
    for j in range (y):
        if sb<=b:
            dt=random.choice(m)
            if dt=="*":
                sb=sb+1
            L.append(dt)
        else:
            L.append("-")
    A.append(L)
for deikse in A:
    print deikse 



    
  


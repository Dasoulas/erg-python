import random
x=input("���� ��� ������ ��� ������� ")
y=input("���� ��� ������ ��� ������ ")
b=input("���� ��� ������ ��� ������")
k=x*y
m=["-","*"]
while k<b:
    b=input("���� ��� ������ ��� ������")
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



    
  


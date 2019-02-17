def summintervals(distance):
    mkoin = []
    for i in range(len(distance)):
        mkoin.append(distance[i][0])
        mkoin.append(distance[i][-1])
    mkoin.sort()

    
    koin=[]
    afair = -1
    for i in range (len(distance)):
        afair=afair +1
        for g in range (distance[afair][0]+1,distance[afair][-1]):
            koin.append(g)


    mk=set(mkoin)
    k=set(koin)
    distance.difference_update(k)
    mkn=list(mk)
    print(koin)
    print(mkoin)
    s=0
    for i in range(0,len(mkn)-1,2):
        s=mkn[i+1]-mkn[i]+s

    print(s)


        

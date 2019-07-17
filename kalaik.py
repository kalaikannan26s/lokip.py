import math
pss,qss=map(int,input().split())
rr1=[]
ss1=list(map(int,input().split()))
for i in range(0,qss):
        uu,vv =map(int,input().split())
        rr1.append([uu,vv])
for i in rr1:
        x1=i[0]-1
        y1=i[1]-1
        print(math.gcd(s1[x1],s1[y1]))

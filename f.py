r1=int(input())
flag2=0
if r1>2:
    for i in range(3,int(r1/2)):
        if r1%i==0:
            flag2=1
            print("no")
            break
if flag2==0 or r1==2:
    print("yes")

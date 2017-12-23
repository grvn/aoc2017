from sys import argv

initb=int(argv[1])
b=100000+(initb*100)
b0=b
c=b+17000
d=0
e=0
f=0
h=0
count=0

def ifprime(n):
    if n<2:
        return False
    return all(n%x!=0 for x in range(2,int(n**0.5)+1))
        
for i in range(b0,c+1,17):
    if not ifprime(i):
        count+=1
print("Answer:",count)


# 'assembly'-koden kan bli typ:
#for _ in range(b,c,17):
#    f=1
#    d=2
#    while True:
#        e=2
#        while True:
#            if d*e==b: <----- Detta itererar alla heltalsmultiplikationer, endast b=primtal tar sig igenom
#                f=0    <----- Man vill att den exekverar om h+=1 ska exekvera
#            e+=1
#            if e==b:
#                break
#        d+=1
#        if d==b:
#            break
#    if f==0:
#        h+=1
#    if b>=c:
#        break

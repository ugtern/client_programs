import random

a=[3,7,2,9]
b=[[1]]
c=[]
sum=1

def cal(a,sum):
    i=0
    j=0
    z=0
    while i<len(a):
        c = b*a[i]
        while j<a[i]:
            
            j+=1
            
        sum*=a[i]
        j=0
        i+=1
        print(c[i])
        print(c,sum)
        
cal(a,sum)
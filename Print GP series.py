def GP(a,b,n):
    r=b/a
    res=a*(r**(n-1))
    print(int(res))

t=int(input())

while(t>0):
    x, y = map(int, input().split())
    n=int(input())
    GP(x,y,n)
    t=t-1
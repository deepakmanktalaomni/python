def fibonacci(n):
    a,b = 0,1
    while a < n:
        print(a,end = '\n')
        a,b = b, a+b

fibonacci(20000000)
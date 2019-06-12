i = int(input())

for j in range (2,i):
    for m in range (2,j):
        if j % m == 0:
            print (j, 'equals', m, 'x', j//m)
            break
    else:
            print(j, 'is a prime number')
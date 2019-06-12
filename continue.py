numberstaken = [2, 55, 34, 21, 76, 54, 64]


print("here are the jursey numbers available")
countlistnumber=0
countnotinlist=0

for n in range(100):
    if n in numberstaken:
        countlistnumber+=1
        continue
    else:
        print(n)
        countnotinlist+=1

print(countlistnumber)
print(countnotinlist)
# A Sample Python program for beginners with Competitive Programming

# Returns index of x in arr if it is present,
# else returns -1

def search(arr,x):
    n = len(arr)
    for j in range(0,n):
        if x==arr[j]:
            return j
    return -1
#Input number of test cases
print ("Enter input number of test cases")

t=int(input())

for i in range(0,t):
    print("Enter Size of array")
    n=int(input())
    print("Input the array values")
    arr = list(map(int,input().split() ))
    print("Input the element to be searched")
    x = int(input())
    print(search(arr,x))
    arr.index(x)


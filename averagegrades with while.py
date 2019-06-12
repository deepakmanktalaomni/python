total = 0
count = 0
grades =(int(input("Enter your grades dear :  ")))
while grades > 0:
    total += grades
    count += 1
    grades = int(input("Enter new grades or a value <= 0 to quit and get average"))

avg = total/count
print("So the average is %5.2f for grades for %5d  students " %(avg,count))
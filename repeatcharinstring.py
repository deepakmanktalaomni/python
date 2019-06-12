mystring = "This is the chatcterAND you need TO COUnt How many of each chare are there"

l = list(mystring)


count = 0
counts = []
text = []
len= int(len(mystring))

for m in l:
    if m not in text:
        text.append(m)


for k in text:
    count = 0
    if k in l:
        count += 1
    print (k,count)


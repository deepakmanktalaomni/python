import pprint

message = ' It was a bright summer day with a lot of sunshine, giving Vitamin D to the kids playing in open sun.'

count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

print(count)
pprint.pprint(count)
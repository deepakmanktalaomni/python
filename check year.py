y = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))

if 0 <= y and 0 < m < 13 and 0 < d < 32: #Check whether date is under limit.

    if m in (4,6,9,11):
        if d > 30:
            print("<Wrong>")
        else:
            print("<Correct>")

    elif y % 4 == 0: # Every 4 year "Leap" year occures so checking...
        if m == 2: # In "Leap" year February has 29 days
            if d < 30:
                print("<Correct>")
            else:
                print("<Wrong>")

    elif m == 2: # But if it's not "Leap" year February will have 28 days
        if d < 29:
            print("<Correct>")
        else:
            print("<Wrong>")
    elif y % 4 != 0 and m != 2: # Otherwise print "Correct"
        print("<Correct>")


else:
    print("<Wrong>")
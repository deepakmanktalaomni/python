from datetime import date


def main():

    bornBefore = date(1997,4,22)

    Date = promptAndExtractDate()

    while Date is not None:
        if Date <= bornBefore:
            print("Is at least 21 years of age: ", Date)
        Date = promptAndExtractDate()

def promptAndExtractDate():
    print("Enter a birth date")
    month = int(input("month(0 to quit"))
    if month == 0:
        return  None
    else :
        day     = int(input("day : "))
        year    = int(input("year : "))
        return date(year, month,day)


main()
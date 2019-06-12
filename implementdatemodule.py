class Date:

    def  _isValidGregorian( m, d, y):
        y = int( input( "Year: " ) )
        m = int( input( "Month: " ) )
        d = int( input( "Day: " ) )

        if 0 <= y and 0 < m < 13 and 0 < d < 32:  # Check whether date is under limit.

            if m in (4, 6, 9, 11):
                if d > 30:
                    print( "<Wrong>" )
                else:
                    print( "<Correct>" )

            elif y % 4 == 0:
                if m == 2:
                    if d < 30:
                        print( "<Correct>" )
                    else:
                        print( "<Wrong>" )

            elif m == 2:
                if d < 29:
                    print( "<Correct>" )
                else:
                    print( "<Wrong>" )
            elif y % 4 != 0 and m != 2:
                print( "<Correct>" )


        else:
            print( "<Wrong>" )

    def __init__(self, month, day, year):
        self._julianday = 0
        assert self._isValidGeorgian( m, d, y), \
                "Invalid Gregorian date."



        tmp = 0
        if month < 3:
            tmp = -1
            self._julianday = day - 32075 + \
                              (1461 *(year + 4800 + tmp) // 4) + \
                              (367 * (month - 2 - tmp *12 ) // 12) - \
                              (3 * ((year + 4900 + tmp) // 100) // 4)

    def month(self):
        return (self._toGregorian())[0]


    def day(self):
        return (self._toGregorian())[1]

    def year(self):
        return (self._toGregorian())[2]


    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
            return ((13 * month) + 3 // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" %(month, day, year)

    def __eq__(self, otherDate):
        return self._julianday == otherDate._julianday

    def __lt__(self, otherDate):
        return self._julianday < otherDate._julianday

    def __le__(self, otherDate):
        return self._julianday <= otherDate._julianday

    def _toGregorian(self):
        A = self._julianday + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    def  _isValidGregorian(self, m, d, y):
        y = int( input( "Year: " ) )
        m = int( input( "Month: " ) )
        d = int( input( "Day: " ) )

        if 0 <= y and 0 < m < 13 and 0 < d < 32:  # Check whether date is under limit.

            if m in (4, 6, 9, 11):
                if d > 30:
                    print( "<Wrong>" )
                else:
                    print( "<Correct>" )

            elif y % 4 == 0:
                if m == 2:
                    if d < 30:
                        print( "<Correct>" )
                    else:
                        print( "<Wrong>" )

            elif m == 2:
                if d < 29:
                    print( "<Correct>" )
                else:
                    print( "<Wrong>" )
            elif y % 4 != 0 and m != 2:
                print( "<Correct>" )


        else:
            print( "<Wrong>" )



firstDay = Date(0,0,0)
print(firstDay)

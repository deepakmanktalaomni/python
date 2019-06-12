def PrintTable(n):
    s = ''
    for i in range( 1, 11 ):
        s += str( n * i ) + ' '
    return s


if __name__ == '__main__':
    t = int( input() )
    for i in range( t ):
        n = int( input() )
        print( PrintTable( n ) )
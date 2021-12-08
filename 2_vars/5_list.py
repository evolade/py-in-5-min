intList = [ 1, 7, 3, 10 ]

mixedList = [ "Lorem", True, 22, 3.14 ]








length = len( mixedList ) # = 4








# get specific element
# !!! arrays start at 0

print( mixedList[0] ) # Lorem

print( mixedList[2] ) # 22

print( mixedList[-1] ) # 3.14








# print list elements

for i in range( len(mixedList) ):
    print( mixedList[i] )

for i in mixedList:
    print( i )








# add, change, remove, sort, reverse, clear

mixedList.append( "ipsum" ) # = ['Lorem', True, 22, 3.14, 'ipsum']

mixedList[ 2 ] = 5 # = ['Lorem', True, 5, 3.14, 'ipsum']

mixedList.pop() # = ['Lorem', True, 22, 3.14]

mixedList.pop( 1 ) # = ['Lorem', 22, 3.14, 'ipsum']

intList.sort() # = [1, 3, 7, 10]

intList.reverse() # = [10, 7, 3, 1]

intList.clear() # = []

def sayHello():
    print( "Hello" )
    
sayHello()








def loop( arr ):
    for i in range( len(arr) ):
        print( str(i + 1) + ". " + arr[i] )

myArr = [ "Lorem", "ipsum", "dolor" ]

loop( myArr )








def add( num1, num2, num3 ):
    #print( num1 + num2 + num3 )
    return num1 + num2 + num3

add( 20, 25, 10 )

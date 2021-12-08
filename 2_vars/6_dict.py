# <keys>: <values>
roadster = {
    "brand": "Tesla",
    "model": "Roadster",
    "price": 200000,
    "available": False
}

print( roadster["available"] )

roadster[ "available" ] = True

print( roadster.items() )








# access elements

for i in roadster.keys():
    print( i )

for i in roadster.values():
    print( i )

for i, j in roadster.items():
    print( i, j )








roadster[ "year" ] = 2023 # adds new element

roadster.pop( "available" ) # removes "available" element

roadster.popitem() # removes last element

roadster.clear()

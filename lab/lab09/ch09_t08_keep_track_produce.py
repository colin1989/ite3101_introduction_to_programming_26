prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for p in prices:
    print("%s" % p)
    print("price: %s" % prices[p])
    print("stock: %s" % stock[p])
    
for p in prices:
    print("%s \n price : %i \n stock : %i" % p, prices[p], stock[i])
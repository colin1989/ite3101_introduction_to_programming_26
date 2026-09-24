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
    p = prices[p]
    print("%s \n price : %s \n stock : %s" % p, prices[p], stock[p])
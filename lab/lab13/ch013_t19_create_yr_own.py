lst1 = [0, 1, 2]
lst2 = [-1, 0, 1]

for a, b in zip(lst1, lst2):
    print(str(max(a, b)))
else:
    print("End")
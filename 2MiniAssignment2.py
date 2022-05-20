lst1 = ["Hello ", "take "]
lst2 = ["Dear", "Sir"]

res = [x + y for x in lst1 for y in lst2]
print(res)
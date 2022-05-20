dict= {'HuEx': [1, 3, 4],'is': [7, 6], 'best': [4, 5]}
print("Original dict is :"+str(dict))
result=[]
for key,val in dict.items( ):
    result.append([key]+val)
print("new list is :"+str(result))
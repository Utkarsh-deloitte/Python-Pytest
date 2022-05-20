def duplicate(s):
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1;
        else:
            dic[i] = 1;
    for key, value in dic.items():
        if (value > 1):
            print(str(key) + "->" + str(value))
s = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
for x in s:
    duplicate(x)
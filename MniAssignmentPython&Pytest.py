from collections import Counter


class StringClass:
    def __init__(self, value, ):
        self.value = value

    def list(self):
        return list(self.value)

    def length(self):
        return len(self.value)

    def Strconvert(self, strlist):
        print(list(strlist))


class PairsPossible(StringClass):

    def Store(self, Pair_list):
        result = [(x, y) for idx, x in enumerate(Pair_list) for y in Pair_list[idx + 1:]]
        print("The pairList is:\n", result)


class SearchCommonElements:

    def __init__(self, x, z):
        self.x = x
        self.z = z

    def common(self):
        dict1 = Counter(self.x)
        print(dict1)
        dict2 = Counter(self.z)
        common = dict1 & dict2
        common_list = list(common)
        print("Common elements between x and z: ", common_list)
        return common_list


class EqualSumPairs:
    def __init__(self, pairspossible):
        self.sum_list = []
        self.pairspossible = pairspossible

    def notequaltosum(self):
        for pair in self.pairspossible:
            inner = [int(i) for i in pair]
            self.sum_list.append(sum(inner))
        not_duplicate_sum = []
        [not_duplicate_sum.append(sums) for sums in self.sum_list if sums not in not_duplicate_sum]
        print("The count of pairs who's sum is not duplicate: " + str(len(not_duplicate_sum)))


x = input("Enter the value:")
y = StringClass(x)
z = "143"
print("The List is:", y.list())  # converting the string into char.
print("The length of the String:", y.length())
c = y.list()
d = PairsPossible(y)
d.Store(c)
e = SearchCommonElements(x, z)
e.common()
f = EqualSumPairs(y.list())
f.notequaltosum()
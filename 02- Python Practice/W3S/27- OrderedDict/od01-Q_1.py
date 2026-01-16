from collections import OrderedDict

o1 = OrderedDict()

for i,j in zip(range(1,6,1),range(6,1,-1)):
    o1[i] = j

for i , j in o1.items():
    print(str(i) + " " + str(j))

print("\n\n")

o2 = {1 : 6, 2 : 5 , 3 : 4 , 4 : 3 , 5 : 2 }

o3 = {1 : 6, 2 : 5 , 3 : 4  , 5 : 2 ,4 : 3}
print(OrderedDict(o1) == OrderedDict(o2))
print(OrderedDict(o1) == OrderedDict(o3))
print(OrderedDict(o2) == o3)
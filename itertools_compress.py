import itertools

lst1=['a','b','c','d','e','f','g']
lst2=[True,False,True,True,False,True,False]

selectors=itertools.compress(lst1,lst2)
for i in selectors:
    print(i)

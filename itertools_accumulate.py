import itertools

lst1=[1,2,3,4,5,6,7,8,9,10]
print(lst1)

total=itertools.accumulate(lst1)
print(list(total))

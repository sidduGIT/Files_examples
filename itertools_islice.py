import itertools 

with open('file1.txt','r') as fr:
    some_lines=itertools.islice(fr,4)
    for i in some_lines:
        print(i)

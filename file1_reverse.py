with open('file1.txt','r') as fh:
    data=fh.readlines()
    #data=reversed(data)
    for line in data:
        print(line[::-1])

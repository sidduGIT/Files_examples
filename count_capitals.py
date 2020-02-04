with open('content.txt','r') as fh:
    count=0
    for line in fh:
        for char in line:
            if char.isupper():
                count+=1
print(count)

#Write a Python program to read an entire text file
with open('input.txt','r') as fh:
    #data=fh.read()
    #print(data)
    print(fh.read())

#Write a Python program to read first n lines of a file.

with open('input.txt','r') as fh:
    data=fh.readlines()
    for i in data[:3]:
        print(i)
    #print(data[:3])

#Write a Python program to append text to a file and display the text.

#with open('input.txt','a') as fh:
    #fh.write('hi siddu how are you')
    #fh.write('I am fine how are you')
#with open('input.txt','r') as fh:
 #   data=fh.read()
 #   print(data)

#Write a Python program to read last n lines of a file.

with open('input.txt','r') as fh:
    data=fh.readlines()
    print('printing lines from last')
    for line in data[-5:]:
        print(line)

#Write a Python program to read a file line by line and store it into a list.
with open('input.txt','r') as fh:
    data=fh.readlines()
    print(data)
    for i in data:
        print(i)

#Write a Python program to read a file line by line store it into an array.

with open('input.txt','r') as fh:
    data=[]
    for line in fh:
        data.append(line)
    print(data)

#Write a python program to find the longest words.

with open('content.txt','r') as fh:
    data=fh.read()
    words=data.split()
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
    print('the longest word in a file')
    print(longest)

#find the words in a file whose length is greater than 8 chars

with open('content.txt','r') as fh:
    lst=[]
    data=fh.read()
    words=data.split()
    for word in words:
        if len(word)>8:
            lst.append(word)
    print('words greater than 8 chars')
    for word in lst:
        print(word)

#find the words in a file whose length is greater than 6 chars and smaller than 12 chars

with open('content.txt','r') as fh:
    lst=[]
    data=fh.read()
    words=data.split()
    for word in words:
        if len(word)>6 and len(word)<12:
            lst.append(word)
    print('words greater than 6 chars ad smaller then 12')
    for word in lst:
        print(word)

#Write a Python program to count the number of lines in a text file.

with open('input.txt','r') as fh:
    data=fh.readlines()
    print('number of lines=',len(data))

with open('input.txt','r') as fh:
    data=fh.read().split('\n')
    count=0
    for line in data:
        count+=1
        print(line)
    print(count)

#Write a Python program to count the frequency of words in a file.

with open('content.txt','r') as fh:
    words=fh.read().split()
    dict1={}
    for word in words:
        if word not in dict1:
            dict1[word]=1
        else:
            dict1[word]+=1
    print('frequency of words in a file')
    for k,v in dict1.items():
        print(k,v)

#Write a Python program to write a list to a file.

lst=['abc','defg','hijk','lmno','pqrst','uvwxyz']
with open('input.txt','w') as fh:
    for word in lst:
        fh.write(word)
        fh.write('\n')

#Write a Python program to copy the contents of a file to another file .

with open('content.txt','r') as fr:
    data=fr.read()
with open('content_copy.txt','w') as fw:
    fw.write(data)

with open('content_copy.txt','r') as fh:
    print(fh.read())

#Write a Python program to combine each line from first file with the corresponding line in second file.

with open('file1.txt','r') as fr1:
    data1=fr1.readlines()
with open('file2.txt','r') as fr2:
    data2=fr2.readlines()
with open('file1_file2.txt','w') as fw:
    for d1,d2 in zip(data1,data2):
        fw.write(d1)
        fw.write(d2)
with open('file1_file2.txt','r') as fr:
    print(fr.read())

#Write a Python program to read a random line from a file

from random import choice
with open('file1.txt','r') as fr1:
    data1=fr1.readlines()
    print(choice(data1))

with open('file1.txt','r') as fr1:
    data1=fr1.read().splitlines()
    print(choice(data1))

#Write a Python program to assess if a file is closed or not.

fr=open('file1.txt','r')
print(fr.closed)
fr.close()
print(fr.closed)

#Write a Python program to remove newline characters from a file.

with open('file1.txt','r') as fr1:
    data=fr1.readlines()
    print([line.rstrip('\n') for line in data])
with open('file1.txt','r') as fr1:
    data=fr1.read().split('\n')
with open('file_nonewline.txt','w') as fw:
    for i in data:
        fw.write(i)






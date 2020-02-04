with open('file1.txt','r') as fr:
    with open('file1_copy.txt','w') as fw:
        for line in fr:
            fw.write(line)

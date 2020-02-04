with open('log.txt') as fr:
    for line in fr:
        split_line=line.split('\t')
        #print(split_line)
        print(split_line[1],split_line[4])

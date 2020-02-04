with open('large.txt','r') as fr:
    with open('large_copy.txt','w') as fw:
        chunk_size=4096
        fr_chunk=fr.read(chunk_size)
        while len(fr_chunk)>0:
            fw.write(fr_chunk)
            fr_chunk=fr.read(chunk_size)

import os

os.chdir('videos')
for fil in os.listdir():
    split_name=fil.split(' - ')
    split_ext=split_name[2].split('.')
    print(split_ext[0].lstrip('#')+' '+split_name[0]+'.'+split_ext[1])

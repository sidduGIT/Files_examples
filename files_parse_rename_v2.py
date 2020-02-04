import os 

os.chdir('videos')

for f in os.listdir():
    fname,fext=os.path.splitext(f)
    ftitle,fcourse,fnum=fname.split(' - ')
    
    ftitle=ftitle.strip()
    fcourse=fcourse.strip()
    fnum=fnum.strip()[1:].zfill(2)
    new_name='{}-{}{}'.format(fnum,ftitle,fext)
    print(new_name)
    #os.rename(f,new_name)

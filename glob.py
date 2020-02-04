from pathlib import Path

path=Path()
for fil in path.glob('*.*'):
    print(fil) #prints only files

for fil in path.glob('*'):
    print(fil) #prints files as well as directory


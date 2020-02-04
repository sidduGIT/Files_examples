from pathlib import Path

path=Path('directory')
print(path.exists()) #return True if directory exists else false

path=Path('emails')
print(path.mkdir())  #creates a directory emails
print(path.exists()) #chack for existance
print(path.rmdir())  #remove emails direcory and check again for existance
print(path.exists()) #chack for existance



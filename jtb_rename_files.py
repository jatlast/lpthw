import os

def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files("."):  
    print (file)

# use the following link on how to rename files using "os.rename(src, dst)""
# https://www.guru99.com/python-rename-file.html
import glob
import os

l = os.listdir(path='.')
for lname in l:
    if os.path.basename(__file__) in lname:
        continue
    print(lname)
    os.system(r"mklink /D C:\usr\{} D:\usr\{}".format(lname, lname))
import glob
import pathlib
import os.path
import re


p_temp = pathlib.Path('.')

old_photo_list = []
new_photo_list = []
for mov in p_temp.glob("**/*"):
    m = re.search(r"IMG_(\d\d\d\d\d\d\d\d)\.mov", str(mov), re.I)
    if m:
        old_photo_list.append(int(m.group(1)))
    else:
        m2 = re.search(r"(IMG_\d{1,6}\.mov)", str(mov), re.I)
        if m2:
            new_photo_list.append(m2.group(1))

old_photo_list.sort()
# print(old_photo_list)

new_photo_list.sort()
count = int(old_photo_list[-1]) + 1

def rename_file(fullpath: str):
    dirname = os.path.dirname(fullpath)
    global count
    count += 1
    root, ext = os.path.splitext(fullpath)
    count_str = str(count).zfill(8)
    # print(root, ext)
    return dirname + "\\" + "IMG_" + count_str + ext


my_glob = p_temp.glob("*/*.*")
for m in my_glob:
    m2 = re.search(r"(IMG_\d{1,6}\.mov)", str(m), re.I)
    if m2:
        name = rename_file(str(m))
        print("ren " + '"' +str(m) + '"' + " " + '"' + name + '"')
        os.rename(str(m), name)

my_glob = p_temp.glob("*/*/*.*")
for m in my_glob:
    m2 = re.search(r"(IMG_\d{1,6}\.mov)", str(m), re.I)
    if m2:
        name = rename_file(str(m))
        print("ren " + '"' +str(m) + '"' + " " + '"' + name + '"')
        os.rename(str(m), name)

my_glob = p_temp.glob("*/*/*/*.*")
for m in my_glob:
    m2 = re.search(r"(IMG_\d{1,6}\.mov)", str(m), re.I)
    if m2:
        name = rename_file(str(m))
        print("ren " + '"' +str(m) + '"' + " " + '"' + name + '"')
        os.rename(str(m), name)

my_glob = p_temp.glob("*/*/*/*/*.*")
for m in my_glob:
    m2 = re.search(r"(IMG_\d{1,6}\.mov)", str(m), re.I)
    if m2:
        name = rename_file(str(m))
        print("ren " + '"' +str(m) + '"' + " " + '"' + name + '"')
        os.rename(str(m), name)

print(count)









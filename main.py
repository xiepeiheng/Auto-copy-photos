import os
import shutil

def obtain(path):
    cmy = []
    for i in os.listdir(path):
        path1 = path + '/' + i
        if os.path.isdir(path1):
            cmy.append(path1)
    return cmy

def rename(path):
    cmy = []
    num = 1
    for i in path:
        for j in os.listdir(i):
            if os.path.splitext(j)[1]=='.heic' or os.path.splitext(j)[1]=='.HEIC':
                oldname = i + '/' + j
                newname = i + '/' + str(num) + '.heic'
                num = num + 1
                os.rename(oldname, newname)
                cmy.append(newname)
    return cmy

def move(path, newpath):
    for i in path:
        shutil.copy(i, newpath)


original = 'C:/Users/谢佩恒/Desktop/graduation photo'
destination = 'C:/Users/谢佩恒/Desktop/Destination'

#获取所有照片地址的数组
path = obtain(original)
rename_path = rename(path)
move(rename_path, destination)
print('OK')
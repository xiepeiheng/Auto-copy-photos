# Python文件操作笔记

## <font color=orange>os.walk()</font>

参数为想要遍历的文件夹的绝对地址

会遍历一个文件夹中的全部文件以及文件夹并以一定格式返回他们的名称，会出现两种斜杠的问题所以不推荐使用。

## <font color=orange>os.listdir()</font>

参数为文件夹的绝对地址

以数组的形式返回一个文件夹中的全部文件以及文件夹，显示文件的时候会带上后缀。

本文件夹的目录如下

```
Original
│  hxy.py
│  xxx.txt
│  
├─cmy
│      cmy.txt
│      photo.heic
│      
├─jsk
│      jsk.txt
│      photo.HEIC
│      
└─zfh
        photo.jpg
        zfh.HEIC
```

打印`os.listdir('C:\Users\谢佩恒\Desktop\Original')`的结果可以得到数组`['cmy', 'hxy.py', 'jsk', 'xxx.txt', 'zfh']`

## <font color=orange>os.path.isdir()</font>

判断是否为文件夹

需要使用绝对地址，返回true或者false

## <font color=orange>os.path.splitext()</font>

将文件的名称输入，会返回一个元组，包括两个元素分别是文件名和扩展名

```python
print(os.path.splitext('zfh.txt'))
```

会得到`('zfh', '.txt')`

## <font color=orange>os.path.split()</font>

输入文件的绝对地址，会返回一个元组，包括两个元素分别是文件地址和文件名

```python
print(os.path.split('C:/Users/谢佩恒/Desktop/Original/cmy/photo.heic'))
```

会得到`('C:/Users/谢佩恒/Desktop/Original/cmy', 'photo.heic')`

## <font color=orange>os.rename()</font>

重命名，输入文件的旧绝对路径转换为新的绝对路径

os.rename(oldpath, newpath)

在大批量复制的时候，如果两个名字相同的文件复制进了同一个文件夹还会导致前一份被覆盖。因此需要复制进去之后重命名

##  <font color=orange>shutil.copy()</font>

需要引入`shutil`模块，该模块无需下载安装，均为绝对路径

shutil.copy(path, dir)

path为文件的绝对路径，dir为文件夹的绝对路径。将文件复制进文件夹中

## <font color=orange>os.startfile()</font>

输入绝对路径后直接打开文件或者应用，如输入exe所在的路径屏幕上会显示该应用被打开



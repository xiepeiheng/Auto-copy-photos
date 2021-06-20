# 自动提取苹果live格式照片中的HEIC图片文件

用苹果手机live模式拍摄完照片后导入win平台电脑后会产生格式如下的文件夹

```
graduation photo
│  
├─IMG_1510.pvt
│      FullSizeRender.heic
│      FullSizeRender.mov
│      metadata.plist
│      
├─IMG_1511.pvt
│      FullSizeRender.heic
│      FullSizeRender.mov
│      metadata.plist
│      
├─IMG_1645.pvt
│      FullSizeRender.HEIC
│      FullSizeRender.mov
│      metadata.plist
│      
└─IMG_1646.pvt
│      FullSizeRender.HEIC
│      FullSizeRender.mov
│      metadata.plist
```

作为样例这里只有四张照片，实际上会有很多照片，为了只将`heic`格式的照片都提取到一个文件夹中，百度了点Python相关文件操作，写了这个东西

只需运行`main.py`文件即可完成转移操作，并附带学习时制作的笔记

提醒大家在一些情况下不要使用live模式。这会导致传给非苹果手机使用者时图片质量会有所下降


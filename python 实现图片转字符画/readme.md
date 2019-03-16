### 先上效果

![](http://po4tl1gtx.bkt.clouddn.com/FjZG3mUciv4NVtyXkrJhQPd_z-S7)

这是一个通过 python 实现图片转字符画的小项目, 合适新手练手. 主要通过调用 PIL(Python Imaging Library) 模块实现对图片的操作. 

关于 PIL 的详细信息可以参考官方文档(http://effbot.org/imagingbook/).

![](http://po4tl1gtx.bkt.clouddn.com/Fq8SkapA9b3uTUkTmtXtS5P_N5D7)

### 实现思路

实现图片转字符画的关键就是用相同的字符替换相同的像素：
1. 将图像灰度化，遍历每个像素点;
3. 将每个像素点与字符进行对应;
2. 将字符串序列打印出来。

难点是建立像素值与灰度值间的映射关系(第五行):

```python
codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''#生成字符画所需的字符集
count = len(codeLib)
codePic = ''

codePic = codePic + codeLib[int(((count-1)*gray)/256)]
```

#### image灰度化有两种方式:
1. 直接使用内置的方法

```python
python_file = image_file("L".convert)
```

2. 加权平均法
根据重要性及其它指标，将三个分量以不同的权值进行加权平均。
由于人眼对绿色的敏感最高，对蓝色敏感最低，因此，按下式对RGB三分量进行加权平均能得到较合理的灰度图像

![](http://po4tl1gtx.bkt.clouddn.com/FlORf9bfqvbZ-_62T7rPGPRue2jE)

```python
gray = int(r* 0.299+g* 0.587+b* 0.114)
```

### 效果对比

两种灰度化的方式哪一个更好一些呢?

![](http://po4tl1gtx.bkt.clouddn.com/FtlbcDWs6Baw5ARycUOkSElfrp_z)

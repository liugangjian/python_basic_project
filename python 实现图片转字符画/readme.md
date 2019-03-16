这是一个通过 python 实现图片转字符画的小项目, 合适新手练手. 主要通过调用 PIL(Python Imaging Library) 模块实现对图片的操作. 

关于 PIL 的详细信息可以参考官方文档(http://effbot.org/imagingbook/).

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

映射关系不止这一种方式，补充几个小Tips:
1. 可以选取以字符集的长度为周期循环映射的方式

```python
codePic = codePic + codeLib[int(gray/count)]
```

2. 可调整像素范围，如多少像素以内可对应统一字符

<div class="output_wrapper" id="output_wrapper_id" style="font-size: 16px; color: rgb(86, 86, 86); line-height: 1.6; word-spacing: 0px; letter-spacing: 0px; font-family: 'Helvetica Neue', Helvetica, 'Hiragino Sans GB', 'Microsoft YaHei', Arial, sans-serif;"><p style="font-size: inherit; color: inherit; line-height: inherit; padding: 0px; margin: 1.5em 0px;"><span class="katex-display" style="display: block; text-align: center; color: inherit; line-height: inherit; margin: 0px; padding: 0px; font-size: 1.22em;"><span class="katex" style="font: 1.21em/1.2 KaTeX_Main, 'Times New Roman', serif; text-indent: 0px; text-rendering: auto; font-size: inherit; color: inherit; line-height: inherit; margin: 0px; white-space: nowrap; display: inline-block; text-align: center; padding: 3px;"><img src="http://po4tl1gtx.bkt.clouddn.com/FgHbXIQs5m5LU-5xlWeg6I_G8gUk" style="font-size: inherit; color: inherit; line-height: inherit; padding: 0px; margin: 0px auto; max-width: 100%; display: inline-block; vertical-align: middle;"></span></span></p></div>

其中, z表示字符集中字符数目; x表示当前灰度值; y表示取整后的常数. 

对应于我们代码中的映射规则，解的当z=25时，10 个像素差范围内的点都用同一个字符表示.


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

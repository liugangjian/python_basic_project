# -*- coding: utf-8 -*-
import cv2
import os
import time

show_heigth = 30              
show_width = 80

# 生成一个ascii字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
char_len = len(ascii_char)

# 加载一个视频
vc = cv2.VideoCapture(r"F:\python_workspace\badapple.3gp")  
        
# 判断是否正常打开
if vc.isOpened():                       
    rval , frame = vc.read()
else:
    rval = False
    
frame_count = 0
# 初始化输出列表
outputList = [] 
# 循环读取视频帧  
while rval:  
    # 使用opencv转化成灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    # resize灰度图
    gray = cv2.resize(gray,(show_width,show_heigth))
    text = ""
    for pixel_line in gray:
        for pixel in pixel_line:   
             # 字符串拼接                
            text += ascii_char[int(pixel / 256 * char_len )]
        text += "\n"                                
    outputList.append(text)a
    frame_count = frame_count + 1   
                        
    if frame_count % 100 == 0:
        print("已处理" + str(frame_count) + "帧")
    rval, frame = vc.read()  
print("处理完毕")

for frame in outputList:            
    print(frame)
    # 清屏
    os.system("cls")   

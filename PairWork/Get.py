import json
import requests
import base64

url = "http://47.102.118.1:8089/api/challenge/start/705a6347-01a2-4dd5-a919-bf3253b167cd"
data = {
    "teamid": 37,
    "token": "6098546f-f027-4a28-bacf-fda5805d21cf"
}
r = requests.post(url, json=data)
r.raise_for_status()
r.encoding = r.apparent_encoding
dic = json.loads(r.text)
img = base64.b64decode(dic["data"]["img"])
file = open('test\\1_.png', 'wb')
file.write(img)
file.close()
Step = dic["data"]["step"]
Swap = dic["data"]["swap"]
Uuid = dic['uuid']

import os
from PIL import Image


def splitImage(src, c_image):
    image_o = Image.open(src)
    dim = 3
    x = image_o.size[0] / dim
    y = image_o.size[1] / dim

    count = 0
    for j in range(dim):
        for i in range(dim):
            area = (i * x, j * y, i * x + x, j * y + y)
            image = image_o
            im = image.crop(area)
            c_image.append(im)

            count = count + 1


#  遍历图像集
def geturlPath():
    # 指定路径
    path = r'Picture Set/'
    # 返回指定路径的文件夹名称
    dirs = os.listdir(path)
    # 循环遍历该目录下的照片
    for dir in dirs:
        # 拼接字符串
        pa = path + dir
        # 判断是否为照片
        if not os.path.isdir(pa):
            # 使用生成器循环输出
            yield pa


c_image = []  # 原图切片后的顺序
c_image1 = []  # 题目切片后的顺序
src1 = 'test/1_.png'
splitImage(src1, c_image1)  # 题目保存地址

for item in geturlPath():  # geturlPath()是遍历图像集的函数
    flag = 0  # 用于记录匹配到的图片个数
    c_image2 = []
    splitImage(item, c_image2)
    for i in range(len(c_image1)):
        for j in range(len(c_image2)):
            if c_image1[i] == c_image2[j]:
                flag += 1
                break
    if flag == 8:  # 题目是随机扣了一张做空白格，因此有八张是一样的就是找到了原图
        print("找到了原图:" + item)
        c_image = c_image2
        break

# 匹配
map_1 = []  # 目标状态
map_2 = []  # 初始状态

for k in range(9):
    map_1.append(k + 1)

for i in range(len(c_image1)):
    temp = 0  # 用于辨别是否匹配到图片
    for j in range(len(c_image)):
        if c_image1[i] == c_image[j]:
            temp = 1
            map_2.append(j + 1)
    # 没有匹配到的就是被扣掉的那一块，置为0
    if temp == 0:
        map_2.append(0)

# 将原图中被扣掉的那一块的位置赋值为0
for i in range(len(map_1)):
    temp2 = 0
    for j in range(len(map_2)):
        if map_1[i] == map_2[j]:
            temp2 = 1
            break
    if temp2 == 0:
        map_1[i] = 0
        break

# 转换成二维列表
s = []  # 初始数码状态
e = []  # 目标数码状态
c = []
for i in range(len(map_1)):
    c.append(map_1[i])
    if (i + 1) % 3 == 0:
        e.append(c)
        c = []

c = []
for j in range(len(map_2)):
    c.append(map_2[j])
    if (j + 1) % 3 == 0:
        s.append(c)
        c = []

# print(s)
# print(e)
print("uuid:", Uuid)

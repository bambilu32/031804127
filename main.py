#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from functools import reduce
import jieba.analyse
from math import sqrt
import sys


class Similarity():
    def __init__(self, target1, target2, topK=10):
        self.target1 = target1
        self.target2 = target2
        self.topK = topK

    def vector(self):
        # 提取关键字和每个关键字的权重
        top_keywords1 = jieba.analyse.extract_tags(self.target1, topK=self.topK, withWeight=True)
        top_keywords2 = jieba.analyse.extract_tags(self.target2, topK=self.topK, withWeight=True)

        self.vdict1 = {}
        self.vdict2 = {}

        for k, v in top_keywords1:
            self.vdict1[k] = v

        for k, v in top_keywords2:
            self.vdict2[k] = v

    def mix(self):
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)

        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)

        def mapminmax(vdict):
            # 计算相对词频
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min

            for key in vdict:
                if _mid != 0:
                    vdict[key] = (vdict[key] - _min) / _mid
                else:
                    vdict[key] = 0  # 如果是空文本，则不计算相对词频，相对词频的值赋值为0

            return vdict

        self.vdict1 = mapminmax(self.vdict1)
        self.vdict2 = mapminmax(self.vdict2)

    def similar(self):
        self.vector()
        self.mix()

        sum = 0

        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]

        # 计算余弦相似度
        A = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict1.values())))
        B = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict2.values())))

        # 如果文本正常，则返回余弦相似度；如果有空文本，则返回0.0
        if A * B != 0:
            return sum / (A * B)
        else:
            return 0.0


# 命令行读入脚本名
pj = sys.argv[0]

# 命令行读入原本
file_name1 = sys.argv[1]
t1 = open(file_name1, 'r', encoding='UTF-8').read()

# 命令行读入抄袭文本
file_name2 = sys.argv[2]
t2 = open(file_name2, 'r', encoding='UTF-8').read()

# 命令行读入答案文本
file_name3 = sys.argv[3]

topK = 10  # 返回TF、IDF权重最大的关键字的个数，设为10

s = Similarity(t1, t2, topK)

result = s.similar()

file_result = open(file_name3, 'w+')
file_result.write(file_name2 + "相似度为" + str('%.2f' % result))

print(0)

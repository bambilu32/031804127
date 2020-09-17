from __future__ import division
from work.cs import Similarity

f1 = 'C:/tests/orig.txt'
t1 = open(f1, 'r', encoding='UTF-8').read()

f2 = 'C:/tests/orig_0.8_add.txt'
t2 = open(f2, 'r', encoding='UTF-8').read()

f3 = 'C:/tests/orig_0.8_del.txt'
t3 = open(f3, 'r', encoding='UTF-8').read()

f4 = 'C:/tests/orig_0.8_dis_1.txt'
t4 = open(f4, 'r', encoding='UTF-8').read()

f5 = 'C:/tests/orig_0.8_dis_3.txt'
t5 = open(f5, 'r', encoding='UTF-8').read()

f6 = 'C:/tests/orig_0.8_dis_7.txt'
t6 = open(f6, 'r', encoding='UTF-8').read()

f7 = 'C:/tests/orig_0.8_dis_10.txt'
t7 = open(f7, 'r', encoding='UTF-8').read()

f8 = 'C:/tests/orig_0.8_dis_15.txt'
t8 = open(f8, 'r', encoding='UTF-8').read()

f9 = 'C:/tests/orig_0.8_rep.txt'
t9 = open(f9, 'r', encoding='UTF-8').read()

f10 = 'C:/tests/orig_0.8_mix.txt'
t10 = open(f10, 'r', encoding='UTF-8').read()

f11 = 'C:/tests/data.txt'
t11 = open(f11, 'r', encoding='UTF-8').read()


s1 = Similarity(t1, t2, 10)
s2 = Similarity(t1, t3, 10)
s3 = Similarity(t1, t4, 10)
s4 = Similarity(t1, t5, 10)
s5 = Similarity(t1, t6, 10)
s6 = Similarity(t1, t7, 10)
s7 = Similarity(t1, t8, 10)
s8 = Similarity(t1, t9, 10)
s9 = Similarity(t1, t10, 10)
s10 = Similarity(t1, t11, 10)

result1 = s1.similar()
result2 = s2.similar()
result3 = s3.similar()
result4 = s4.similar()
result5 = s5.similar()
result6 = s6.similar()
result7 = s7.similar()
result8 = s8.similar()
result9 = s9.similar()
result10 = s10.similar()

print("orig_0.8_add:")
print(result1)

print("orig_0.8_del:")
print(result2)

print("orig_0.8_dis_1:")
print(result3)

print("orig_0.8_dis_3:")
print(result4)

print("orig_0.8_dis_7:")
print(result5)

print("orig_0.8_dis_10:")
print(result6)

print("orig_0.8_dis_15:")
print(result7)

print("orig_0.8_rep:")
print(result8)

print("orig_0.8_mix:")
print(result9)

print("data.txt:")
print(result10)
<span style='font-size:20px;'>**徽章**</span>

python



<span style='font-size:20px;'>**运行环境**</span>

Windows10

PyCharm2019.3.3



<span style='font-size:20px;'>**编译方法**</span>

python AI.py

python Post.py



<span style='font-size:20px;'>**使用方法**</span>

每次获取题目，修改Get.py中url的challenge-uuid部分。

AI.py直接import Get得到初始状态和目标状态，修改后Get.py的url链接后，直接运行AI.py解题。

最终结果是强制交换前的步骤＋强制交换后的步骤，输出是分两次，需要自己手动合并，自由交换的方块取输出的最后一次结果（因为之前的都是被判断无解的），如果没有输出自由交换的方块，就是没有执行自由交换，运行结果首行输出了提交题目的uuid。

提交题目


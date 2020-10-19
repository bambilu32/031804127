# coding=utf-8
from __future__ import print_function
import copy
import random
from jieba import xrange
from Get import Step, Swap, s, e, Uuid


def swap(arr):
    t = arr
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    k = random.randint(0, 2)
    v = random.randint(0, 2)
    temp = t[x][y]
    t[x][y] = t[k][v]
    t[k][v] = temp
    print("自由交换的方块为:", x * 3 + y + 1, k * 3 + v + 1)


def showMap(array2d):
    for x in xrange(0, 3):
        for y in xrange(0, 3):
            print(array2d[x][y], end='')
        print(" ")
    print("--------")
    return


def move(array2d, srcX, srcY, drcX, drcY):
    temp = array2d[srcX][srcY]
    array2d[srcX][srcY] = array2d[drcX][drcY]
    array2d[drcX][drcY] = temp
    return array2d


# 计算是奇数列还是偶数列
def getStatus(array2d):
    y = 0
    '''    for i in range(len(nums)):
        if (nums[i] != 0):
            for j in range(i):
                if (nums[j] > nums[i]):'''
    for i in range(len(array2d)):
        if array2d[i] != 0:
            for j in range(i):
                if array2d[j] > array2d[i]:
                    y += 1
    return y


# 根据奇数列和偶数列判断是否有解
def pd(start, end):
    startY = getStatus(start)
    endY = getStatus(end)
    # print(startY)
    # print(endY)
    if startY % 2 != endY % 2:
        return False
    else:
        return True


# 描述A算法中的节点数据
class Node:
    def __init__(self, array2d, g=0, h=0):
        self.array2d = array2d  # 二维数组
        self.father = None  # 父节点
        self.g = g  # g值
        self.h = h  # h值

    """
    估价公式
     """

    def setH(self, endNode):
        for x in xrange(0, 3):
            for y in xrange(0, 3):
                for m in xrange(0, 3):
                    for n in xrange(0, 3):
                        if self.array2d[x][y] == endNode.array2d[m][n]:
                            self.h += abs(x * y - m * n)

    def setG(self, g):
        self.g = g

    def setFather(self, node):
        self.father = node

    def getG(self):
        return self.g


class A:
    """
    A*算法
    """

    def __init__(self, startNode, endNode):
        """
        startNode:  寻路起点
        endNode:    寻路终点
        """
        global count
        # 开放列表
        self.openList = []
        # 封闭列表
        self.closeList = []
        # 起点
        self.startNode = startNode
        # 终点
        self.endNode = endNode
        # 当前处理的节点
        self.currentNode = startNode
        # 最后生成的路径
        self.pathlist = []
        # step步
        self.step = 0
        count = 0
        return

    def getMinFNode(self):
        """
        获得openlist中F值最小的节点
        """
        nodeTemp = self.openList[0]
        for node in self.openList:
            if node.g + node.h < nodeTemp.g + nodeTemp.h:
                nodeTemp = node
        return nodeTemp

    def nodeInOpenlist(self, node):
        for nodeTmp in self.openList:
            if nodeTmp.array2d == node.array2d:
                return True
        return False

    def nodeInCloselist(self, node):
        for nodeTmp in self.closeList:
            if nodeTmp.array2d == node.array2d:
                return True
        return False

    def endNodeInOpenList(self):
        for nodeTmp in self.openList:
            if nodeTmp.array2d == self.endNode.array2d:
                return True
        return False

    def getNodeFromOpenList(self, node):
        for nodeTmp in self.openList:
            if nodeTmp.array2d == node.array2d:
                return nodeTmp
        return None

    def searchOneNode(self, node):
        """
        搜索一个节点
        """
        # 忽略封闭列表
        if self.nodeInCloselist(node):
            return
            # G值计算
        gTemp = self.step

        # 如果不再openList中，就加入openlist
        if self.nodeInOpenlist(node) is False:
            node.setG(gTemp)
            # H值计算
            node.setH(self.endNode)
            self.openList.append(node)
            node.father = self.currentNode
        # 如果在openList中，判断currentNode到当前点的G是否更小
        # 如果更小，就重新计算g值，并且改变father
        else:
            nodeTmp = self.getNodeFromOpenList(node)
            if self.currentNode.g + gTemp < nodeTmp.g:
                nodeTmp.g = self.currentNode.g + gTemp
                nodeTmp.father = self.currentNode
        return

    def searchNear(self):
        """
        搜索下一个可以动作的数码
        找到0所在的位置并以此进行交换
        """
        flag = False
        for x in xrange(0, 3):
            for y in xrange(0, 3):
                if self.currentNode.array2d[x][y] == 0:
                    flag = True
                    break
            if flag is True:
                break

        self.step += 1
        if x - 1 >= 0:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x - 1, y)
            self.searchOneNode(Node(arrayTemp))
        if x + 1 < 3:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x + 1, y)
            self.searchOneNode(Node(arrayTemp))
        if y - 1 >= 0:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x, y - 1)
            self.searchOneNode(Node(arrayTemp))
        if y + 1 < 3:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x, y + 1)
            self.searchOneNode(Node(arrayTemp))

        return

    def start(self):
        """
        开始寻路
        """

        # 将初始节点加入开放列表
        self.startNode.setH(self.endNode)
        self.startNode.setG(self.step)
        self.openList.append(self.startNode)

        global key

        while True:
            # 获取当前开放列表里F值最小的节点
            # 并把它添加到封闭列表，从开发列表删除它
            self.currentNode = self.getMinFNode()
            self.closeList.append(self.currentNode)
            self.openList.remove(self.currentNode)
            self.step = self.currentNode.getG()
            self.searchNear()

            # 判断是否进行强制交换
            if key == 0 and self.step == Step + 1:
                nodeTmp = self.currentNode
                while True:
                    self.pathlist.append(nodeTmp)
                    if nodeTmp.father is not None:
                        nodeTmp = nodeTmp.father
                    else:
                        key = 1
                        return True

            # 检验是否结束
            if self.endNodeInOpenList():
                nodeTmp = self.getNodeFromOpenList(self.endNode)
                while True:
                    self.pathlist.append(nodeTmp)
                    if nodeTmp.father is not None:
                        nodeTmp = nodeTmp.father
                    else:
                        return True

            elif len(self.openList) == 0:
                return False

        return True

    def showPath(self):
        global result
        for node in self.pathlist[::-1]:
            # showMap(node.array2d)
            result.append(node.array2d)


ct = 0
key = 0
result = []
sp = Swap
a = A(Node(s), Node(e))
print("A start:")
# 开始寻路
if a.start():
    a.showPath()

# 输出强制交换前的步骤
print("强制交换前的步骤为：")
for i in range(len(result) - 1):
    od = sum(result[i], [])
    ne = sum(result[i + 1], [])
    if ne.index(0) - od.index(0) == -3:
        print('w', end='')
    if ne.index(0) - od.index(0) == 3:
        print('s', end='')
    if ne.index(0) - od.index(0) == -1:
        print('a', end='')
    if ne.index(0) - od.index(0) == 1:
        print('d', end='')
print("\n")
if key == 1:
    ls_1 = copy.deepcopy(result[-1])
    # print("强制交换前", result[-1])

    # 执行强制调换
    if 1 <= sp[0] <= 3:
        m = 0
        n = sp[0] - 1
    if 4 <= sp[0] <= 6:
        m = 1
        n = sp[0] - 4
    if 7 <= sp[0] <= 9:
        m = 2
        n = sp[0] - 7
    if 1 <= sp[1] <= 3:
        p = 0
        q = sp[1] - 1
    if 4 <= sp[1] <= 6:
        p = 1
        q = sp[1] - 4
    if 7 <= sp[1] <= 9:
        p = 2
        q = sp[1] - 7
    temp = ls_1[m][n]
    ls_1[m][n] = ls_1[p][q]
    ls_1[p][q] = temp
    result.append(ls_1)
    # print("强制交换后", result[-1])

    # 判断是否有解
    ls_2 = copy.deepcopy(ls_1)
    ls_3 = copy.deepcopy(ls_1)
    while pd(ls_2, e) is False:
        ct = 1
        ls_2 = copy.deepcopy(ls_3)
        # 进行自由交换
        swap(ls_2)

    # 将自由交换后的状态存入结果列表
    if ct == 1:
        result.append(ls_2)
    print("自由交换后", result[-1])

    wb = len(result)

    # 构建b
    b = A(Node(ls_2), Node(e))

    # 开始寻路
    if b.start():
        b.showPath()

    print("强制交换后的步骤为：")
    for i in range(wb - 1, len(result) - 1):
        od = sum(result[i], [])
        ne = sum(result[i + 1], [])
        if ne.index(0) - od.index(0) == -3:
            print('w', end='')
        if ne.index(0) - od.index(0) == 3:
            print('s', end='')
        if ne.index(0) - od.index(0) == -1:
            print('a', end='')
        if ne.index(0) - od.index(0) == 1:
            print('d', end='')

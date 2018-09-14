# -*- coding: utf-8 -*-
"""
Created on 2018/9/12 16:18

@author: vincent
"""
# 这个问题原始是用来实现一个可变长度的编码问题，但可以总结成这样一个问题，假设我们有很多的叶子节点，
# 每个节点都有一个权值w(可以是任何有意义的数值，比如它出现的概率)，我们要用这些叶子节点构造一棵树，
# 那么每个叶子节点就有一个深度d，我们的目标是使得所有叶子节点的权值与深度的乘积之和$$\Sigma w{i}d{i}$$最小。
#
# 很自然的一个想法就是，对于权值大的叶子节点我们让它的深度小些(更加靠近根节点)，权值小的让它的深度相对大些，
# 这样的话我们自然就会想着每次取当前权值最小的两个节点将它们组合出一个父节点，一直这样组合下去直到只有一个节点即根节点为止。

from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))            # num ensures valid ordering
    heapify(trees)                              # A min-heap based on freq
    print(trees)
    while len(trees) > 1:                       # Until all are combined
        fa, _, a = heappop(trees)               # Get the two smallest trees
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a, b]))     # Combine and re-add them
        print(trees)
    # print trees
    return trees[0][-1]

seq = "abcdefghi"
frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
print(huffman(seq, frq))
# [['i', [['a', 'b'], 'e']], [['f', 'g'], [['c', 'd'], 'h']]]
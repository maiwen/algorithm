# -*- coding: utf-8 -*-
"""
Created on 2018/9/12 11:15

@author: vincent
"""

# 邻接表
# Adjacency Lists

def graph_list():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c, d, e, f],  # a
        [c, e],  # b
        [d],  # c
        [e],  # d
        [f],  # e
        [c, g, h],  # f
        [f, h],  # g
        [f, g]  # h
    ]
    return N


a, b, c, d, e, f, g, h = range(8)
N = [
    [b, c, d, e, f],  # a
    [c, e],  # b
    [d],  # c
    [e],  # d
    [f],  # e
    [c, g, h],  # f
    [f, h],  # g
    [f, g]  # h
]
b in N[a]
len(N[f])

def graph_set():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b, c, d, e, f},  # a
        {c, e},  # b
        {d},  # c
        {e},  # d
        {f},  # e
        {c, g, h},  # f
        {f, h},  # g
        {f, g}  # h
    ]
    return N
# Adjacency Sets
# A Straightforward Adjacency Set Representation
a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},    # a
    {c, e},             # b
    {d},                # c
    {e},                # d
    {f},                # e
    {c, g, h},          # f
    {f, h},             # g
    {f, g}              # h
]

b in N[a] # Neighborhood membership -> True
len(N[f]) # Degree -> 3
# 对于list，判断一个元素是否存在是线性时间O(N(v))，而在set中是常数时间O(1)，所以对于稠密图使用adjacency sets要更加高效。

# adjacency dicts 表示形式，这种情况下如果边是带权值的都没有问题！

# A Straightforward Adjacency Dict Representation
a, b, c, d, e, f, g, h = range(8)
N = [
    {b:2, c:1, d:3, e:9, f:4},    # a
    {c:4, e:3},                   # b
    {d:8},                        # c
    {e:7},                        # d
    {f:5},                        # e
    {c:2, g:2, h:2},              # f
    {f:1, h:6},                   # g
    {f:9, g:8}                    # h
]

b in N[a] # Neighborhood membership -> True
len(N[f]) # Degree -> 3
N[a][b] # Edge weight for (a, b) -> 2

# 邻接矩阵 Adjacency Matrix

# 使用嵌套的list，用1和0表示点和点之间的连接关系，此时点之间的连接性判断时间是常数，但是对于度的计算时间是线性的
# An Adjacency Matrix, Implemented with Nested Lists
a, b, c, d, e, f, g, h = range(8)
N = [[0,1,1,1,1,1,0,0], # a
     [0,0,1,0,1,0,0,0], # b
     [0,0,0,1,0,0,0,0], # c
     [0,0,0,0,1,0,0,0], # d
     [0,0,0,0,0,1,0,0], # e
     [0,0,1,0,0,0,1,1], # f
     [0,0,0,0,0,1,0,1], # g
     [0,0,0,0,0,1,1,0]] # h

N[a][b] # Neighborhood membership -> 1
sum(N[f]) # Degree -> 3

# 如果边带有权值，也可以使用权值代替1，用inf代替0
a, b, c, d, e, f, g, h = range(8)
_ = float('inf')

W = [[0,2,1,3,9,4,_,_], # a
     [_,0,4,_,3,_,_,_], # b
     [_,_,0,8,_,_,_,_], # c
     [_,_,_,0,7,_,_,_], # d
     [_,_,_,_,0,5,_,_], # e
     [_,_,2,_,_,0,2,2], # f
     [_,_,_,_,_,1,0,6], # g
     [_,_,_,_,_,9,8,0]] # h

W[a][b] < _ # Neighborhood membership
sum(1 for w in W[a] if w < _) - 1  # Degree
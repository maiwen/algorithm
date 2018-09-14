# -*- coding: utf-8 -*-
"""
Created on 2018/9/12 11:42

@author: vincent
"""
# 图的连通分量是图的一个最大子图，在这个子图中任何两个节点之间都是相互可达的(忽略边的方向)。
from algorithms.graph import graph
def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P

# 来测试下，得到的结果没有问题
G = graph.graph_set()
print(list(walk(G, 0)))

# 上面的walk函数只适用于无向图，而且只能找到一个从参数s出发的连通分量，要想得到全部的连通分量需要修改下
def components(G):                              # The connected components
    comp = []
    seen = set()                                # Nodes we've already seen
    for u in G:                                 # Try every starting point
        if u in seen: continue                  # Seen? Ignore it
        C = walk(G, u)                          # Traverse component
        seen.update(C)                          # Add keys of C to seen
        comp.append(C)                          # Collect the components
    return comp

G = {
    0: set([1, 2]),
    1: set([0, 2]),
    2: set([0, 1]),
    3: set([4, 5]),
    4: set([3, 5]),
    5: set([3, 4])
    }
print([list(sorted(C)) for C in components(G)])  #[[0, 1, 2], [3, 4, 5]]

# 上面的迷宫实际上就是为了引出深度优先搜索(DFS)，每次到了一个交叉口的时候，可能我们可以向左走，也可以向右走，选择是有不少，
# 但是我们要向一直走下去的话就只能选择其中的一个方向，如果我们发现这个方向走不出去的话，我们就回溯回来，选择一个刚才没选过的方向继续尝试下去。
# 基于上面的想法可以写出下面递归版本的DFS

def dfs(G, s, S=None):
    if not S:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        dfs(G, u, S)
    return S

G = graph.graph_set()
print(list(dfs(G, 0)))

def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u
G = graph.graph_set()
print(list(iter_dfs(G, 0)))

# 加上时间戳的DFS遍历
def dfs(G, s, d, f, S=None, t=0):
    if S is None: S = set()                     # Initialize the history
    d[s] = t; t += 1                            # Set discover time
    S.add(s)                                    # We've visited s
    for u in G[s]:                              # Explore neighbors
        if u in S: continue                     # Already visited. Skip
        t = dfs(G, u, d, f, S, t)               # Recurse; update timestamp
    f[s] = t; t += 1                            # Set finish time
    return t                                    # Return timestamp

# 除了给节点加上时间戳之外，算法导论在介绍DFS的时候还给节点进行着色，在节点被发现之前是白色的，
# 在发现之后先是灰色的，在结束访问之后才是黑色的，详细的流程可以参考上面给出的算法导论中的那幅DFS示例图。
# 有了颜色有什么用呢？作用大着呢！根据节点的颜色，我们可以对边进行分类！大致可以分为下面四种：使
# 用DFS对图进行遍历时，对于每条边(u,v)，当该边第一次被发现时，根据到达节点 v 的颜色来对边进行分类(正向边和交叉边不做细分)：
# (1)白色表示该边是一条树边；
# (2)灰色表示该边是一条反向边；
# (3)黑色表示该边是一条正向边或者交叉边。
# 那对边进行分类有什么作用呢？作用多着呢！
# 最常见的作用的是判断一个有向图是否存在环，如果对有向图进行DFS遍历发现了反向边，那么一定存在环，反之没有环。
# 此外，对于无向图，如果对它进行DFS遍历，肯定不会出现正向边或者交叉边。
# 那对节点标注时间戳有什么用呢？其实，除了可以发现上面提到的那些很重要的性质之外，时间戳对于接下来要介绍的拓扑排序的另一种解法和强连通分量很重要！
# 如果我们按照节点的f[v]降序排列，我们就得到了我们想要的拓扑排序了！
# 这就是拓扑排序的另一个解法！[在算法导论中该解法是主要介绍的解法，而我们前面提到的那个解法是在算法导论的习题中出现的]

#Topological Sorting Based on Depth-First Search
def dfs_topsort(G):
    S, res = set(), []                          # History and result
    def recurse(u):                             # Traversal subroutine
        if u in S: return                       # Ignore visited nodes
        S.add(u)                                # Otherwise: Add to history
        for v in G[u]:
            recurse(v)                          # Recurse through neighbors
        res.append(u)                           # Finished with u: Append it
    for u in G:
        recurse(u)                              # Cover entire graph
    res.reverse()                               # It's all backward so far
    return res

G = {'a': set('bf'), 'b': set('cdf'), 'c': set('d'), 'd': set('ef'), 'e': set('f'), 'f': set()}
print(dfs_topsort(G))

# BFS的代码很好实现，主要是使用队列
#Breadth-First Search
from collections import deque

def bfs(G, s):
    P, Q = {s: None}, deque([s])                # Parents and FIFO queue
    while Q:
        u = Q.popleft()                         # Constant-time for deque
        for v in G[u]:
            if v in P: continue                 # Already has parent
            P[v] = u                            # Reached from u: u is parent
            Q.append(v)
    return P

G = graph.graph_set()
print(list(bfs(G, 0)))

# Python的list可以很好地充当stack，但是充当queue则性能很差，函数bfs中使用的是collections模块中的deque，
# 即双端队列(double-ended queue)，它一般是使用链表来实现的，这个类有extend、append和pop等方法都是作用于队列右端的，
# 而方法extendleft、appendleft和popleft等方法都是作用于队列左端的，它的内部实现是非常高效的。


# 强连通分支算法的流程有下面四步：
#
# 1.对原图G运行DFS，得到每个节点的完成时间f[v]；
#
# 2.得到原图的转置图GT；
#
# 3.对GT运行DFS，主循环按照节点的f[v]降序进行访问；
#
# 4.输出深度优先森林中的每棵树，也就是一个强连通分支。
#
# 根据上面的思路可以得到下面的强连通分支算法实现，其中的函数parse_graph是作者用来方便构造图的函数

def tr(G):                                      # Transpose (rev. edges of) G
    GT = {}
    for u in G: GT[u] = set()                   # Get all the nodes in there
    for u in G:
        for v in G[u]:
            GT[v].add(u)                        # Add all reverse edges
    return GT

def scc(G):
    GT = tr(G)                                  # Get the transposed graph
    sccs, seen = [], set()
    for u in dfs_topsort(G):                    # DFS starting points
        if u in seen: continue                  # Ignore covered nodes
        C = walk(GT, u, seen)                   # Don't go "backward" (seen)
        seen.update(C)                          # We've now seen C
        sccs.append(C)                          # Another SCC found
    return sccs

from string import ascii_lowercase
def parse_graph(s):
    # print zip(ascii_lowercase, s.split("/"))
    # [('a', 'bc'), ('b', 'die'), ('c', 'd'), ('d', 'ah'), ('e', 'f'), ('f', 'g'), ('g', 'eh'), ('h', 'i'), ('i', 'h')]
    G = {}
    for u, line in zip(ascii_lowercase, s.split("/")):
        G[u] = set(line)
    return G

G = parse_graph('bc/die/d/ah/f/g/eh/i/h')
print(list(map(list, scc(G))))
#[['a', 'c', 'b', 'd'], ['e', 'g', 'f'], ['i', 'h']]


# -*- coding: utf-8 -*-
"""
Created on 2018/9/13 15:21

@author: vincent
"""

# 连通无向图G的生成树是指包含它所有顶点但是部分边的子图，假设每条边都有一个权值，那么权值之和最小的生成树就是最小生成树，
# 它不一定是唯一的。如果图G是非连通的，那么它就没有生成树。
#
# 前面我们在介绍遍历的时候也得到过生成树，那里我们是一个顶点一个顶点进行遍历，下面我们通过每次添加一条边来得到最小生成树，
# 而且每次我们贪心地选择剩下的边中权值最小的那条边，但是要保证不能形成环！
#
# 那怎么判断是否会出现环呢？
#
# 假设我们要考虑是否添加边(u,v)，一个最直接的想法就是遍历已生成的树，看是否能够从 u 到 v，如果能，那么就舍弃这条边继续考虑后面的边，
# 否则就添加这条边。很显然，采用遍历的方式太费时了。
#
# 再假设我们用一个集合来保存我们已经生成的树中的节点，如果我们要考虑是否添加边(u,v)，那么我们就看下集合中这两个节点是否都存在，
# 如果都存在的话说明这条边加进来的话会形成环。这么做可以在常数时间内确定是否会形成环，但是…它是错误的！除非我们每次添加一条边之后得到的局部解一直都只有一棵树才对，如果之前加入的节点 u 和节点 v 在不同的分支上的话，上面的判断不能确定添加这条边之后会形成环！[后面的Prim算法采用的策略就能保证局部解一直都是一棵树]
#
# 下面我们可以试着让每个加入的节点都知道自己处在哪个分支上，而且我们可以用分支中的某一个节点作为该分支的“代表”，
# 该分支中的所有节点都指向这个“代表”，显然我们接下来会遇到分支合并的问题。如果两个分支因为某条边的加入而连通了，
# 那么它们就要合并了，那怎么合并呢？我们让两个分支中的所有节点都指向同一个“代表”就行了，但是这是一个线性时间的操作，
# 我们可以做得更快！假设我们改变下策略，让每个节点指向另一个节点(这个节点不一定是分支的“代表”)，如果我们顺着指向链一直找，
# 就肯定能找到“代表”，因为“代表”是自己指向自己的。
# 这样的话，如果两个分支要合并，只需要让其中的一个分支的“代表”指向另一个分支的“代表”就行啦！这就是一个常数时间的操作。
#A Naïve Implementation of Kruskal’s Algorithm
def naive_find(C, u):                           # Find component rep.
    while C[u] != u:                            # Rep. would point to itself
        u = C[u]
    return u

def naive_union(C, u, v):
    u = naive_find(C, u)                        # Find both reps
    v = naive_find(C, v)
    C[u] = v                                    # Make one refer to the other

def naive_kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G[u]]
    T = set()                                   # Empty partial solution
    C = {u:u for u in G}                        # Component reps
    print(C)
    for _, u, v in sorted(E):                   # Edges, sorted by weight
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))                       # Different reps? Use it!
            naive_union(C, u, v)                # Combine components
    return T

G = {
    0: {1:1, 2:3, 3:4},
    1: {2:5},
    2: {3:2},
    3: set()
    }
print(list(naive_kruskal(G)))#[(0, 1), (2, 3), (0, 2)]

# 从上面的分析我们可以看到，虽然合并时修改指向的操作是常数时间的，但是通过指向链的方式找到“代表”所花的时间是线性的，而这里还可以做些改进。
#
# 首先，在合并(union)的时候我们让“小”分支指向“大”分支，这样平衡了之后平均查找时间肯定有所下降，那么怎么确定分支的“大小”呢？
# 这个可以用平衡树的方式来思考，假设我们给每个节点都设置一个权重(rank or weight)，其实重要的还是“代表”的权重，
# 如果要合并的两个分支的“代表”的权重相等的话，在将“小”分支指向“大”分支之后，还要将“大”分支的权重加1。
#
# 其次，在查找(find)的时候我们一边查找一边修正经过的点的指向，让它直接指向“代表”，这个怎么做到呢？使用递归就行了，因为递归在找到了之后会回溯，
# 回溯的时候就可以设置其他节点的“代表”了，这个叫做path compression技术，是Kruskal算法常用的一个技巧。
#
# 基于上面的改进就有了下面优化的Kruskal算法

#Kruskal’s Algorithm
def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])                    # Path compression
    return C[u]

def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:                             # Union by rank
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:                            # A tie: Move v up a level
        R[v] += 1

def kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G[u]]
    T = set()
    C, R = {u:u for u in G}, {u:0 for u in G}   # Comp. reps and ranks
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T

G = {
    0: {1:1, 2:3, 3:4},
    1: {2:5},
    2: {3:2},
    3: set()
    }
print(list(kruskal(G))) #[(0, 1), (2, 3), (0, 2)]

# 接下来就是Prim算法了，它其实就是我们前面介绍的traversal算法中的一种，不同点是它对待办事项(to-do list，即前面提到的“边缘节点”，
# 也就是我们已经包含的这些节点能够直接到达的那些节点)进行了一定的排序，我们在实现BFS时使用的是双端队列deque，
# 此时我们只要把它改成一个优先队列(priority queue)就行了，这里选用heapq模块中的堆heap。
#
# Prim算法不断地添加新的边(也可以说是一个新的顶点)，一旦我们加入了一条新的边，可能会导致某些原来的边缘节点到生成树的距离更加近了，
# 所以我们要更新一下它们的距离值，然后重新调整下排序，那怎么修改距离值呢？我们可以先找到原来的那个节点，然后再修改它的距离值接着重新调整堆，
# 但是这么做实在是太麻烦了！这里有一个巧妙的技巧就是直接向堆中插入新的距离值的节点！为什么可以呢？因为插入的新节点B的距离值比原来的节点A的距离值小，
# 那么Prim算法添加顶点的时候肯定是先弹出堆中的节点B，后面如果弹出节点A的话，因为这个节点已经添加进入了，直接忽略就行了，也就是说我们这么做不仅很简单，
# 而且并没有把原来的问题搞砸了。

from heapq import heappop, heappush

def prim(G, s):
    P, Q = {}, [(0, None, s)]
    while Q:
        _, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        for v, w in G[u].items():
            heappush(Q, (w, u, v)) #weight, predecessor node, node
    return P

G = {
    0: {1:1, 2:3, 3:4},
    1: {0:1, 2:5},
    2: {0:3, 1:5, 3:2},
    3: {2:2, 0:4}
    }
print(prim(G, 0)) # {0: None, 1: 0, 2: 0, 3: 2}
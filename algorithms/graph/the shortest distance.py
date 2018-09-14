# -*- coding: utf-8 -*-
"""
Created on 2018/9/14 15:08

@author: vincent
"""
# 首先我们来实现下之前学过的松弛技术relaxtion，代码中D保存各个节点到源点的距离值估计(上界值)，
# P保存节点的最短路径上的前驱节点，W保存边的权值，其中不存在的边的权值为inf。
# 松弛就是说，假设节点 u 和节点 v 事先都有一个最短距离的估计(例如测试代码中的7和13)，如果现在要松弛边(u,v)，
# 也就是对从节点 u 通过边(u,v)到达节点 v，将这条路径得到节点 v 的距离估计值(7+3=10)和原来的节点 v 的距离估计值(13)进行比较，
# 如果前者更小的话，就表示我们可以放弃在这之前确定的从源点到节点 v 的最短路径，改成从源点到节点 u，
# 然后节点 u 再到节点 v，这条路线距离会更短些，这也就是发生了一次松弛！(测试代码中10<13，所以要进行松弛，此时D[v]变成10，而它的前驱节点也变成了 u)

#relaxtion
inf = float('inf')
def relax(W, u, v, D, P):
    d = D.get(u,inf) + W[u][v]                  # Possible shortcut estimate
    if d < D.get(v,inf):                        # Is it really a shortcut?
        D[v], P[v] = d, u                       # Update estimate and parent
        return True                             # There was a change!

#测试代码
u = 0; v = 1
D, W, P = {}, {u:{v:3}}, {}
D[u] = 7
D[v] = 13
print(D[u]) # 7
print (D[v]) # 13
print (W[u][v]) # 3
relax(W, u, v, D, P) # True
print (D[v]) # 10
D[v] = 8
relax(W, u, v, D, P)
print (D[v]) # 8


#Bellman-Ford算法
def bellman_ford(G, s):
    D, P = {s:0}, {}                            # Zero-dist to s; no parents
    for rnd in G:                               # n = len(G) rounds
        changed = False                         # No changes in round so far
        for u in G:                             # For every from-node...
            for v in G[u]:                      # ... and its to-nodes...
                if relax(G, u, v, D, P):        # Shortcut to v from u?
                    changed = True              # Yes! So something changed
        if not changed: break                   # No change in round: Done
    else:                                       # Not done before round n?
        raise ValueError('negative cycle')      # Negative cycle detected
    return D, P                                 # Otherwise: D and P correct

#测试代码
s, t, x, y, z = range(5)
W = {
    s: {t:6, y:7},
    t: {x:5, y:8, z:-4},
    x: {t:-2},
    y: {x:-3, z:9},
    z: {s:2, x:7}
    }
D, P = bellman_ford(W, s)
print ([D[v] for v in [s, t, x, y, z]]) # [0, 2, 4, 7, -2]
print (s not in P) # True
print ([P[v] for v in [t, x, y, z]] == [x, y, s, t]) # True
W[s][t] = -100
print (bellman_ford(W, s))
# Traceback (most recent call last):
#         ...
# ValueError: negative cycle


#Dijkstra算法
from heapq import heappush, heappop

def dijkstra(G, s):
    D, P, Q, S = {s:0}, {}, [(0,s)], set()      # Est., tree, queue, visited
    while Q:                                    # Still unprocessed nodes?
        _, u = heappop(Q)                       # Node with lowest estimate
        if u in S: continue                     # Already visited? Skip it
        S.add(u)                                # We've visited it now
        for v in G[u]:                          # Go through all its neighbors
            relax(G, u, v, D, P)                # Relax the out-edge
            heappush(Q, (D[v], v))              # Add to queue, w/est. as pri
    return D, P                                 # Final D and P returned

#测试代码
s, t, x, y, z = range(5)
W = {
    s: {t:10, y:5},
    t: {x:1, y:2},
    x: {z:4},
    y: {t:3, x:9, z:2},
    z: {x:6, s:7}
    }
D, P = dijkstra(W, s)
print ([D[v] for v in [s, t, x, y, z]]) # [0, 8, 9, 5, 7]
print (s not in P) # True
print ([P[v] for v in [t, x, y, z]] == [y, t, s, y]) # True

from copy import deepcopy
#Johnson’s Algorithm
def johnson(G):                                 # All pairs shortest paths

    G = deepcopy(G)                             # Don't want to break original
    s = object()                                # Guaranteed unique node
    G[s] = {v:0 for v in G}                     # Edges from s have zero wgt
    h, _ = bellman_ford(G, s)                   # h[v]: Shortest dist from s
    del G[s]                                    # No more need for s
    for u in G:                                 # The weight from u...
        for v in G[u]:                          # ... to v...
            G[u][v] += h[u] - h[v]              # ... is adjusted (nonneg.)
    D, P = {}, {}                               # D[u][v] and P[u][v]
    for u in G:                                 # From every u...
        D[u], P[u] = dijkstra(G, u)             # ... find the shortest paths
        for v in G:                             # For each destination...
            D[u][v] += h[v] - h[u]              # ... readjust the distance
    return D, P                                 # These are two-dimensional

a, b, c, d, e = range(5)
W = {
    a: {c:1, d:7},
    b: {a:4},
    c: {b:-5, e:2},
    d: {c:6},
    e: {a:3, b:8, d:-4}
    }
D, P = johnson(W)
print ([D[a][v] for v in [a, b, c, d, e]]) # [0, -4, 1, -1, 3]
print ([D[b][v] for v in [a, b, c, d, e]]) # [4, 0, 5, 3, 7]
print ([D[c][v] for v in [a, b, c, d, e]]) # [-1, -5, 0, -2, 2]
print ([D[d][v] for v in [a, b, c, d, e]]) # [5, 1, 6, 0, 8]
print ([D[e][v] for v in [a, b, c, d, e]]) # [1, -3, 2, -4, 0]

#递归版本的Floyd-Warshall算法
from functools import wraps

def memo(func):
    cache = {}                                  # Stored subproblem solutions
    @wraps(func)                                # Make wrap look like func
    def wrap(*args):                            # The memoized wrapper
        if args not in cache:                   # Not already computed?
            cache[args] = func(*args)           # Compute & cache the solution
        return cache[args]                      # Return the cached solution
    return wrap                                 # Return the wrapper

def rec_floyd_warshall(G):                                # All shortest paths
    @memo                                                 # Store subsolutions
    def d(u,v,k):                                         # u to v via 1..k
        if k==0: return G[u][v]                           # Assumes v in G[u]
        return min(d(u,v,k-1), d(u,k,k-1) + d(k,v,k-1))   # Use k or not?
    return {(u,v): d(u,v,len(G)) for u in G for v in G}   # D[u,v] = d(u,v,n)

#测试代码
a, b, c, d, e = range(1,6) # One-based
W = {
    a: {c:1, d:7},
    b: {a:4},
    c: {b:-5, e:2},
    d: {c:6},
    e: {a:3, b:8, d:-4}
    }
for u in W:
    for v in W:
        if u == v: W[u][v] = 0
        if v not in W[u]: W[u][v] = inf
D = rec_floyd_warshall(W)
print ([D[a,v] for v in [a, b, c, d, e]]) # [0, -4, 1, -1, 3]
print ([D[b,v] for v in [a, b, c, d, e]]) # [4, 0, 5, 3, 7]
print ([D[c,v] for v in [a, b, c, d, e]]) # [-1, -5, 0, -2, 2]
print ([D[d,v] for v in [a, b, c, d, e]]) # [5, 1, 6, 0, 8]
print ([D[e,v] for v in [a, b, c, d, e]]) # [1, -3, 2, -4, 0]

#空间优化后的Floyd-Warshall算法
def floyd_warshall1(G):
    D = deepcopy(G)                             # No intermediates yet
    for k in G:                                 # Look for shortcuts with k
        for u in G:
            for v in G:
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])
    return D

#测试代码
a, b, c, d, e = range(1,6) # One-based
W = {
    a: {c:1, d:7},
    b: {a:4},
    c: {b:-5, e:2},
    d: {c:6},
    e: {a:3, b:8, d:-4}
    }
for u in W:
    for v in W:
        if u == v: W[u][v] = 0
        if v not in W[u]: W[u][v] = inf
D = floyd_warshall1(W)
print ([D[a][v] for v in [a, b, c, d, e]]) # [0, -4, 1, -1, 3]
print ([D[b][v] for v in [a, b, c, d, e]]) # [4, 0, 5, 3, 7]
print ([D[c][v] for v in [a, b, c, d, e]]) # [-1, -5, 0, -2, 2]
print ([D[d][v] for v in [a, b, c, d, e]]) # [5, 1, 6, 0, 8]
print ([D[e][v] for v in [a, b, c, d, e]]) # [1, -3, 2, -4, 0]

# 当然啦，一般情况下求最短路径问题我们还需要知道最短路径是什么，这个时候我们只需要在进行选择的时候设置一个前驱节点就行了

#最终版本的Floyd-Warshall算法
def floyd_warshall(G):
    D, P = deepcopy(G), {}
    for u in G:
        for v in G:
            if u == v or G[u][v] == inf:
                P[u,v] = None
            else:
                P[u,v] = u
    for k in G:
        for u in G:
            for v in G:
                shortcut = D[u][k] + D[k][v]
                if shortcut < D[u][v]:
                    D[u][v] = shortcut
                    P[u,v] = P[k,v]
    return D, P

#测试代码
a, b, c, d, e = range(5)
W = {
    a: {c:1, d:7},
    b: {a:4},
    c: {b:-5, e:2},
    d: {c:6},
    e: {a:3, b:8, d:-4}
    }
for u in W:
    for v in W:
        if u == v: W[u][v] = 0
        if v not in W[u]: W[u][v] = inf
D, P = floyd_warshall(W)
print ([D[a][v] for v in [a, b, c, d, e]])#[0, -4, 1, -1, 3]
print ([D[b][v] for v in [a, b, c, d, e]])#[4, 0, 5, 3, 7]
print ([D[c][v] for v in [a, b, c, d, e]])#[-1, -5, 0, -2, 2]
print ([D[d][v] for v in [a, b, c, d, e]])#[5, 1, 6, 0, 8]
print ([D[e][v] for v in [a, b, c, d, e]])#[1, -3, 2, -4, 0]
print ([P[a,v] for v in [a, b, c, d, e]])#[None, 2, 0, 4, 2]
print ([P[b,v] for v in [a, b, c, d, e]])#[1, None, 0, 4, 2]
print ([P[c,v] for v in [a, b, c, d, e]])#[1, 2, None, 4, 2]
print ([P[d,v] for v in [a, b, c, d, e]])#[1, 2, 3, None, 2]
print ([P[e,v] for v in [a, b, c, d, e]])#[1, 2, 3, 4, None]
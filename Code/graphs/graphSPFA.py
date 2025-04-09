import random
import sys

def generate(nNodes, nEdges, maxVal):
    n = random.randint(1, nNodes)
    m = random.randint(1, nEdges)
    m = max(m, n * (n - 1) // 2)
    
    d[1] = 0
    for i in range(2, n + 1):
        u = i
        l = max(i - 5, 1)
        r = i - 1
        v = random.randint(l, r)
        d[u] = d[v] + 1
        t = random.randint(1, maxVal)  
        s.add((u, v))
        s.add((v, u))
        print(u, v, t)
    
    for i in range(1, m - (n - 1) + 1):
        u = random.randint(1, n)
        v = random.randint(1, n)
        if (u, v) in s or u == v:
            i -= 1
            continue
        s.add((u, v))
        s.add((v, u))
        l = abs(d[u] - d[v])
        r = l + 5
        t = random.randint(l, r)
        print(u, v, t)

# 调用函数生成数据
generate()
#最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#最大公約数の個数
def ngcd(a):
    res = a[0]
    for i in range(len(a)):
        if res != 1:
            res = gcd(a[i], res)
    return res

#最小公倍数
def lcm(a,b):
    return a * b // gcd(a, b)

#最小公倍数の個数
def nlcm(a):
    res = a[0]
    for i in range(len(a)):
        res = lcm(res, a[i])
    return res


#素数判定
def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(pow(n, 0.5)) + 1):
        if n % k == 0:
            return False
    return True

# 約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

# 因数分解
def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n != 1:
        res.append([n, 1])
    prime = []
    for p in res:
        for _ in range(p[1]):
            prime.append(p[0])
    return prime

# 桁和
def digit_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

# 幅優先探索
from collections import deque

h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
grid = [input() for _ in range(h)]

f_inf = float('inf')
maze = [[f_inf] * w for _ in range(h)]
maze[sy - 1][sx - 1] = 0
que = deque([[sy - 1, sx - 1]])
while que:
    y, x = que.popleft()
    for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        next_y, next_x = y + i, x + j
        if grid[next_y][next_x] != "#":
            if maze[next_y][next_x] > maze[y][x] + 1:
                maze[next_y][next_x] = maze[y][x] + 1
                que.append([next_y, next_x])

print(maze[gy - 1][gx - 1])

#bit全探索
for i in range(2 ** n):
    for j in range(n):
        if (i >> j) & 1:
            #ここで何らかの処理

#グラフの作成
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

# Union Find
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 親が同じか判別
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # 経路圧縮
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 根を繋ぎ直す
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 親が同じか判別
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 連結成分の大きさを返す
    def size(self, x):
        return -self.parents[self.find(x)]

# ランレングス圧縮
def rle(s):
    tmp, count, ans = s[0], 1, ""
    for i in range(1, len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans += tmp + str(count)
            tmp = s[i]
            count = 1
    ans += tmp + str(count)
    return ans
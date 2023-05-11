# 1 задача
h1, h2, h3, h4 = map(int, input().split())

if h1 <= h2 <= h3 <= h4 or h1 >= h2 >= h3 >= h4:
    print("YES")
else:
    print("NO")





# 2 задача

n, m, k = map(int, input().split())

total_checks = n * k
total_time = (total_checks + m - 1) // m  # округляем вверх до целого числа

print(total_time)



# 3 задача

from math import inf
 
n = int(input())
s = input()
ans = inf
for i in range(n - 1):
    for j in range(i + 1, n):
        if len(set(s[i:j + 1])) == 4:
            ans = min(ans, j - i + 1)
if ans is inf:
    print(-1)
else:
    print(ans)



#  4 задача

 def is_boring(arr):
    s = set(arr)
    if len(s) == 2:
        if arr.count(min(s)) == 1:
            return True
        if arr.count(max(s)) == 1:
            return True
    if arr.count(1) == len(arr):
        return True
    return False
 
 
n = int(input())
*a, = map(int, input().split())
ans = 1
d = {}
for i in range(n):
    key = a[i]
    d[key] = d.get(key, 0) + 1
    if is_boring(list(d.values())):
        ans = i + 1
print(ans)



# 5 задача
input()
bals = list(map(int, input().split()))
n = len(bals)
rngs = set()
for start in range(n - 1):
    for end in range(start + 2, n + 1):
        if sum(bals[start:end]) == 0:
            rngs |= { (i, j) for i in range(start + 1) for j in range(end - 1, n) }
            break
print(len(rngs))




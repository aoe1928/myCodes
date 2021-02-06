from collections import deque

N = int(input())
A = deque(map(int, input().split()))

def divid_2(n):
    while True:
        if n % 2 != 0:
            break
        n = n // 2
    return n

num_set = set()

for _ in range(N):
    num = A.pop()
    num = divid_2(num)
    num_set.add(num)

print(len(num_set))
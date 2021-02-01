# 配列
array = [4, 2, 5, 6, 1, 7]
# 配列の長さ
N = len(array)
for i in range(N):
    w = array[i]
    k = i
    for j in range(i + 1, N):
        if w > array[j]:
            w = array[j]
            k = j
    array[k] = array[i]
    array[i] = w

print(array)
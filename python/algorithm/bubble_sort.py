# 配列
array = [2, 6, 1, 5, 8, 7, 9, 0, 3]
# 配列の長さ
N = len(array)
for i in range(N):
    for j in range(N-1, i, -1):
        if array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]

print(array)

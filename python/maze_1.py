import numpy as np
import random

# 1 壁 0 通路

def main():
    # 迷路の大きさ、H Wは奇数
    H, W = 21, 21
    maze = np.zeros((H, W), dtype='int32')
    road_list = []
    for h in range(H):
        maze[h][0], maze[h][-1] = 1, 1
        if 0 < h < H-1 and h % 2 == 0:
            road_list.append((h, 0))
            road_list.append((h, W-1))
    for w in range(W):
        maze[0][w], maze[-1][w] = 1, 1
        if 0 < w < W-1 and w % 2 == 0:
            road_list.append((0, w))
            road_list.append((H-1, w))
    r_l = len(road_list)
    start = road_list.pop(random.randrange(0, r_l))
    print(start, 'start')
    
    def move(h, w):
        maze[h][w] = 1
        move_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        lst = [0, 1, 2, 3]
        while lst:
            l = lst.pop(random.randrange(0, len(lst)))
            l = move_list[l]
            if 0 <= h + l[0] * 2 < H and 0 <= w + l[1] * 2 < W:
                if maze[h + l[0]][w + l[1]] == 0 and maze[h + l[0] * 2][w + l[1] * 2] == 0:
                    h, w = h + l[0], w + l[1]
                    maze[h][w] = 1
                    if h % 2 == 0 and w % 2 == 0:
                        road_list.append((h, w))
                    h, w = h + l[0], w + l[1] 
                    if h % 2 == 0 and w % 2 == 0:
                        road_list.append((h, w))
                    maze[h][w] = 1
                    lst = [0, 1, 2, 3]
        r_l = len(road_list)
        if r_l == 0:
            return 0
        start = road_list.pop(random.randrange(0, r_l))
        move(*start)

    move(*start)

    for h in range(H):
        for w in range(W):
            if maze[h][w] == 1:
                print('■', end='')
            else:
                print(' ', end='')
            if w == W - 1:
                print()


if __name__ == '__main__':
    main()
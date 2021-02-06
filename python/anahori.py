#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random

N, M = 11, 13  # size of maze

maze = np.ones((N, M), dtype='int64')
# for n in range(N):
#     for m in range(M):
#         maze[n][0], maze[n][-1], maze[0][m], maze[-1][m] = 0, 0, 0, 0

n, m = 1, 1

def make_maze(n, m):
    maze[n][m] = 0
    vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while True:
        v = vectors.pop(random.randrange(0, len(vectors)))
        try:
            p, q = n + v[0] * 2, m + v[1] * 2
            r = maze[p][q]
        except IndexError:
            print(n, m)
        finally:
            if r == 1 and maze[n + v[0]][m + v[1]] == 1:
                n, m = n + v[0], m + v[1]
                maze[n][m] = 0
                vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if len(vectors) == 0:
            for s, t in zip(range(1, N, 2), range(1, M, 2)):
                if maze[s][t] == 0:
                    print(s, t)
                    print(maze)
                    make_maze(s, t)
                    break
            else:
                return 0

make_maze(1, 1)
print(maze)
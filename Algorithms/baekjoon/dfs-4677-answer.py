import sys
import collections

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(v):
    q = collections.deque()
    q.append(v)

    while q:
        v = q.popleft()
        for a in range(8):
            i = v[0] + di[a]
            j = v[1] + dj[a]
            if 0 <= i <= N-1 and 0<= j <= M-1 and land[i][j] is '@' and not(visited[i][j]):
                visited[i][j] = True
                q.append([i,j])

while True:
    N, M = map(int, input().split())
    cnt = 0
    if N is 0 and M is 0:
        break
    land = [list(input()) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not(visited[i][j]) and land[i][j] is '@':
                cnt += 1
                visited[i][j] = True
                dfs([i, j])
    print(cnt)
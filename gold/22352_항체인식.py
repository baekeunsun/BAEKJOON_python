# 2232 항체인식


import sys
from collections import deque
input = sys.stdin.readline

def bfs(temp):
    global array2
    global array1
    
    while queue :
        x,y = queue.popleft()
        num = array1[x][y]
        array1[x][y] = temp
                
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]

            if 0 <= ix < N and 0 <= iy < M and visited[ix][iy] == False and array1[ix][iy] == num:
                queue.append([ix,iy])
                visited[ix][iy] = True
def turn():                  
    for i in range(N):
        for j in range(M):
            if array1[i][j] != array2[i][j]: # 두개 다르면 array2 bfs 돌리기
                temp = array2[i][j]
                queue.append([i,j])
                visited[i][j] = True
                bfs(temp)
                return ans()
    return "YES"


def ans():
    for i in range(N):
        for j in range(M):
            if array1[i][j] != array2[i][j]:
                return "NO"
    return "YES"

N,M = map(int,input().split())
array1 = list(list(map(int,input().split()))for _ in range(N))
array2 = list(list(map(int,input().split()))for _ in range(N))
visited = list([False for _ in range(M)]for _ in range(N))
temp = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()

print(turn())


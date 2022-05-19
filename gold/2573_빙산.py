# 2573 빙산

from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
array = list(list(map(int,input().split()))for _ in range(N))
visited = []


dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
def check(): # 덩어리 수 세기
    global visited
    visited = list([False for _ in range(M)]for _ in range(N))
    num = 0
    another = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] != 0 and visited[i][j] == False:
                another = 1
                visited[i][j] = True
                queue.append([i,j])
                bfs()
                num += 1
    if another == 0:
        print(0)
        exit()
    else :
        return num

def bfs(): # 한 덩어리 확인
    while queue :
        x,y = queue.popleft()        

        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]

            if 0 <= ix < N and 0 <= iy < M:
                if array[ix][iy] != 0 and visited[ix][iy] == False:
                    queue.append([ix,iy])
                    visited[ix][iy] = True
    
def melt(): # 녹이기
    temp_array = [item[:] for item in array]
        
    for x in range(N):
        for y in range(M):
            if array[x][y] != 0:
                temp = 0
                for k in range(4):
                    ix = x + dx[k]
                    iy = y + dy[k]

                    if 0 <= ix < N and 0 <= iy < M and array[ix][iy] == 0:
                        temp +=1
                temp_array[x][y] = max(0,array[x][y]-temp)
    return temp_array


# bfs 돌려서 두덩어리이상 나올때까지 0만큼 빼주기
ans = 0
land = 1
while land < 2:
    array = melt()
    land = check()
    ans += 1

print(ans)
    

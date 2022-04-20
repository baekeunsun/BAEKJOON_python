import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())

array = [[] for _ in range(N+1)]
flag = list(False for _ in range(N+1))

ans = 0

def find(num):
    flag[num] = True

    for i in array[num]:
        if flag[i] == False:
            flag[i] = True
            find(i)
            
                     
for _ in range(M):
    i,j = map(int,input().split())
    array[i].append(j)
    array[j].append(i)

for i in range(1,N+1):
    if not flag[i] :
        find(i)
        ans += 1


print(ans)

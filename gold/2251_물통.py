# 2251 물통

from collections import deque

A,B,C = map(int, input().split())

array = list()
array.append([0,0,C])

queue = deque()
queue.append([0,0,C])

while queue :
    a,b,c = queue.popleft()
    if a > 0 :
        if B > a+b > 0 :
            temp = [0,a+b,c]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        else:
            temp = [a-B+b,B,c]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        if C > a+c > 0 :
            temp = [0,b,a+c]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        else :
            temp = [a-C+c,b,C]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
            
    if b > 0 :
        if A > b+a > 0 :
            temp = [b+a,0,c]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        else :
            temp = [A,b-A+a,c]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        if C > b+c > 0 :
            temp = [a,0,b+c]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        else :
            temp = [a,b-C+c,C]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
            
    if c > 0:
        if A > c+a > 0 :
            temp = [c+a, b, 0]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        else :
            temp = [A,b,c-A+a]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        if B > c+b > 0 :
            temp = [a,b+c,0]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
        else:
            temp = [a,B,c-B+b]
            if temp not in array :
                queue.append(temp)
                array.append(temp)
ans = []
for a,b,c in array :
    if a == 0:
        ans.append(c)

ans.sort()
for i in ans:
    print(i, end=" ")
        
        

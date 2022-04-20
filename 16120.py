import sys
input = sys.stdin.readline

string = list(input())
one = 0
i = 0
k = 0

while i < len(string)-1:
    if string[i] == 'P':
        one+=1
        i+=1
        continue
    if one>=2 and string[i+1] == 'P':
        one-=1
        i+=1
    else:
        k=1
        break
    i+=1

if one!=1 or k==1:
    print("NP")
else:
    print("PPAP")

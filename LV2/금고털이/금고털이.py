import sys
input = sys.stdin.readline

w, n = map(int, input().split())

jewelry = [list(map(int,input().split())) for i in range(n)]
jewelry.sort(key=lambda x:x[1], reverse=True)

result = 0
for m,p in jewelry:
    if(w>m):
        result = result+m*p
        w = w-m
    else:
        result = result+w*p
        break

print(result)
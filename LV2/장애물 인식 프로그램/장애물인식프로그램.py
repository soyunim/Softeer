import sys

cnt = []
result = []

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    
    if graph[x][y]==1:
        cnt.append(1)
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

answer = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            answer+=1
            result.append(len(cnt))
            cnt = []

print(answer)
result.sort()
for i in range(len(result)):
    print(result[i])
import sys
input = sys.stdin.readline

speed_max = 0
now = 1
limit_info = [0]*101

n, m = map(int, input().split())

for i in range(n):
    section, speed = map(int, input().split())
    for j in range(now, now+section):
        limit_info[j] = speed
    now = now+section

now = 1
result = 0
for i in range(m):
    section, speed = map(int, input().split())
    for j in range(now, now+section):
        result = max(result, speed-limit_info[j])
    now = now+section

print(result)
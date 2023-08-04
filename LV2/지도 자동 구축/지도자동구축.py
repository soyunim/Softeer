import sys
import math
input = sys.stdin.readline

result = 0
now = 1

n = int(input())

for i in range(n+1):
    result = math.pow(now+1,2)
    now = now*2

print(int(result))
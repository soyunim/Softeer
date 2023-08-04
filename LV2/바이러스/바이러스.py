import sys

K,P,N = list(map(int,sys.stdin.readline().split()))

for i in range(N):
    K = (K * P) % 1000000007

print(K)
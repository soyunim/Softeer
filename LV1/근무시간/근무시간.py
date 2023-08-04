import sys
input = sys.stdin.readline

minute=0
hour=0
result=0

for i in range(5):
    start, end = map(str, input().split())
    shour, smin = start.split(":")
    ehour, emin = end.split(":")
    shour, smin, ehour, emin = int(shour), int(smin), int(ehour), int(emin)

    if(emin>smin):
        minute+=emin-smin
        hour+=ehour-shour

    else:
        minute+=60-smin+emin
        hour+=ehour-shour-1


result=hour*60+minute
print(result)
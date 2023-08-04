import sys
input = sys.stdin.readline

light = {
    "0" : "1110111",
    "1" : "0010010",
    "2" : "1011101",
    "3" : "1011011",
    "4" : "0111010",
    "5" : "1101011",
    "6" : "1101111",
    "7" : "1110010",
    "8" : "1111111",
    "9" : "1111011",
    " " : "0000000"
}


t = int(input())

for i in range(t):
    a, b = map(str,input().split())
    a = (5-len(a))*" "+a
    b = (5-len(b))*" "+b

    result = 0
    for j in range(5):
        for k in range(7):
            result += (light[a[j]][k]!=light[b[j]][k])
    print(result)
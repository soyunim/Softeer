import sys
input = sys.stdin.readline

n, m = map(int, input().split())
timetable = {}

for i in range(n):
    timeline = ["09","10","11","12","13","14","15","16","17","18"]
    timetable[input().rstrip()] = timeline


for j in range(m):
    r, s, t = input().split()
    for i in range(int(s)-9, int(t)-8):
        timetable[r][i]=" "
timetable=dict(sorted(timetable.items()))


cnt = 0
for i, j in timetable.items():
    cnt=cnt+1
    print("Room "+i+":")
    result_s = []
    result_e = []
    for k in range(10):

        #시작이 9
        if(j[k]!=" " and k==0):
            result_s.append(j[k])
        if(j[k]!=" " and k!=0 and j[k-1]==" "):
            result_s.append(str(int(j[k])-1))

        # 끝이 18
        if(j[k]!=" " and k==9):
            result_e.append(j[k])
        if(j[k]!=" " and k!=9 and j[k+1]==" "):
            result_e.append(str(int(j[k])+1))


    if(len(result_s)==0):
        print("Not available")
    else:
        print(str(len(result_s))+" available:")

    for l in range(len(result_s)):
        print(result_s[l]+"-"+result_e[l])

    if(cnt!=len(timetable)):
        print("-----")
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
timetable = {}

for i in range(n):
    timeline = [0,0,0,0,0,0,0,0,0,0]
    timetable[input().rstrip()] = timeline


for j in range(m):
    r, s, t = input().split()
    for i in range(int(s)-9, int(t)-9+1):
        timetable[r][i]=1

timetable=dict(sorted(timetable.items()))

cnt =0
for i,j in timetable.items():
    cnt=cnt+1
    print("Room "+i+":")
    start = 0
    end = 0
    time_s = []
    time_e = []
    for k in range(10):
        if(k==0 and j[k]==0 and start==0 and end==0):
            start=1
            time_s.append(str(k+9))
        if(k!=0 and j[k]==0 and start==0 and end==0):
            start=1
            end=0
            time_s.append(str(k+8))
        if(k!=0 and j[k]==0 and start==0 and end==1):
            start=1
            end=0
            time_s.append(str(k+8))

        if(j[k]==1 and start==1):
            end=1
            start=0
            time_e.append(str(k+9))
        if(k==9 and j[k]==0 and start==1 and end==0):
            time_e.append(str(k+9));
    if(len(time_s)==0):
        print("Not available")
    else:
        print(str(len(time_s))+" available:")

        for l in range(len(time_s)):
            if(time_s[l]=="9"):
                time_s[l]="09"
            if(time_e[l]=="9"):
                time_e[l]="09"
            print(str(time_s[l])+"-"+str(time_e[l]))

    if(cnt!=len(timetable)):
        print("-----")
    
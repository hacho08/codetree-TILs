N, M, K = map(int, input().split())


arr = [list(map(int, input().split())) for x in range(N)]

for i in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    arr[x][y] += -1

er, ec =  map(lambda x: int(x)-1, input().split())
arr[er][ec] = -11

moved = 0
cnt = M

def move(arr, cnt):
    #상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    narr = [x[:] for x in arr]

    for r in range(N):
        for c in range(N):
            if -11<arr[r][c]<0:
                # exit과의 거리 계산
                dist = abs(er-r) + abs(ec-c)
                for i in range(len(dr)):
                    if abs(r+dr[i]-er)+abs(c+dc[i]-ec) < dist:
                        narr[r][c] -= arr[r][c]
                        global moved
                        moved += arr[r][c]

                        if narr[r+dr[i]][c+dc[i]] == -11:
                            cnt += arr[r][c]
                        else:
                            narr[r+dr[i]][c+dc[i]] += arr[r][c]
                        
                        break
    arr = narr
    
    if cnt == 0:
        return

def find_square(arr):
    # 가장 작은 정사각형 구하기
    mn = N
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0:
                mn = min(mn, max(abs(er-i), abs(ec-j)))

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=er<=si+mn and sj<=ec<=sj+mn:
                for i in range(si, si+mn+1):
                    for j in range(sj, sj+mn+1):
                        if -11<arr[i][j]<0:
                            return si, sj, mn+1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j]==-11:
                return i,j
            
def turn(arr):
    narr = [x[:] for x in arr]
    si, sj, L = find_square(arr)
    narr = [x[:] for x in arr]
    # 90도로 회전하기
    for i in range(si, si+L):
        for j in range(sj, sj+L):
            if arr[i][j]>0:
                narr[L-1-j][i] = arr[i][j]-1
            else:
                narr[L-1-j][i] = arr[i][j]

    arr = narr
    er, ec = find_exit(arr)

for _ in range(K):
    move(arr, cnt)
    turn(arr)
print(-moved)
print(er+1, ec+1)
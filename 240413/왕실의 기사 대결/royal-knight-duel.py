import sys

l, n, q = map(int, sys.stdin.readline().split())

field = [[2]*(l+2)] + [[2]+list(map(int, sys.stdin.readline().split()))+[2] for _ in range(l)] + [[2]*(l+2)]
knights = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
orders = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]

knightField = [[0 for _ in range(l)] for _ in range(l)]
init_k = [0 for _ in range(n+1)]

d_r = [-1, 0, 1, 0]
d_c = [0, 1, 0, -1]

knightDict = {}
answer = 0

def attack(knight, dr):

    q = []
    visited = set()
    damaged = [0 for _ in range(n+1)]

    q.append(knight)
    visited.add(knight)
    
    
    while q:
        knight_i = q.pop(0)
        r, c, h, w, k = knightDict[knight_i]
        nr = r + d_r[dr]
        nc = c + d_c[dr]

        # 이동했을 때 field에서 벽, 장애물 확인 
        for i in range(nr, nr+h):
            for j in range(nc, nc+w):
                if field[i][j] == 2:
                    return
                
                if field[i][j] == 1:
                    damaged[knight_i] += 1
        
        # 이동 했을때 다른 기사들이랑 부딛히는지 확인 
        for idx in knightDict:
            if idx not in visited:
                # 겹치면
                tr, tc, th, tw, k = knightDict[idx]
                if tr<nr+h and tc<nc+w and nr<tr+th and nc<tc+tw:
                    q.append(idx)
                    visited.add(idx)

    # 명령 받은 기사는 데미지 없음 
    damaged[knight] = 0

    # 이동 가능한지 다 확인 한 후 이동
    for idx in visited:
        r, c, h, w, k = knightDict[idx]
        if k - damaged[idx] <= 0:
            knightDict.pop(idx)
        else: 
            knightDict[idx][0] = r + d_r[dr]
            knightDict[idx][1] = c + d_c[dr]
            knightDict[idx][-1] = k - damaged[idx]


for i, knight in enumerate(knights):
    knightDict[i+1] = knight
    init_k[i+1] = knight[-1]


for order in orders:
    knight, dr = order
    if knight in knightDict:
        attack(knight, dr)

for i in knightDict:
    answer += init_k[i] - knightDict[i][-1]

print(answer)
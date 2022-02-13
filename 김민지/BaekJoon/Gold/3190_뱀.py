import sys
sys.stdin = open("input.txt", "r")

delta = {'R': [0,1], 'L': [0,-1], 'U': [-1,0], 'D': [1,0]}
directions = ['R', 'D', 'L', 'U']

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 갯수

board = [[0]*N for _ in range(N)] # 보드 초기화
board[0][0] = 'R' # 뱀의 처음 위치 및 머리의 진행 방향 (R: 오른쪽, L: 왼쪽, U: 위, D: 아래)

# 사과 위치 초기 세팅
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

# 이동 순서 입력 받기
M = int(input())
moves = {}
for _ in range(M):
    x, c = input().split()
    moves[x] = c

hr, hc = 0, 0 # 머리(head) 인덱스
tr, tc = 0, 0 # 꼬리(tail) 인덱스
hd = 0 # 머리의 진행 방향
time = 0
flag = False # 사과를 먹었는지 유무

while True:

    time += 1

    # 1. 머리가 한칸 이동
    dr, dc = delta[directions[hd]]
    hr, hc = hr+dr, hc+dc

    # 2. 벽 또는 자기 자신과 부딪혔는지 체크
    if (hr < 0) or (hc < 0) or (hr >= N) or (hc >= N):
        break
    elif str(board[hr][hc]).isalpha():
        break
    
    # 3. 게임이 끝나지 않았다면 다음 칸으로 이동
    # 3-1. 방향 전환이 있는지 없는지 확인
    if str(time) in moves:
        if moves[str(time)] == 'D':
            hd = (hd + 1) % 4
        else:
            hd = (hd + 3) % 4
    
    # 3-2. 다음 칸에 사과가 있는지 확인
    if board[hr][hc]:
        flag = True 
    
    # 3-3. 다음 칸으로 이동
    board[hr][hc] = directions[hd]


    # 3-4. 사과를 먹지 않았다면, 꼬리도 같이 한칸 앞으로 이동
    if not flag:
        dr, dc = delta[board[tr][tc]]
        board[tr][tc] = 0
        tr, tc = tr+dr, tc+dc 
    
    flag = False

print(time)
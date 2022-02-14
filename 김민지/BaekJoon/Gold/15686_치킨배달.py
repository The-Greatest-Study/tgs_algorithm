from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
houses, chicken = [], []

# 일반집과 치킨집의 좌표를 각각 houses, chicken 배열에 저장
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append([r, c])
        elif city[r][c] == 2:
            chicken.append([r, c])


# 각 치킨집 위치 경우의 수 별로 치킨거리를 구한다
def find_chicken_dist(combi):
    chicken_dist = 0
    for r, c in houses:
        dist = 99999999
        for cr, cc in combi:
            dist = min(dist, abs(cr-r) + abs(cc-c))
        chicken_dist += dist
    return chicken_dist


# 치킨집을 N개만 고를 수 있는 경우의 수
chicken_combi = combinations(chicken, M)

min_dist = 99999999999
for combi in chicken_combi:
    min_dist = min(min_dist, find_chicken_dist(combi))

print(min_dist)
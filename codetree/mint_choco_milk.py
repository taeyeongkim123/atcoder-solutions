"""Codetree (Samsung SW 기출) - 민트초코우유
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description

문제
----
N×N 격자 위에 학생들이 있고, 각 학생은 좋아하는 음식 집합(T=민트,
C=초코, M=우유의 부분집합)과 신앙심(B) 값을 갖는다. T일 동안 하루마다
아침/점심/저녁 세 단계를 반복하며 신앙심과 좋아하는 음식이 전파된다.

- 아침: 모든 학생의 신앙심이 1씩 증가한다.
- 점심: 좋아하는 음식이 정확히 같은 학생들끼리 상하좌우로 연결된 그룹을
  BFS로 찾는다. 각 그룹에서 신앙심이 가장 높은(동률이면 행-열이 작은)
  학생을 대표로 뽑고, 나머지 그룹원의 신앙심 1씩을 대표에게 몰아준다.
- 저녁: 그룹을 (단일/이중/삼중 음식 개수, 대표의 신앙심 내림차순,
  행, 열) 순으로 정렬해 전파 순서를 정하고, 각 대표는 "간절함"
  (원래 신앙심 - 1)만큼을 자신의 신앙심을 4로 나눈 나머지가 가리키는
  방향으로 한 방향 직진하며 이웃 학생들에게 나눠준다. 이미 그날 저녁에
  전파를 받은 학생은 더 이상 전파 대상이 되지 않는다(방어 상태).

접근
----
격자를 그대로 시뮬레이션한다. 점심 단계는 좋아하는 음식별로 각각
BFS 연결요소를 구해 그룹/대표/신앙심 정산을 처리하고, 저녁 단계는
정해진 우선순위로 정렬된 대표 리스트를 순회하며 간절함을 소모할
때까지 한 방향으로 전파한다. 하루가 끝나면 음식 조합별 신앙심 총합을
집계해 출력한다.

주의
----
Codetree 문제 페이지가 로그인 없이는 본문이 보이지 않아, 공식 예제
입출력으로 검증하지 못했다. 문법 검사와 간단한 스모크 테스트만
통과한 상태이며, 정확성은 Codetree 채점 결과로 확인 필요.
"""

import sys
from collections import deque


def merge_food(food1, food2):
    """두 음식을 결합하여 T -> C -> M 순서의 표준 문자열로 만듭니다."""
    s = set(food1) | set(food2)
    res = ""
    for char in ["T", "C", "M"]:
        if char in s:
            res += char
    return res


def main():
    # 입력 처리
    N, T = map(int, sys.stdin.readline().split())

    L_grid = []
    for _ in range(N):
        L_grid.append(list(sys.stdin.readline().strip()))

    B_grid = []
    for _ in range(N):
        B_grid.append(list(map(int, sys.stdin.readline().split())))

    # -------------------------------------------------------------
    # 시뮬레이션 시작 (T일 동안 반복)
    # -------------------------------------------------------------
    for day in range(T):

        # 1. 아침 시간 (#morning)
        for i in range(N):
            for j in range(N):
                B_grid[i][j] += 1

        # 2. 점심 시간 (#noon)
        like_list = ["T", "C", "M", "CM", "TM", "TC", "TCM"]
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]

        leaders_to_propagate = []

        for food_type in like_list:
            visited_list = [[False] * N for _ in range(N)]

            for r in range(N):
                for c in range(N):
                    # L_grid[r][c]가 리스트나 단일 문자열일 수 있으므로 "".join으로 변환하여 비교
                    curr_food = "".join(L_grid[r][c]) if isinstance(L_grid[r][c], list) else L_grid[r][c]

                    if curr_food == food_type and not visited_list[r][c]:
                        queue = deque([(r, c)])
                        visited_list[r][c] = True
                        group_members = [(r, c)]

                        while queue:
                            curr_r, curr_c = queue.popleft()
                            for d in range(4):
                                nr, nc = curr_r + dr[d], curr_c + dc[d]
                                if 0 <= nr < N and 0 <= nc < N:
                                    next_food = "".join(L_grid[nr][nc]) if isinstance(L_grid[nr][nc], list) else L_grid[nr][nc]
                                    if next_food == food_type and not visited_list[nr][nc]:
                                        visited_list[nr][nc] = True
                                        queue.append((nr, nc))
                                        group_members.append((nr, nc))

                        # 대표자 선정 (신앙심 높은 순 -> 행 작은 순 -> 열 작은 순)
                        leader_r, leader_c = max(
                            group_members,
                            key=lambda pos: (B_grid[pos[0]][pos[1]], -pos[0], -pos[1])
                        )

                        leaders_to_propagate.append((leader_r, leader_c, food_type))

                        # 신앙심 정산
                        for mem_r, mem_c in group_members:
                            if mem_r == leader_r and mem_c == leader_c:
                                B_grid[mem_r][mem_c] += (len(group_members) - 1)
                            else:
                                B_grid[mem_r][mem_c] -= 1

        # 3. 저녁 시간 (#evening)
        # 단일(1), 이중(2), 삼중(3) 그룹으로 분류
        group_priority = {
            "T": 1, "C": 1, "M": 1,
            "CM": 2, "MC": 2, "TM": 2, "MT": 2, "TC": 2, "CT": 2,
            "TCM": 3, "TMC": 3, "CTM": 3, "CMT": 3, "MTC": 3, "MCT": 3
        }

        leaders_to_propagate.sort(key=lambda x: (
            group_priority[x[2]],
            -B_grid[x[0]][x[1]],
            x[0],
            x[1]
        ))

        # 전파 방향: 0: 위, 1: 아래, 2: 왼쪽, 3: 오른쪽
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        state_defense = set()

        for leader_r, leader_c, M in leaders_to_propagate:
            # 방어 상태면 당일 저녁 전파 스킵
            if (leader_r, leader_c) in state_defense:
                continue

            orig_B = B_grid[leader_r][leader_c]
            F = orig_B - 1       # 간절함 x = B - 1
            B_grid[leader_r][leader_c] = 1  # 자신은 1만 남음

            D = orig_B % 4       # 원래 신앙심 % 4

            curr_r, curr_c = leader_r, leader_c

            while F > 0:
                curr_r += dx[D]
                curr_c += dy[D]

                # 격자 밖으로 나가면 종료
                if not (0 <= curr_r < N and 0 <= curr_c < N):
                    break

                target_food = "".join(L_grid[curr_r][curr_c]) if isinstance(L_grid[curr_r][curr_c], list) else L_grid[curr_r][curr_c]

                # 신봉 음식이 완전히 같으면 전파 없이 패스 (간절함 차감 없음)
                if target_food == M:
                    continue

                # 전파 당한 학생은 바로 방어 상태가 됨
                state_defense.add((curr_r, curr_c))

                y = B_grid[curr_r][curr_c]

                # 1) 강한 전파 (x > y)
                if F > y:
                    L_grid[curr_r][curr_c] = M
                    F -= (y + 1)
                    B_grid[curr_r][curr_c] += 1
                    if F <= 0:
                        break

                # 2) 약한 전파 (x <= y)
                else:
                    L_grid[curr_r][curr_c] = merge_food(target_food, M)
                    B_grid[curr_r][curr_c] += F
                    F = 0
                    break

        # 4. 하루 종료 후 결과 집계 및 출력
        # 출력 순서: 민트초코우유, 민트초코, 민트우유, 초코우유, 우유, 초코, 민트
        order = ["TCM", "TC", "TM", "CM", "M", "C", "T"]
        faith_sum = {food: 0 for food in order}

        for r in range(N):
            for c in range(N):
                food = "".join(L_grid[r][c]) if isinstance(L_grid[r][c], list) else L_grid[r][c]
                if food in faith_sum:
                    faith_sum[food] += B_grid[r][c]

        print(" ".join(str(faith_sum[food]) for food in order))


if __name__ == "__main__":
    main()

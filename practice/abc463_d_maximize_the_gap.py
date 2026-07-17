"""AtCoder Beginner Contest 463 - D: Maximize the Gap (복습용 재풀이)
https://atcoder.jp/contests/abc463/tasks/abc463_d

문제
----
수직선 위에 N개의 구간 [L_i, R_i]가 있다. 이 중 서로 겹치지 않는 K개를
골라서, 고른 것들 사이 모든 인접 쌍의 거리 중 최솟값(점수)을 최대화하라.
그런 K개를 고를 수 없으면 -1을 출력한다.

접근
----
"최솟값의 최대화"이므로 답(간격 g)을 이분탐색한다. 후보 g가 실현
가능한지는 구간들을 오른쪽 끝(R) 오름차순으로 정렬한 뒤 탐욕적으로
확인한다: 마지막으로 고른 구간의 오른쪽 끝을 last_r이라 할 때, 다음 구간의
L이 last_r + g 이상이면 그 구간을 고른다. 고른 개수가 K 이상이면 g는
실현 가능하다.

g=1(가장 느슨한 경우)조차 K개를 고를 수 없으면 -1을 출력한다. 그렇지
않으면 lo=1에서 시작해, "lo는 항상 실현 가능한 값"이라는 불변식을
유지하며 이분탐색한다 (mid를 올림 나눗셈으로 계산하고 성공 시 lo=mid로
그 자신을 후보로 남겨서, 루프 종료 후 lo가 바로 정답이 되도록 함).

시간복잡도: O(N log N log(max coordinate))
"""

import sys


def feasible(data: list[list[int]], k: int, gap: int) -> bool:
    point = 0
    idk = 0
    last_r = -(10**18)
    while point < k:
        if idk > len(data) - 1:
            return False
        if data[idk][0] - last_r >= gap:
            last_r = data[idk][1]
            point += 1
        idk += 1
    return True


def solve(n: int, k: int, data: list[list[int]]) -> int:
    data = sorted(data, key=lambda x: x[1])

    if not feasible(data, k, 1):
        return -1

    lo, hi = 1, 2 * 10**9
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(data, k, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def main() -> None:
    data_in = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data_in[idx])
    k = int(data_in[idx + 1])
    idx += 2
    data = []
    for _ in range(n):
        left = int(data_in[idx])
        r = int(data_in[idx + 1])
        idx += 2
        data.append([left, r])

    print(solve(n, k, data))


if __name__ == "__main__":
    main()

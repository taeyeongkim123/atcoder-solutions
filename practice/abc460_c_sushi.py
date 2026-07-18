"""AtCoder Beginner Contest 460 - C: Sushi (복습용 재풀이)
https://atcoder.jp/contests/abc460_c

문제
----
샤리(밥) N개(무게 A_i)와 네타(재료) M개(무게 B_j)가 있다. 샤리 1개와
네타 1개를 짝지어 초밥 1개를 만들려면 "네타 무게 <= 샤리 무게 x 2"를
만족해야 한다. 각 샤리/네타는 최대 1번만 사용 가능. 만들 수 있는 최대
초밥 개수를 구하라.

접근
----
A(샤리), B(네타)를 모두 오름차순 정렬한 뒤 투 포인터로 매칭한다.
샤리 포인터 i는 항상 한 칸씩 전진하고, 네타 포인터 j는 매칭에
성공했을 때만 전진한다.

- 가장 작은 미매칭 샤리 A[i]와 가장 작은 미매칭 네타 B[j]를 비교해
  B[j] <= 2*A[i]이면 매칭 확정, i와 j 둘 다 전진.
- 아니면(A[i]가 너무 작아서 B[j]를 못 받아주면) 이 네타는 더 큰
  샤리라면 받아줄 수 있으니 그대로 두고, 샤리만 다음(더 큰) 것으로
  넘어간다.

작은 샤리를 먼저 소모하면서 감당 가능한 가장 작은 네타부터 매칭시켜
두면, 큰 샤리를 필요 이상으로 작은 네타에 낭비하지 않게 되어 최적이
된다(교환 논증으로 증명 가능한 전형적인 그리디 매칭 패턴).

시간복잡도: O(N log N + M log M)
"""

import sys


def solve(n: int, m: int, sha: list[int], neta: list[int]) -> int:
    sha = sorted(sha)
    neta = sorted(neta)

    answer = 0
    i, j = 0, 0
    while i != n and j != m:
        if neta[j] <= 2 * sha[i]:
            answer += 1
            i += 1
            j += 1
        else:
            i += 1
    return answer


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    sha = [int(data[idx + k]) for k in range(n)]
    idx += n
    neta = [int(data[idx + k]) for k in range(m)]

    print(solve(n, m, sha, neta))


if __name__ == "__main__":
    main()

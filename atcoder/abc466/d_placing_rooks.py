"""AtCoder Beginner Contest 466 - D: Placing Rooks
https://atcoder.jp/contests/abc466/tasks/abc466_d

문제
----
N*N 격자에서 M번의 조작을 순서대로 수행한다. i번째 조작은 R_i행과
C_i열에 있던 말을 모두 제거한 뒤, (R_i, C_i)에 말을 하나 놓는 것이다.
모든 조작이 끝난 뒤 격자에 남아있는 말의 개수를 구하라.

접근
----
정방향으로 시뮬레이션하면 한 번의 조작이 그 행/열에 있던 말들을
전부 지워야 해서 O(N*M)이 될 수 있다. 대신 조작을 뒤에서부터
살펴본다: 마지막에 놓인 말부터 거꾸로 확인하면서, 그 이후(시간상
더 나중, 즉 역순 기준으로는 이전)에 같은 행이나 열이 다시 쓰인
적이 없는 말만 최종적으로 살아남는다. 이미 등장한 행/열을 집합에
기록해두면 각 말이 살아남는지 O(1)에 판정할 수 있다.

시간복잡도: O(N + M)
"""

import sys


def solve(n: int, m: int, operations: list[tuple[int, int]]) -> int:
    visited_rows: set[int] = set()
    visited_cols: set[int] = set()
    ans = 0

    for r, c in reversed(operations):
        if r not in visited_rows and c not in visited_cols:
            ans += 1
        visited_rows.add(r)
        visited_cols.add(c)

    return ans


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    operations = []
    idx = 2
    for _ in range(m):
        r = int(data[idx])
        c = int(data[idx + 1])
        operations.append((r, c))
        idx += 2

    print(solve(n, m, operations))


if __name__ == "__main__":
    main()

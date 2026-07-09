"""AtCoder Beginner Contest 458 - C: C Stands for Center
https://atcoder.jp/contests/abc458/tasks/abc458_c

문제
----
대문자로만 이루어진 문자열 S가 주어진다. 홀수 길이의 부분문자열 중, 정중앙
문자가 'C'인 것의 개수를 구하라. 같은 문자열이라도 뽑힌 위치가 다르면 다른
부분문자열로 센다.

접근
----
홀수 길이 부분문자열은 항상 하나의 "중심" 위치를 가진다. 따라서 문자열의
각 'C' 위치 i를 중심으로, 왼쪽/오른쪽으로 대칭 확장 가능한 반지름
min(i, n-1-i)만큼 (반지름 0부터 그 값까지) 서로 다른 부분문자열이 하나씩
나온다. 즉 'C' 위치 하나당 min(i, n-1-i) + 1개의 부분문자열이 있으므로,
모든 'C' 위치에 대해 이 값을 더하면 답이 된다.

시간복잡도: O(N)
"""

import sys


def solve(s: str) -> int:
    n = len(s)
    total = 0
    for i, ch in enumerate(s):
        if ch == "C":
            total += min(i, n - 1 - i) + 1
    return total


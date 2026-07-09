# coding-test-solutions

CS 알고리즘 학습 기록용으로 [AtCoder](https://atcoder.jp/), [Programmers](https://school.programmers.co.kr/)
문제를 풀고 정리하는 저장소입니다.

## 풀이 목록

### AtCoder

| 문제 | 난이도 | 핵심 아이디어 | 시간복잡도 |
|---|---|---|---|
| [ABC458 C - C Stands for Center](https://atcoder.jp/contests/abc458/tasks/abc458_c) | 400 | 각 'C'를 중심으로 대칭 확장 가능한 반지름 계산 | O(N) |
| [ABC462 C - Not Covered Points](https://atcoder.jp/contests/abc462/tasks/abc462_c) | 300 | X 오름차순 정렬 + Y의 접두사 최솟값(prefix minimum) | O(N log N) |
| [ABC463 C - Tallest at the Moment](https://atcoder.jp/contests/abc463/tasks/abc463_c) | 300 | 접미사 최댓값 배열 + 이분 탐색 | O((N+Q) log N) |
| [ABC463 D - Maximize the Gap](https://atcoder.jp/contests/abc463/tasks/abc463_d) | 500 | 이분 탐색(정답) + 구간 스케줄링 탐욕으로 실현 가능성 판정 | O(N log N log C) |
| [ABC464 C - Plumage Palette](https://atcoder.jp/contests/abc464/tasks/abc464_c) | 300 | 색이 바뀌는 날짜만 이벤트로 처리해 distinct 개수 증분 관리 | O(N+M) |

### Programmers

| 문제 | 난이도 | 핵심 아이디어 | 시간복잡도 |
|---|---|---|---|
| [지게차와 크레인](https://school.programmers.co.kr/learn/courses/30/lessons/468379) | Lv.2 | 매 지게차 요청마다 테두리에서 빈 칸을 통해서만 BFS해 "진짜 바깥과 연결된" 영역 판정 | O(요청 수 x 격자 크기) |
| [선인장 숨기기](https://school.programmers.co.kr/learn/courses/30/lessons/388353) | 2025 카카오 하반기 2차 | 칸별 최초 피격 시점 계산 + 2D 슬라이딩 윈도우 최솟값(단조 deque) | O(m*n) |
| [광물 캐기](https://school.programmers.co.kr/learn/courses/30/lessons/172927) | Lv.2 | 다이아몬드 곡괭이 우선 배정 + 나머지는 5*다이아몬드+철 기준 정렬 그리디 | O(K log K) |
| [리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199) | Lv.2 | "미끄러져 멈추는 위치"를 한 번의 전이로 보는 BFS | O((R*C)*(R+C)) |

각 풀이 파일 맨 위 docstring에 문제 요약과 접근 방식을 한국어로 정리해뒀습니다.





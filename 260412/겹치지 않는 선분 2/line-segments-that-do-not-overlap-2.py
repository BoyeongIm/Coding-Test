n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
'''
정렬 필요 없고 그냥 모든 쌍에 대해서 봐야 하는 이유:
앞쪽에서 A가 C와 겹친다고 셌더라도 C 자신의 차례에서는 그 정보가 없음
한 쌍 (두개의 선분) 전체에 대해서 따져봐야 함.
'''
for i in range(n):
    a1, a2 = lines[i]
    crossed = False
    for j in range(n):
        if i==j:
            continue
        b1, b2 = lines[j]
        if (a1-b1) * (a2-b2) < 0: # 교차하는 조건!!
            crossed = True
            break
    if not crossed:
        ans += 1
print(ans)
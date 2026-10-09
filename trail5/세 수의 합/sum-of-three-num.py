n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import Counter

answer = 0
count = Counter(arr)
for i in range(n-1):
    # 이미 순회한 적이 있는 숫자는 빼 버림으로서
    # 같은 조합이 여러번 세어지는 걸 방지합니다.
    count[arr[i]] -= 1

    for j in range(i):
        diff = k-arr[i]-arr[j]
        if diff in count:
            answer += count[diff]

print(answer)
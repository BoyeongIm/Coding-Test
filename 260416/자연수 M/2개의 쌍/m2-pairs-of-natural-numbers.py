N = int(input())
x, y = zip(*[tuple(map(int, input().split())) for _ in range(N)])

nums = []
for i in range(N):
    nums.append([y[i], x[i]])
nums.sort(key=lambda x:(-x[0], x[1]))

i, j = 0, N-1
ans = -1

while i < j:
    minused = min(nums[i][1], nums[j][1])
    ssum = nums[i][0] + nums[j][0]
    if ans < ssum:
        ans = ssum
    nums[i][1] -= minused
    nums[j][1] -= minused
    if nums[i][1] == 0:
        i += 1
    if nums[j][1] == 0:
        j -= 1
    
print(ans)
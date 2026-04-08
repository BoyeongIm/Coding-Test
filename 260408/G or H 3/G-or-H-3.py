n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr = [0] * max(x)
for i in range(n):
    arr[x[i]-1] = 1 if c[i] == "G" else 2
window_pnts = sum(arr[:k+1])
max_pnts = window_pnts
for i in range(k+1, len(arr)):
    window_pnts += arr[i] - arr[i-k-1]
    max_pnts = max(max_pnts, window_pnts)
print(max_pnts)
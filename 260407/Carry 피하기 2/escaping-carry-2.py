n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def check_carry(n1, n2, n3):
    while n1>0 or n2>0 or n3>0:
        summ = n1%10 + n2%10+ n3%10
        if summ >= 10:
            return True
        n1 //= 10
        n2 //= 10
        n3 //= 10
    return False


import sys
maxsum = -sys.maxsize
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n): 
            n1 = arr[i]
            n2 = arr[j]
            n3 = arr[k]
            carry = check_carry(n1, n2, n3)
            if not carry:
                nsum = n1+n2+n3
                maxsum = max(maxsum, nsum)

print(maxsum)
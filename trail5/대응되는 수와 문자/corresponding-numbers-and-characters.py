n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
word_to_num = dict()
for i, w in enumerate(words):
    word_to_num[w]=int(i)
def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

for q in queries:  
    if is_int(q):
        print(words[int(q)])
    else:
        print(word_to_num[q])
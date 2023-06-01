import sys

n = int(sys.stdin.readline())

l = [sys.stdin.readline() for _ in range(n)]

for i, sentence in enumerate(l):
    words = sentence.split()
    words.reverse()
    print("Case #{}: {}".format(i+1, " ".join(words)))
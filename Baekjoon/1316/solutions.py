# Input
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
count = n

# Algorithm
for word in arr:
    history = []
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            count -= 1
            break
print(count)

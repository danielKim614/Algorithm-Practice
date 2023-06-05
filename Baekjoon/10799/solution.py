import sys

arr = sys.stdin.readline()

stack = []
prev = None
count = 0

for c in arr:
    if c == '(':
        stack.append(c)
    elif c == ')' and prev == '(':
        stack.pop()
        count += len(stack)
    elif c == ')':
        stack.pop()
        count += 1
    prev = c

print(count)
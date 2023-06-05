import sys

sentences = []

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    sentences.append(sentence)

for s in sentences:
    stack = []
    if s == '.':
        break

    for c in s:
        if c in ['[', '(']:
            stack.append(c)
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
                break
        elif c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
                break
        else:
            continue

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
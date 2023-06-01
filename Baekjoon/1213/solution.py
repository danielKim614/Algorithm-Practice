import sys
input = sys.stdin.readline

string = list(input().rstrip())
str_dict = dict()

string.sort()

for char in string:
    if char in str_dict.keys():
        str_dict[char] += 1
    else:
        str_dict[char] = 1

num_odd = 0
center, front = "", ""

for c, n in str_dict.items():
    if n % 2 == 1:
        if num_odd > 1:
            break
        center += c
        num_odd += 1
        
    front += c * (n // 2)

if num_odd > 1:
    output = "I'm Sorry Hansoo"
else:
    output = front + center + front[::-1]
    
print(output)

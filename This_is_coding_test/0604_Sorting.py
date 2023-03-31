'''
두 배열의 원소 교체
'''

# Input
n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
# Define Variables

# Algorithm
arr_a.sort()
arr_b.sort(reverse=True)

for i in range(k):
    if arr_a[i] < arr_b[i]:
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else:
        break

# Output
print(sum(arr_a))
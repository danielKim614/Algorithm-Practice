'''
성적이 낮은 순서로 학생 출력하기
'''

# Input
n = int(input())

# Define Variables
arr = []
for i in range(n):
    arr.append(input().split())

# Algorithm
arr = sorted(arr, key=lambda x: x[1])

# Output
for student in arr:
    print(student[0], end=' ')
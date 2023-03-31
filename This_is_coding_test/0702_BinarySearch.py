'''
부품 찾기
'''

# Input
n = int(input())
market_arr = list(map(int, input().split()))
m = int(input())
customer_arr = list(map(int, input().split()))

# Define Functions
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)
    
# Algorithm
market_arr.sort()
for item in customer_arr:
    result = binary_search(market_arr, item, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

'''
위에서 아래로
'''

# Input
n = int(input())

# Define Variables
arr = []
for i in range(n):
    arr.append(int(input()))

# Define Functions
def selection_sort(arr):
    for i in range(len(arr)-1):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[i-1] < arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    def merge(low, mid, high):
        tmp_arr = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] >= arr[j]:
                tmp_arr.append(arr[i])
                i += 1
            else:
                tmp_arr.append(arr[j])
                j += 1
        
        while i <= mid:
            tmp_arr.append(arr[i])
            i += 1
        while j <= high:
            tmp_arr.append(arr[j])
            j += 1

        for k in range(low, high + 1):
            arr[k] = tmp_arr[k-low]      
            
    def sort(low, high):
        if high - low < 1:
            return
        mid = (high + low) // 2
        sort(low, mid)
        sort(mid+1, high)
        merge(low, mid, high)
        
    sort(0, len(arr)-1)
    return arr

def quick_sort(arr):
    def partition(p, r):
        pivot = arr[p]
        i = p + 1
        for j in range(p+1, r+1):
            if arr[j] >= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i-1], arr[p] = arr[p], arr[i-1]

        return i-1
                
    def sort(p, r):
        if p < r:
            q = partition(p, r)
            sort(p, q-1)
            sort(q+1, r)

    sort(0, len(arr)-1)
    return arr

# def heap_sort(arr):
#     def heapify():
#         pass

# Algorithm
arr = quick_sort(arr)

# Outputs
for i in arr:
    print(i, end=' ')

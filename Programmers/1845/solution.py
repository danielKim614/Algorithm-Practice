import collections

def solution(nums):
    kind = len(collections.Counter(nums).keys())
    pick = len(nums) // 2
    
    if kind < pick:
        return kind
    else:
        return pick
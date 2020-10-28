import heapq

nums = [int(_) for _ in input().split(',')]
k = int(input())

print(heapq.nsmallest(k, nums))
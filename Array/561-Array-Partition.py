"""
Problem: 561. Array Partition
Topic: Array / Greedy
Difficulty: Easy
Time Complexity: O(n log n)
Space Complexity: O(1)
"""




nums =  [1,4,3,2]

nums.sort()
total = 0
for i in range(0, len(nums),2):
    total+=nums[i]



print(total)

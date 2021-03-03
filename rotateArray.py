# Task: https://leetcode.com/problems/rotate-array/

def reverseArr(nums, st_idx, e_idx):
    n = len(nums)
    start_idx = st_idx
    end_idx   = e_idx
    if n < 2 or start_idx < 0 or end_idx > n - 1:
        return
    # [1,2,3,4,5] 5//2 = 2, [1,2,3,4] 4//2 = 2
    while start_idx < end_idx:
        temp            = nums[start_idx]        
        nums[start_idx] = nums[end_idx]
        nums[end_idx]   = temp

        start_idx += 1
        end_idx   -= 1

def rotateByOne(nums):
    n = len(nums)
    if n < 2:
        return
    # example
    # [1, 2, 3, 4]
    # [4, 1, 2, 3]
    temp = nums[-1]
    for i in range(n - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = temp

def rotateArrayApproach01(nums, k):
    # approach 1
    # use slicing, uses extra space 
    # runtime O(n), space O(n)
    n = len(nums)
    return nums[n - k:] + nums[: n - k]   

def rotateArrayApproach02(nums, k):
    # approach 2
    # rotateByOne x k times
    if len(nums) < 2:
        return

    for i in range(k):
        rotateByOne(nums)
    return nums

def rotateArrayApproach03(nums, k):
    # Approach 3: Use reverse
    # Example nums = [1,2,3,4,5], k = 2
    # [3, 2, 1, 4, 5] -> [3, 2, 1, 5, 4] -> [4, 5, 1, 2, 3]
    n = len(nums)
    if n < 2 or k < 1:
        return
    # Reverse last k elements
    reverseArr(nums, n - k, n - 1)
    # Reverse first n - k elements
    reverseArr(nums, 0, n - k - 1)
    # Reverse entire array
    reverseArr(nums, 0, n - 1)

rotate_by = 3
arr = [1,2,3,4,5,6,7]

print(arr, " Original")
print(rotateArrayApproach01(arr, rotate_by), " Approach 1, Slicing (k={}): Use additional memory".format(rotate_by))
print(arr, " Original")
rotateArrayApproach02(arr, rotate_by + 1)
print(arr, " Approach 2, Rotate 1x{} times".format(rotate_by + 1))
arr.sort()
print(arr, " Original")
rotateArrayApproach03(arr, rotate_by + 2)
print(arr, " Approach 3, Reverse: Rotate {} times".format(rotate_by + 2))

# Output
# [1, 2, 3, 4, 5, 6, 7]  Original
# [5, 6, 7, 1, 2, 3, 4]  Approach 1, Slicing (k=3): Use additional memory
# [1, 2, 3, 4, 5, 6, 7]  Original
# [4, 5, 6, 7, 1, 2, 3]  Approach 2, Rotate 1x4 times
# [1, 2, 3, 4, 5, 6, 7]  Original
# [3, 4, 5, 6, 7, 1, 2]  Approach 3, Reverse: Rotate 5 times
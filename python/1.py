# given an array nums and an integer target, return indices of the 2 numbers such that they add up to target.
# input: [2,7,11,15], target: 9, output: [0,1] 

#  O(n^2)
def sol1(nums, target):
    for num in nums:
        for num2 in nums:
            if num+num2==target:
                return [nums.index(num), nums.index(num2)]

def sol2(nums, target):
    for num in nums:
        diff = target - num
        if diff in nums:
            return [nums.index(diff), nums.index(num)]

def sol3(nums, target):
    hash_map = {}
    for num in nums:
        diff = target - num
        if diff in hash_map:
            return [nums.index(num), hash_map[diff]]     
        hash_map[num] = nums.index(num)

def sol3(arr, target):
    hash_map = {}
    for i, n in enumerate(arr):
        diff = target - n
        if diff in hash_map:
            return [hash_map[diff], i]
        else:
            hash_map[n] = i 
    return hash_map


print(sol([2,7,11,15], 9))



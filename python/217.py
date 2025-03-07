# given an int array, return true if any value appears at least twice, return false if every element is distinct.

def sol1(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j : continue
            if nums[i]==nums[j]:
                print("nums[i]: ",nums[i], " no")
        

def sol2(nums):
    seen = set()
    dubles = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


def sol3(nums):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True

def sol4(nums):
    for num in nums:
        for num2 in nums:
            if num==num2:
                return True
    return False

def sol6(arr):
    hash_set = set()
    for num in arr:
        if num in hash_set:
            return True
        hash_set.add(num) 
    return False

print(sol6([1,2,3,4,5,6,6,6]))

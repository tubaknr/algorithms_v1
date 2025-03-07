# check given list for missing numbers range(1, len(nums))
# input: [4,3,2,7,8,2,3,1], output: [5,6]

def sol1(arr):
    set_nums = set(arr)
    misses = []
    for i in range(1,len(arr)+1):
        if i not in set_nums:
            misses.append(i)
    return misses


print(sol1([4,3,2,7,8,2,3,1]))





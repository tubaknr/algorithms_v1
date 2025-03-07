# input: [8,1,1,2,3] listedeki her bir sayıdan daha küçük olan kaç sayı olduğunu yaz, liste halinde.
# output: [4,0,0,1,3]

# O(n^2)
def sol1(nums):
    smallers = [0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                smallers[i] += 1
                
    return smallers

def sol2(nums):
    sorted_nums = sorted(nums)
    indices = {} # sayı:idx olarak indisleri tutması için hash map
    res = [] # kaç tane oldukları

    for idx, num in enumerate(sorted_nums):
        if num not in indices:
            indices[num] = idx
    for num in nums:
        res.append(indices[num]) # sadece indisleri ekle
    return res


print(soll([8,1,1,2,3]))

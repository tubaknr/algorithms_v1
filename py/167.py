# given sorted array, in ascending order. find 2 nums such that they ad up to a specific target number. 
# [1,3,4,5,7,11],9 , output:[3,4]
# [2,7,11,15],9, output:[1,2]

def sol(arr, target):
    left = 0
    right = len(arr) -1
    while left < right:
        sumA = arr[left] + arr[right]
        if sumA > target:
            right-=1
        elif sumA < target:
            left+=1
        else:
            return [left+1, right+1]
        

print(sol([1,3,4,5,7,11],9))
print(sol([2,7,11,15],9))

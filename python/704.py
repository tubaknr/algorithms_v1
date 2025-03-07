#binary search
# fnd the target number in given array taht is sorted in ascending order.
# if target exists, return its index, if not, return -1.

# input: [-1, 0, 3, 5, 9, 12], target:9, output:4.

def binSearch(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        middle = (arr[left]+arr[right])//2 # ortanca
        if arr[middle] > target: # hedef, ortancadan küçükse, sola kaydır
            right = middle-1
        elif arr[middle] < target: # hedef, ortancadan büyükse , sağa kaydır.
            left = middle+1
        else: # hedef ortancaya eşitse ortancanın indeksini döndür.
            return middle
    return -1

print(binSearch([-1, 0, 3, 5, 9, 12], 9))


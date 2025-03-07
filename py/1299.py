# given an array arr, replace every element int that array with 
# the greatest element among the elemnets to its right,
# and replace the last element with -1.
# input = arr = [17,18,5,4,6,1],
# output = [18, 6, 6, 6, 1, -1]

def sol1(arr):
    res = [-1]
    max_val = 0
    for num in arr[::-1]:
        if max_val<num:
            max_val = num
        res.append(max_val)
    res.pop()   
    return res[::-1]

print(sol([17,18,5,4,6,1]))










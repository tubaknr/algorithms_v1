#sorted array given, take squares of them and sort.
# input=[-4, -1, 0, 3, 10], output=[0,1,9,16,100]

def sol1(nums):
    sq_list = [i*2 for i in nums]
    return sq_list.sort()


def sol2(nums):
    if not nums:
        return nums
    
    if nums[0]>0: # hepsi pzitifse
        return [num*2 for num in nums]

    ###
    # find index first positive
    m = 0
    for idx, num in enumerate(nums):
        if num>0:
            m = idx # ilk pozitif sayının indexi
            break
    
    A = nums[m:] # pozitifler
    B = [-1*n for n in reversed(nums[:m])] # negatifler, sıralanmış
    def merge(A, B):
        a = b = 0
        ret = []
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                ret.append(A[a])
                a += 1
            else:
                ret.append(B[b])
                b += 1
        
        if a < len(A):
            ret.extend(A[a])
        else:
            ret.extend(B[b])
        return [n**2 for n in ret]
    
    print(merge(A,B))


     





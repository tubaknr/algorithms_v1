import math
# n,m = 0, "abc"
# print(n)
# print("m:", m)

# n = n+1
# n+=1
# #n++  NO

# None = absence 

# if n>2:
#     print("n is greater than 2")
# elif n==2:
#     print("n==2")
# else:
#     print("ni smaller than 2")


# if (n>2 and n!=m) or (n==m) or (n==2):
#     print("yes")

# n=0
# while n<5:
#     print(n)
#     n += 1

# for i in range(10):
    # print(i)


# for i in range(2,6):
#     print(i*2)

# for i in range(10,6,-3):
    # print(i)

# print(5//2) # TAM BÖLME
# print(5/2) # KALANLI BÖLME
# print(-3//2) # -2 X
# print(-3/2) # -1.5
# print(10%3) # 1
# print(-10%3) # 2 X
# print(math.fmod(-10,3))

# print(math.floor(3/2))
# print(math.ceil(3/2))
# print(math.sqrt(2))
# print(math.pow(2,3))

# float("inf")
# float("-inf")

# arr = [1,2,3,4,5]
# arr.append(6)
# arr.pop()
# arr.insert(1,8) O(n) X
# arr.pop(1)
# arr[0]=3
# print(arr)


# n=5
# arr = [1]*n
# print(arr)
# print(len(arr))
# arr = [1,2,3,4,5]
# print(arr[-1])
# print(arr[1:2]) # 2 HARİÇ
# print(arr[1:3])

# a,b = [1,2,3] # X ERROR
# print(a,b)

nums = [1,2,3,4,5]
# for i in range(len(nums)):
    # print(nums[i])

# for n in nums:
    # print(n)

# for i,n in enumerate(nums):
    # print(i,n)

nums2 = [7,8,9,10,11]
# print(list(zip(nums, nums2)))


# for n1, n2 in zip(nums, nums2):
    # print(n1, n2)

arr = [3,4,5]
# arr.reverse()
# print(arr)
# print(arr[::-1])

# allNums = nums + nums2
# print(allNums)
# allNums.sort(reverse=True)
# allNums.sort()
# print(allNums)

# arr1 = ["cccca", "ab", "abc", "abcd"]
# arr1.sort(key=lambda x: len(x))
# arr1.sort() # ALPHABETICAL ORDER
# print(arr1)

# arr2 = [i*2 for i in range(9)]
# print(arr2)


# arr3 = [[0]*2 for i in range(3)]
# print(arr3)


s = "abc"
# print(s[:2])
# s[0] = "s" # X
s += "def" # YENİ BİR STRING OLUŞTURDU
# print(s)

# print(int("3232"))
# print(str(3434) + str(3534))

# strings = ["asa", "fsdf", "rdg"]
# print("".join(strings))

new_set = set()
new_set.add(45)
# print(new_set)

new_set.add(1)
new_set.add(2)
new_set.add(3)
# print(new_set)
# print(1 in new_set)
# print(4 in new_set)
# print(len(new_set))
new_set.remove(45)
# print(new_set)

# HASH MAP = DICTIONARY
new_map = {}
new_map[1]="a"
new_map["b"]=2
new_map["c"]=3
# print(new_map)
# print(len(new_map))
# print(new_map["b"])

values = range(3,6)
keys = ["a","b","c"]
myMap = {k:v*2 for k,v in zip(keys, values)} 
# print(myMap)

# myMap = {"a":90, "b":70}
# for key in myMap:
    # print(key, myMap[key])

# for value in myMap.values():
    # print(value)


def multiplyBy2(num):
    return num*2

# print(multiplyBy2(8))

class TryClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
    def getLength(self):
        return self.size

element = TryClass([1,2,3,4])
print(element.getLength())



















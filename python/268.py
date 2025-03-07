# given an array containing n distinct numbers in the range [0, n], return the only number n the range taht is missing from the arrray.
# ex: input : [3,1,0], output: 2
# ex: input: [0,1], output: 2


def sol1(arr):
    arr.sort() # n.log(n)
    for index, value in enumerate(arr):
        if index != value:
            return value - 1
        if value == len(arr)-1:
            return value + 1

def soll(arr):
    return sum(range(len(arr)+1))-sum(arr)


print(soll([3,1,0]))
print(soll([1,0]))



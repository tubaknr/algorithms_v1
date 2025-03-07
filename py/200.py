# best time to buy and sell stock
# input = [7,1,5,3,6,4] her bir değer, stock'un o indexteki değerini gösteriyor. max getiriyi hesapamak siyoruz.

def sol1(arr):  
    left = 0
    right = 1
    maxP = 0
    while right!=len(arr):
        if (arr[left]<arr[right]):
            profit = arr[right]-arr[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right += 1
    return maxP

def maxProfit(prices_array):
    left = 0 # left first element, alma fiyatı
    right = 1 # left second element, satma fiyatı
    maxProfit = 0
    while right != len(prices_array): # en sona gelmediysek
        if (prices_array[left] < prices_array[right]): # aldığım değer (soldaki), satacağımdan (right) küçükse satarım
            profit = prices_array[right] - prices_array[left] # satarsam kazancım
            maxProfit = max(maxProfit, profit) # max kazanç mı?
        else: # right (satacağım) değer aldığımdan azsa
            left = right # right'ın değeri neyse demek ki en küçü oymus; left'i oraya taşı.

        right += 1 # ilerlet
    
    return maxProfit


def sol(pr):
    left = 0
    right = 1
    maxP = 0
    while right != len(pr):
        if pr[left] < pr[right]:
            profit = pr[right] - pr[left]
            maxP = max(profit, maxP)
        else:
            left = right
        right+=1
    return maxP 








# longest substring without repeating characters
# find the length of it.
# input: "abcabcbb", output: 3

def sol1(str):
    left = 0 # SLIDING WINDOW BAŞLANGIÇ NOKTASI
    res = 0 # BULDUĞUMUZ EN UZUN SUBSTRING UZUNLUĞU
    charSet = set() # GÖRÜLMÜŞ KARAKTERLERİ SAKLAYAN SET.

    for right in range(len(str)):
        while str[right] in charSet: # right pointer'ın gsterdiği karakter, önceden gördüklermizden biriyle aynıysa
            charSet.remove(str[left]) # biriktirdiğmiz en soldaki karateri çıkar
            left += 1 # pencereyi 1 basamak sağa kaydır--> TEKRARLAYAN KARAKTERİ ORTADAN KADLDIR.
        charSet.add(str[right]) # şu anda geldiğimiz karakteri set'e ekliyoruz. 
        res = max(res, right - left + 1) # daha önce bulduğumuz en uzun ile şu andaki uzunluğu kıyaslıyoruz.
    return res

def sol(str):
    left = 0
    res = 0
    charSet = set()
    for right in range(len(str)):
        while str[right] in charSet:
            charSet.remove(str[left]) 
            left+=1
        charSet.add(str[right])
        res = max(res, right - left + 1)
    return res



def sol2(str):
    left = 0
    res = 0
    hash_map = set()

    for n in range(len(str)):
        if str[n] in hash_map:
            hash_map.remove(str[left])
            left += 1
        hash_map.add(str[n])
        res = max(res, n - left + 1)
    return res


print(sol2("abcabcbb"))



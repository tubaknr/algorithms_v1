def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        # string doluysa, her harfi seçip, geri kalan harflerle fonksiyonu tekrar çağırıyor
        for i in range(len(string)):
            letter = string[i] # A --> POCKET
            front = string[:i] # ""
            back = string[i+1:] # BC
            together = front + back  # BC
            permute(together, letter + pocket) # BC, A
            

print(permute("ABC", ""))


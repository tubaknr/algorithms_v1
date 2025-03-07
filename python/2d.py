# 3 koordinat veriliyor. bu 3 koordinata birim zamanda birim hareket (sağ,sol,yukarı,aşağ,çapraz) yaparak minimum sürede ulaş ve süreyi ver.
import math 

def minTimeToVisitAllPoints(points_array):
    total_time = 0
    for i in range(len(points_array)-1):
        [x1, y1] = points_array[i]
        [x2, y2] = points_array[i+1]
        # iki nokta arasındaki minimum süre = x'ler farkı ile y'ler farkından ahngisi daha büyük ise o.
        total_time += max(abs(x1-x2), abs(y2-y1))

    return total_time


print(sol([[1,1], [3,4], [-1,0]]))
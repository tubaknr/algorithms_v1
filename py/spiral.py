def spiral(matrix):
    ret = []
    while matrix:
        ret += matrix.pop(0) # İLK SATIR EKLENDİ VE MATRIX'DEN SİLİNDİ.
        # print(matrix)
        for row in matrix:
            ret.append(row.pop()) # KALAN 2 SATIRIN SON ELEMANLARI EKLENDİ VE MATRIXTEN SİLİNDİ
        ret += matrix.pop()[::-1] # son satırın ilk 2 elemanını tersten ekle ve matrixten sil
        for row in matrix[::-1]:
            ret.append(row.pop(0))
        return ret

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))



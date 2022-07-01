def rotation(key):
    rotated_key = [[0]*len(key) for _ in range(len(key[0]))] # 행과 열이 바뀌는점 주의
    for i in range(len(key)):
        for j in range(len(key[0])):
            rotated_key[j][len(key)-i-1] = key[i][j]
    return rotated_key
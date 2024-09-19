if __name__ == "__main__":
    arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr2 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            m[i][j] = arr1[i][0] * arr2[0][j] + arr1[i][1] * arr2[1][j] + arr1[i][2] * arr2[2][j]
    
    print(m)
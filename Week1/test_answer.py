def flippingMatrix(matrix):
    n = len(matrix)
    s = 0

    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    result = flippingMatrix(matrix)
    print(result)

    # matrix = [[3, 2, 1],
    #           [6, 5, 4],
    #           [9, 8, 7]]

    # matrix = [[9, 8, 7],
    #           [6, 5, 4],
    #           [3, 2, 1]]

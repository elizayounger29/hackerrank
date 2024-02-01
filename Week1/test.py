def vertical_sort(matrix):
    row_num = len(matrix)
    row_len = len(matrix[0])

    for element in range(row_len):
        temp = []
        for row in range(row_num):
            temp.append(matrix[row][element])
        # temp = sorted(temp, reverse=True)
        for nrow in range(row_num):
            matrix[nrow][element] = temp[nrow]
    return matrix

def horizontal_sort(matrix):
    pass

def matrix_sort(matrix):
    # sort horizontally
    sorted_matrix = horizontal_sort(matrix)
    #sort vertically
    sorted_matrix = vertical_sort(sorted_matrix)
    return sorted_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    result = matrix_sort(matrix)
    print(result)

    # matrix = [[3, 2, 1],
    #           [6, 5, 4],
    #           [9, 8, 7]]

    # matrix = [[9, 8, 7],
    #           [6, 5, 4],
    #           [3, 2, 1]]
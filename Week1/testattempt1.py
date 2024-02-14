def vertical_sort(matrix):
    row_number = len(matrix)
    row_length = len(matrix[0])

    for element in range(row_length):
        temp = []
        for row in range(row_number):
            temp.append(matrix[row][element])
        if temp[0] < temp[-1]:
            temp.reverse()
        # temp = sorted(temp, reverse=True)
        for new_row in range(row_number):
            matrix[new_row][element] = temp[new_row]
    return matrix

def horizontal_sort(matrix):
    temp = [row.copy() for row in matrix]
    for row in temp:
        if row[0] < row[-1]:
            row.reverse()
    return temp


def flippingMatrix(matrix):
    current_matrix = matrix.copy()
    previous_matrix = None

    while previous_matrix != current_matrix:
        # Apply the first function
        result1 = horizontal_sort(current_matrix)

        # Apply the second function to the result
        result2 = vertical_sort(result1)

        # Check for changes
        if current_matrix != result2:
            # Update matrices for the next iteration
            previous_matrix = current_matrix.copy()
            current_matrix = result2.copy()
        else:
            # If no change, break the loop
            break

    matrix_split = current_matrix[:2]
    matrix_split = [row[:2] for row in current_matrix[:2]]
    matrix_sum = sum(sum(row) for row in matrix_split)
    return matrix_sum


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

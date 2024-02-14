def findMedian(arr):
    sorted_arr = sorted(arr)
    arr_length = len(arr)
    median_idx = (arr_length - 1) // 2
    return sorted_arr[median_idx]


if __name__ == '__main__':
    arr = [5, 4, 6, 2, 1]
    result = findMedian(arr)
    print(result)
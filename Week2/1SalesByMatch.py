from collections import Counter

def sockMerchant(n, ar):
    pairs = 0
    socks = Counter(ar)
    for sock, value in socks.items():
        if value % 2 == 0:
            pairs += value / 2
        elif value > 2:
            pairs += (value - 1) / 2

    return int(pairs)

if __name__ == "__main__":
    # array_length = 7
    # sock_array = [1, 2, 1, 2, 1, 3, 2]
    array_length = 9
    sock_array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(array_length, sock_array)
    print(result)


    # 9
    # 10 20 20 10 10 30 50 10 20
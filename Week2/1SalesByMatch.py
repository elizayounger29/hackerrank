from collections import Counter

def sockMerchant(ar):
    pairs = 0
    socks = Counter(ar)
    for sock, value in socks.items():
        if value % 2 == 0:
            pairs += value / 2
        if value > 2:
            pairs += (value - 1) / 2

    return int(pairs)

if __name__ == "__main__":
    sock_array = [1, 2, 1, 2, 1, 3, 2]
    result = sockMerchant(sock_array)
    print(result)
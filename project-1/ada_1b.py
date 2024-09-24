# Counting sort

def second_algorithm(T, k):
    n = len(T)
    H = [0] * k
    S = [0] * n

    # Count the number of occurrences of each integer in T
    for j in range(n):
        H[T[j] - 1] += 1

    # Compute the cumulative sum of H
    for i in range(1, k):
        H[i] += H[i - 1]

    # Place each element of T in the correct position in S
    for j in range(n - 1, -1, -1):
        S[H[T[j] - 1] - 1] = T[j]
        H[T[j] - 1] -= 1

    return S

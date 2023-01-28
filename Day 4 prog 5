def min_jumps(arr):
    n = len(arr)
    if n == 0 or arr[0] == 0:
        return -1
    jumps = [float('inf')] * n
    jumps[0] = 0
    for i in range(1, n):
        for j in range(i):
            if i <= j + arr[j] and jumps[j] != float('inf'):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    if jumps[n-1] != float('inf'):
        return jumps[n-1]
    else:
        return -1

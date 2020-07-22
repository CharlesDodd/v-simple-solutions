def max_subarray(arr):
    best = 0 
    current = 0
    for i in arr:
        current = max(0, current + i)
        best = max(best, current)

    return best

print(max_subarray([4, -1, 2, 1]))
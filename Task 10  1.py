def subArray(arr, l):
    for i in range(l -1):
        s = arr[i]
        for j in range(i + 1, l):
            s += arr[j]
            if s == 0:
                return True
            return False
array = [4, 2,-3, 1, 6]

print(subArray(array, len(array)))
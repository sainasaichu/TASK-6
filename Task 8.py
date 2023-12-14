arr = [12, 2, 11, 25, 1, 3]
print(arr)
min= arr[0]
for i in range(0, len(arr)):
    if arr[i] < min:
        min = arr[i]
print("smallest element in the arry:", min)

s1 = [4, 3, 2, 8, 5, 6, 7, 2]
s2 = [3, 2, 8, 1, 7, 5, 8, -4]
s3 = s1+s2

result = []

for i in s3:
    if i not in result:
        result.append(i)
print(result)  

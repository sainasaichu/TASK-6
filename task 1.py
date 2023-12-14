a = [10, 501, 22, 37, 100, 999, 87, 351]
oddlist = []
evenlist = []

for i in a:
    if i % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("even numbers", evenlist)
print("odd numbers", oddlist)

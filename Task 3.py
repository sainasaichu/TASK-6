def sumofdigit(n):
    res = 0
    rem = 0
    while n > 0:
        rem = n % 10
        res = res + rem*rem
        n = n//10
        return res
n = int(input ("enter the number :"))
result = n
while result!=1 and result!=4:
    result = sumofdigit(result)

if result == 1:
    print(n, "is happy numbers")
else:
    print(n, "is not happy numbers:")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
result = gcd(a, b)
print("Наибольший общий делитель:", result)
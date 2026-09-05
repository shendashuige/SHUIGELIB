#4 最大公约数
def gcd(a, b):  
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
        
print(gcd(12, 16))
    
#3 阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#2 斐波那契数列
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))



#1 求两数的和
def sum_two_numbers(a, b):
    return a + b

print("1 + 2 =", sum_two_numbers(1, 2))
    
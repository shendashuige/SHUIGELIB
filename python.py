#6 判断素数
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

#5 最小公倍数
def lcm(a, b):  
    return abs(a * b) // gcd(a, b)                                          

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
    

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    result = a + b
    print(result)
gcd(1200, 30)


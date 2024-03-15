def divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
    
def gcd(a,b):
    alist=divisors(a)

    for divisor in reversed(alist):
        if b % divisor == 0:
            return divisor
    return 1

a=60
b=28
result = gcd(a,b)
print(a,'의 약수',divisors(a))
print(a,'과',b,'의 최대공약수 =',result)
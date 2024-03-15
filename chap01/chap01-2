def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def gcd(a, b):
    alist = find_divisors(a)
    blist = find_divisors(b)
    
    common_divisors = set(alist) & set(blist)
    
    return max(common_divisors)

a = 60
b = 28
result = gcd(a, b)
print('a의 약수 = ',find_divisors(a))
print('b의 약수 = ',find_divisors(b))
print(a,'과',b,'의 최대 공약수 =' ,result)
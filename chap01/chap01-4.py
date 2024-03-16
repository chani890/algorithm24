def gcd(a,b):
    print('gcd',(a,b))
    if b>a:
        a,b = b,a
    while b != 0:
        r =  a%b
        a = b
        b = r
        
        if b>a:
            a,b=b,a
        print('gcd',(a,b))

    return a
print("60과 28의 최대공약수 ",gcd(60,28))
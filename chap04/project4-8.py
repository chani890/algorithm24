def power(x,n):
    if n==0:
        return 1
    elif(n%2)==0:
        return power(x*x,n//2)
    else:
        return x*power(x*x,(n-1)//2)
result = power(5, 2)
print(result)
    
def slow_power(x,n):
    result = 1.0
    for i in range(n):
        result = result*x
    return result 
result = slow_power(5, 2)
print(result)
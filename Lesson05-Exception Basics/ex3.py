def div(a, b):
    if b == 0:
        raise ValueError("divisor cannot be zero!")
    else: return a / b
try:
    for i in range(3, -1, -1):
        num = div(5,i)
        print(num)
except:
    i  -= 1
    print(div(5,i))
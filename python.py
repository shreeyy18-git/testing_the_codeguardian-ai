def calculate():
    a = 10
    b = 20
    print("a,b are already declared")
    if a < 0:
        return b
    else:
        return a + b
    return calculate()

print(result)
print("code is executed")

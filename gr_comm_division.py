print ( 'Input two numbers' )
print()
num1 = int (input () )
num2 = int (input () )

def gr_comm_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2
            
    
a = gr_comm_division(num1, num2)
print()
print('Gratest Common Division is', a)

def alg_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = alg_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

b = alg_extended(num1, num2)
print()
print(f'x = {b[1]}, y = {b[2]}')



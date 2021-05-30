def gr_comm_division(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gr_comm_division(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

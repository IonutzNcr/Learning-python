# function 

def ma_function_additionner(number1,number2 = 2):
    return number1 * number2

print(ma_function_additionner(2))

print(ma_function_additionner(2,4))

# function with lambda

def ma_funct_lambda(do):
    return do(2)

ma_funct_lambda(lambda x: print(x))


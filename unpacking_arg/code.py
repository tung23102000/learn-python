def multiply(*args):
    print(args)
    total=1
    for arg in args:
        print(arg)
        total *= arg
    return total
    
# print(multiply(1,3,5))



# def add(x,y):
#     return x +y

# #nums = [3,5]
# nums = {"x": 15, "y": 25}
# print(add(**nums))


def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else: 
        return "No valid operator provided to apply()"
print(apply(1,3,4,56,operator="*"))
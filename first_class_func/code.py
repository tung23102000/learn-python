# def divide(dividend, divisor):
#   if divisor == 0:
#       raise ZeroDivisionError("Divisor cannot be 0")
      
#   return dividend / divisor


# def calculate(*values,operator):
#     return operator(*values)

# result = calculate(20,4, operator=divide)
# print(result)



def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "a", "age": 24},
    {"name": "b", "age": 28}
]

def get_friend_name(friend):
    return friend["name"]

# print(search(friends, "a", lambda friend: friend["name"]))
print(search(friends, "a", get_friend_name))
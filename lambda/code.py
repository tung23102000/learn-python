# def add(x,y):
#     return x+y



#Ex1: dung lambda func
# add =lambda x,y: x+y

# print(add(5,7))

#ex2:

def double(x):
    return x*2

sequence = [1,3,5,7]
#c1: dung list comprehension
doubled = [double(x) for x in sequence]
#c2: dung lambda func
doubled = list(map(lambda x:x*2, sequence))
def divide(dividend, divisor):
  if divisor == 0:
      raise ZeroDivisionError("Divisor cannot be 0")
      
  return dividend / divisor

grades=[]

print("welcome to the average")
try:
   average = divide(sum(grades), len(grades))
   
except ZeroDivisionError as e:
   print(e)
   print("There are no grades yet in your list")
else:
   print(f"The avarage grade is {average}")
finally:
    print("thank you")
    




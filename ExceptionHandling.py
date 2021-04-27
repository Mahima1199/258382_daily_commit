# Example1
try:
    num1 = 10
    num2 = 2
    print(num1/num2)
    print("Done Calculation")
except ZeroDivisionError:
    print("An error occured ")
    print("Due to Zero Division")
#Example 2
try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

#Example 3
try:
    variable = 10
    print(variable+"Hello")
    print(variable/2)
except ZeroDivisionError:
    print("Divided by Zero")
except(ValueError,TypeError):
    print("Error Occured")

# Example 4
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divided by Zero")
finally:
    print("This code will run no matter what")
    



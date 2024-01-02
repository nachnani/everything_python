#syntax error
#def function()
#    print("Hello World")

#logical errors
def addition(a, b):
    return a - b


result = addition(5, 3)
print(result)

#runtime error
numerator = 10
denominator = 0
result = numerator/denominator
print(result)

#exception handling


n1 = int(input('Enter numerator'))
d1 = int(input('Enter denominator'))
result = n1 / d1
try:
    result = n1 / d1
    print(result)
except ZeroDivisionError:
    # write the code we want to execute when exception occurs
    print('Divide by zero error')

print(result)

#else block
n2 = int(input('Enter numerator'))
d2 = int(input('Enter denominator'))

try:
    result = n2 / d2

except ZeroDivisionError:
    # write the code we want to execute when exception occurs
    print('Divide by zero error')
else:
    print(result)

#finally block

n3 = int(input('Enter numerator'))
d3 = int(input('Enter denominator'))

try:
    result = n3 / d3
    print(result)
except ZeroDivisionError:
    # write the code we want to execute when exception occurs
    print('Divide by zero error')
finally:
    print('This code will be executed no matter what')
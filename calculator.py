
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(first, second):
    print("inside the sum() function, passed in: "+str(a)+" and "+str(b))
    return (first + second)

def substract(c, d):
    return (c - d)

def multiply(e, f):
    return (e * f)
    
def divide(g,h):
    return (g / h)

print("here")
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
print(f'Difference of {a} and {b} is {substract(a,b)}')
print(f'product of {a} and {b} is {multiply(a,b)}')
print(f'quotient of {a} and {b} is {divide(a,b)}')

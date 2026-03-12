print(len("Hello World")) # console output: 11
""" the command 'len()' counts how many itens in a object have. Is not included 'int' or 'float', numbers. """

print("Hello"[0]) # console output: H
""" that get the index iten in a object and shows exactly. It starts on 0. """

print(type(123)) # console output: < class 'int' >
print(type(12.3)) # console output: < class 'flt' >
print(type(123_456)) # console output: < class 'int' >
""" you can use '_' to separate three and three numbers to visualate big numbers better. """
print(type("Hello Word")) # console output: < class 'str' >
print(type(True))  # console output: < class 'bln' >

print("123" + "456") # console output: 123456
""" the '+' character concatenate if the two object aren't a number, float ou integer. """
str() # converte to string type
float() # converte to a float type
bool() # converte to a boolean type
print(int("123") + int("456")) # console output: 579
""" using type convertion is possible to avoid such problems. But use carrefully, maybe it can get errors. """

print(1 + 2) # console output: 3
print(1 - 2) # console output: -1
print(2 * 3) # console output: 6
print(2 ** 3) # console output: 8    2x2x2= 8
print(5 / 3) # console output: 1.66666667    float type
print(5 // 3) # console output: 1    integer type, but it cut off the decimal number
print(round(5 / 3)) # console output: 2    integer type, but it set the next number
print(round(5 / 3, 2)) # console output: 1.67    float type

print(f"F string is used to auto converte to string the variables or data type like 1+2= {1+2}.")

""" Studant: Johnatas Dias dos Santos - Sao Paulo/Brazil, 08/mar/2026 """
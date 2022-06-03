'''
Exercise 3a

Write a function that takes a float and two integers ( before and after ). The
function should return a float consisting of before digits before the decimal
point and after digits after. Thus, if we call the function with 1234.5678 , 2 and
3 , the return value should be 34.567 .

'''

def trim(number, before, after):
    dot_position = len(str(int(number)))
    temp = str(number)[dot_position-before:]
    dot_position = len(str(int(float(temp))))
    return float(temp[:dot_position + after + 1])

print(trim(123456.78912, 3, 2))
print(trim(14.105, 2, 6))
print(trim(1663.877364, 1, 5))
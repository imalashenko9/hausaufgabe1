#1
def name_age(name,age):
    name = str(input("Hello "))
    age = int(input("Your age is: "))
    result = (name + str(age))
    return result
print (name_age("",""))

#2
def swap_integers(num1, num2):
    return num2,num1
num1 = 10
num2 = 22
print('Before swapping:')
print(f'num1 = {num1} @', id(num1))
print(f'num2 = {num2} @', id(num2))
num1, num2 = swap_integers(num1,num2)
print('After swapping:')
print(f'num1 = {num1} @', id(num1))
print(f'num2 = {num2} @', id(num2))
print(num1,num2, sep="")

#3
def check_numbers(num1,num2):
     if (num1 or num2) % 6 and (num1 and num2) % 10:
         return True
     else:
         return False
i = check_numbers(6, 10)
print(i)

#4
def sum_up(num1, num2):
    sum = 0
    for i in range (num1, num2 +1):
        sum += i
    if num2 > num1:
        return sum
    else:
        return 0
    if (num1 or num2) > 0:
        return sum
    else:
        return 0
print (sum_up(3,9))

#5
def circle_area(r1,r2,r3):
    pi = 3.14
    r1 = float(pi * r1 ** 2)
    r2 = float(pi * r2 ** 2)
    r3 = float(pi * r3 ** 2)

    return r1+r2+r3
i1 = circle_area(3,1,4)
print(i1)

#6
def check_string(text):
    text2 = text.lower()
    if text2.startswith("a"):
        return True
    elif text2.endswith("a"):
        return True
    else:
        return False
print(check_string("nn"))

#7
def triangle(rows):
    for i in range (0 + rows):
        for j in range (0, i+1):
            print("* ", end ="")
        print ("\r")
rows = 4
triangle(rows)







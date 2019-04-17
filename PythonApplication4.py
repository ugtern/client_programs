
def calc():
    while True:
       print("Options:")
       print("Enter 'add' to add two numbers")
       print("Enter 's' to subtract two numbers")
       print("Enter 'm' to multiply two numbers")
       print("Enter 'd' to divide two numbers")
       print("Enter 'q' to end the program")
       user_input = input(": ")

       if user_input == "q":
          break
       elif user_input == "add":
          num1 = float(input("Введите первое число: "))
          num2 = float(input("Введите второе число: "))
       elif user_input == "s":
          print("Ответ = ", (num1 - num2))
       elif user_input == "m":
          ...
       elif user_input == "d":
          ...
       else:
          print("Unknown input")



def add(a,b):
    return a+b

def sum_f(func,a,b):
    return func(func(a,b),func(a,b))

summary = sum_f(add,10,10)

def output(w):
    print(w)

"""

import random

for i in range(30):
    value = random.randint(1,6)
    print(value)


import math

num = 10
print(math.sqrt(num))


def func(x):
    res = 0
    for i in range(x):
        res += i
    return res


print(func(4))


try:
    print("hello")
    print(1/0)
except ZeroDivisionError:
    print("Ноль")
finally:
    print("этот код сработал")
    
"""

def mf2():
    assert float(input(": ")) >= 0, "Введите число больше нуля"
    try:
        print("hello")
        print(1/0)
    except:
        print("Ноль")
        raise
    finally:
        print("error")

def f(name,name2):
    file = open(name,"rb")
    text = file.read()
    file.close()
    file2 = open(name2, "wb")
    file2.write(text)
    print("complite")
    file2.close()


    """
f("pass.png", "test.jpg")
"""

def f1(name):
    file = open(name,"r")
    for i in range(21):
        print(file.read(4))
    file.close()

def mf2():
    ar = list(range(60))
    print(ar[2])
    print(ar[20:35])
    print(ar[:10])
    print(ar[50:])
    print(ar[5:30:5])
    print(ar[55:40:-5])



def testMf():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                print('*', end=' ')
            else:
                print(end='  ')
        print()
    print('end function')


def nums1():

    nums1 = {1:'One',2:'Two',3:'Three'}
    nums2 = list(range(30))
    print(1 in nums1)
    print("Three" in nums1)
    print(4 not in nums1)
    if 2 in nums2:
        ptint("find!")
    else:
        print("No find")


def usl():
    u = [i**3 for i in range(90,101) if i%2==0]
    print(u)


def fort():
    ask = list(range(6))
    strok = "Numbers: {0}, {1}, {2}, {3}, {4}, {5}".format(ask[0],ask[1],ask[2],ask[3],ask[4],ask[5])
    print(strok)
    new_strok = "And the: {0}{1}{0}{0}{2}".format("Гыча","Ыча","Гычача")
    print(new_strok)


def fstrok():
    print("give ',' near all list elements and change type to string: ",", ".join(["spam","eggs","ham"]))
    print("Change 'Me' to 'World': ","Hello Me".replace("Me","World"))
    print("Phrase starting with 'This'?: ","This is a".startswith("This"))
    print("Phrase ending with 'a'?: ","This is a".endswith("a"))
    print("Phrase ending with 'This'?: ","This is a".endswith("This"))
    print("up words: ","This is a".upper())
    print("smaller words: ","THIS IS A".lower())
    print("Change type to list: ", "spam, eggs, ham".split(", "))

def m_list():
    print(min(range(1,10)))
    print(max(range(1,10)))
    print(abs(-67))
    print(abs(46))
    print(sum(range(1,11)))

def all_any():
    nums = [i for i in range(1,60) if i%11 == 0]
    print(nums)
    if all([i>5 for i in nums]):
        print("True")
    if any([i%2 == 0 for i in nums]):
        print("True")
    for v in enumerate(nums):
        print(v)



def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

def test_f2(ch):
    filename = input("Enter a filename: ")

    with open(filename) as f:
        text = f.read()

    
    for char in ch:
        perc = 100*count_char(text, char) / len(text)

    print("Символов в тексте встречается: ", count_char(text, ch), " Процентное соотношение = ", "{0} - {1}%".format(char, round(perc, 2)))

"""
while True:
    test_f2(input("Введите символ: "))
    """

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x+5

"""
Дублирование функции
print(apply_twice(add_five, 10))
"""

def pure_f(x, y):
    temp = x+2*y
    return temp/(2*x+y)

"""
Правильные функции и лямбда
print(pure_f(5,5))

u = (lambda x: x**2)(8)

a = lambda x: x**2
b = lambda x: x+x
print(b(a(8)))
"""

def byes_rule(x,y):
    x_ = 1-x
    y_ = 1-y
    answer_r = (x*y)/((x*y)+(x_*y_))
    return answer_r

"""
Условие для Правила Байеса
print(byes_rule((3/8),(1/9)))
"""

def add_five(x):
    return x+5

nums = [i for i in range(1,60) if i%11 == 0]
result = list(map(add_five, nums))
print(result)


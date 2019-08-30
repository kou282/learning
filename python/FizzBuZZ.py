# -*- coding: utf-8 -*-
a = input('入力してください')
a = int(a)
if a % 15 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else:
    print(a)

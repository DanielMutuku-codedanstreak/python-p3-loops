#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    i = 10
    while i >= 1 :
        print(i)
        i -= 1
    print(f"Happy New Year!",)

def square_integers(int_list):
    # code goes here!
    pass
    newlist = [item ** 2 for item in int_list]
    return newlist

def fizzbuzz():
    # code goes here!
    pass
    for i in range(1, 101) :
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

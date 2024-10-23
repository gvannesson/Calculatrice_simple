#!/usr/bin/env python3

def addition(number_1:int|float,number_2:int|float) -> int|float:
    if isinstance(number_1,int|float) and isinstance(number_2, int|float):
        return (number_1 + number_2)

if __name__ == '__main__':
    number_1 = 3
    number_2 = 4
    letter = "a"
    print(addition(number_1, number_2))
    print(addition(number_1, letter))
    
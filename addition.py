#!/usr/bin/env python3

def addition(number_1:int|float,number_2:int|float) -> int|float:
    if isinstance(number_1,int|float) and isinstance(number_2, int|float):
        return (number_1 + number_2)
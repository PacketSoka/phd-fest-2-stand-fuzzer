#!/usr/bin/env python3
"""
Module 14 - overwritten names

So yeah, see this small 'e' constant? We have a 'math' package for that in
the real world. But precision and code reuse aside, one letter
variable here gets rewritten when exception is caught by 'except ValueError as e'
clause.
When it resumes execution, 'e' now stands for nothing. Try to use it, get exception.

To trigger, you need to hit 'top_left' case after ValueError.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "kkk,11"


def reliable_func_never_crashes(data: str):
    pi = 3.141592653589793
    e = 2.718281828459045
    try:
        a, b = data.split(",")
    except ValueError:
        return "bad data"
    try:
        a = int(a)
    except ValueError as e:
        a = 0
    try:
        b = int(b)
    except ValueError as e:
        b = 0
    a, b = a % 21, b % 21
    QUADRANT2PROCESS = {
        "top_left": lambda x, y: x * y + e ** y,
        "bottom_right": lambda x, y: x * y - x,
        "top_right": lambda x, y: x * y + x ** 2,
        "bottom_left": lambda x, y: y * pi/2 + x * pi/4
    }
    AXIS = 1_0
    if a <= AXIS and b <= AXIS:
        return QUADRANT2PROCESS["bottom_left"](a, b)
    elif a > AXIS and b > AXIS:
        return QUADRANT2PROCESS["top_right"](a, b)
    elif a <= AXIS and b > AXIS:
        return QUADRANT2PROCESS["top_left"](a, b)
    else:
        return QUADRANT2PROCESS["bottom_right"](a, b)


def main():
    logging.basicConfig(level=logging.INFO)
    target_func = reliable_func_never_crashes
    i = input()
    try:
        result = target_func(i)
    except BaseException as exc:
        logging.exception(exc)
        sys.exit(-1)
    else:
        print(f"retval: {result}")


if __name__ == "__main__":
    main()

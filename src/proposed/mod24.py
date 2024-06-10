#!/usr/bin/env python3
"""
Module 24 - another float

AFAIR this is a play on float precision

Was not used on the stand
"""
import logging
import sys


additional_provided_comment = """
print("Try letter:")
never_crash("a,10,2")

print("Try numbers:")
never_crash("3,4,6")

print("Try crush:")
never_crash("2,53,1")
never_crash(input())
"""


INTENDED_TRIGGER_INPUT = "2,53,1"


def reliable_func_never_crashes(data: str):
    import math

    try:
        number, degree, factor = data.split(",")
        number, degree, factor = int(number), int(degree), int(factor)
    except:
        return 0

    if number < 0 or number > 100 or degree < 1 or degree > 100 or factor < 0 or factor > 100:
        return 0

    number /= 1
    first_number = number ** degree + factor
    second_number = number ** degree + factor + 1

    if str(first_number).find('e') != -1 or str(second_number).find('e') != -1:
        return 0

    expression = math.pi / (first_number - second_number)
    print(f"My calculated expression: {expression}")


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

#!/usr/bin/env python3
"""
Module 7 - more floats

Again, the error is division by zero. But now you have to enter
something that passes the limits no simple number pass. The calculation
is safe until you remember: infinity is a valid IEEE 754 number, and it
can be negative.

On the second day, we also added 'nan' to the mix, which is even stranger
... err ... 'float'. A few people remembered something they heard about
nan, but for some reason, they thought that 'None' in python is a 'nan'.
This is wrong.

Note: nan is not actually mathematical 'transcendent' number, the naming
is a ploy to distract the players.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "nan,inf"


def reliable_func_never_crashes(data: str):  # day two edition
    try:
        x, y = data.split(',')
    except ValueError:
        return "bad fmt"
    try:
        transcendent = float(x)
        decimal = float(y)
    except ValueError:
        return "bad fmt"
    if transcendent != transcendent:
        decimal = -decimal
    else:
        decimal = transcendent * decimal
    if (decimal * decimal) < 1.0:
        decimal = 1.0
    if decimal > 1.0:
        decimal = 1.0
    return 2.718281828459045 / (1.0 / decimal)


DAY_ONE_INTENDED_TRIGGER_INPUT = "minf"


def day_one_reliable_func_never_crashes(data: str):
    data = data.replace("m", "-")
    try:
        decimal = float(data)
    except ValueError:
        return "bad fmt"
    if (decimal * decimal) < 1.0:
        decimal = 1.0
    if decimal > 1.0:
        decimal = 1.0
    return 2.718281828459045 / (1.0 / decimal)


def main():
    logging.basicConfig(level=logging.INFO)
    target_func = reliable_func_never_crashes
    i = input()
    try:
        result = target_func(i)
    except BaseException as exc:
        logging.exception(exc)
        sys.exit(1)
    else:
        print(f"retval: {result}")


if __name__ == "__main__":
    main()

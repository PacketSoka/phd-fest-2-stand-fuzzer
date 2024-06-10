#!/usr/bin/env python3
"""
Module 6 - floats and notations

The error is of course a classical division by zero.

But you seem to have not enough symbols to enter a large enough number
to make the divisor equal to zero. Unless you remember about scientific
notation, that is.

Day two edition protected from repeating with changing the constants.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "2e6"


def reliable_func_never_crashes(data: str):  # day 2 edition
    data = data.replace(",", "1")
    data = data.replace(".", "2")
    if len(data) > 3:
        return "too big"
    try:
        decimal = float(data)
    except ValueError:
        return "bad fmt"
    divisor = 1000000.0 - decimal + 1000000.0
    return 3.14159265358979 / divisor


DAY_ONE_INTENDED_TRIGGER_INPUT = "1e5"


def day_one_reliable_func_never_crashes(data: str):
    data = data.replace(",", "1")
    data = data.replace(".", "2")
    if len(data) > 3:
        return "too big"
    try:
        decimal = float(data)
    except ValueError:
        return "bad fmt"
    divisor = 100000.0 - decimal
    return 3.14159265358979 / divisor


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

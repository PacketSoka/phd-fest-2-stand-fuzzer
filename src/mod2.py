#!/usr/bin/env python3
"""
Module 2 - variable name rules

Exec or eval is always a straightforward way to introduce a bug
or even a vulnerability into your code, ESPECIALLY when user input is
passed.

But we are sanitizing our inputs, right? :)

This statement is intended to create a new variable. On day first, you had
to remember that variable name rules disallow first character to be a digit.
On the second day, we made people remember long reserved keywords.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "nonlocal"


def reliable_func_never_crashes(data: str):  # day 2 edition
    if len(data) <= 6:
        return "too weak"
    nums = [char for char in data if char.isnumeric()]
    if len(nums) != 0 or "," in data or "u" in data:
        return "I hate digits and semicolons and u, they are complex"
    try:
        non_number = int(data)
    except ValueError:
        print("good")
        exec(f"{data} = 1")
    else:
        print("bad input")


DAY_ONE_INTENDED_TRIGGER_INPUT = "1name"


def day_one_reliable_func_never_crashes(data: str):
    if data == "":
        print("bad input")
        return None
    try:
        non_number = int(data)
    except ValueError:
        print("good")
        exec(f"{data} = 1")
    else:
        print("bad input")


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

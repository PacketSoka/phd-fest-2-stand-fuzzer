#!/usr/bin/env python3
"""
Module 12 - parenthesis

This one is very python-specific, but surely there are same kind of problem in
some other languages.

a = (1) is an integer value
b = (2,) is tuple
oh, and just for fun:
c = 1 is an integer value
d = 1, is a tuple

Miss the comma and get completely different type.

Initial version of this module had string value and no parenthesis instead.
Both strings and tuples are iterable... But it was too much, and we ended up
simplifying to this.

Implicit cast to a bool() could be another source of 'funny' bugs tho, but not there.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "aaaDDD2"


def reliable_func_never_crashes(data: str):
    MORE_LOWER, MORE_UPPER, CHARS_ONLY, STRANGE = 0x1, 0x2, 0x4, 0x8
    # digits -> non upper and non lower
    count_lower = len(list(filter(lambda c: c, map(lambda c: c.islower(), data))))
    count_upper = len(list(filter(lambda c: c, map(lambda c: c.isupper(), data))))
    if 0 <= count_lower <= count_upper and count_upper + count_lower == len(data):
        properties = (MORE_UPPER, CHARS_ONLY)
    elif 0 <= count_upper <= count_lower and count_upper + count_lower == len(data):
        properties = (MORE_LOWER, CHARS_ONLY)
    elif 0 <= count_upper < count_lower:
        properties = (MORE_LOWER,)
    elif 0 < count_lower < count_upper:
        properties = (MORE_UPPER,)
    else:
        properties = (STRANGE)
    for prop in properties:
        print(prop)


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

#!/usr/bin/env python3
"""
Module 0 - negative indexing of string

This is simple. Your input will be parsed as an integer for the purpose of
indexing a string. The usual error is when your index is out of range. But
here were are 'protected' from that via 'min' call.

But in python, you can also use negative indexing, which can bypass the 'min'.
Of course, you have to 'undershoot' with the index anyway to trigger an exception.

This was solved easily, and, more importantly, it was easy to explain. So
on the next day, trivial 'bait' were added, which complicates the input but
does not change the error.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "100000,m1000"


def reliable_func_never_crashes(data: str):  # day two edition
    data = data.replace("m", "-")
    try:
        a, b = data.split(",")
        index = int(b)
        limit = int(a)
    except ValueError:
        return None
    str1 = "lorem ipsum dolor sit amet"
    if limit := index < limit:
        index = min(index, len(str1) - 1)
    else:
        index = min(abs(limit), 0)
    print(str1[index])


DAY_ONE_INTENDED_TRIGGER_INPUT = "m100000"


def day_one_reliable_func_never_crashes(data: str):
    data = data.replace("m", "-")
    try:
        index = int(data)
    except ValueError:
        return None
    index = min(index, len(data))
    s1 = "asdfasdfasdfsadf"
    print(s1[index])


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

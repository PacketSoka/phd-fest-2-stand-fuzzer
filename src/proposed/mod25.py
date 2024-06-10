#!/usr/bin/env python3
"""
Module 25 - another another float

If you haven't got this yet, floats are tricky. https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues

This was probably about too big of a float (1e10000000000000000000000000000000000)

But it could be other things: https://github.com/python/cpython/blob/main/Objects/floatobject.c#L1068

Was not used on the stand
"""
import logging
import sys


def reliable_func_never_crashes(data: str):
    try:
        x = float(data)
    except ValueError:
        return 'invalid fmt'
    if x > 0:
        return f"{round(x)} is Positive!!!"
    if x < 0:
        return f"{round(x)} is Negative!!!"
    else:
        return f"{round(x)} is Zero!!!"


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

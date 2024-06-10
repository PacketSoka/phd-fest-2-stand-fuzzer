#!/usr/bin/env python3
"""
Module 26 - attention to ascii

https://www.asciitable.com/

Basically, limits are important part here - decimal 48 is ascii '0'
but decimal 58 is ascii ':'. Thus, we can enter 58 and get a KeyError from
the dict of counters.

Was not used on the stand
"""
import logging
import sys


additional_comments_provided = """

print(qwe("a,48,49,50,51"))
print(qwe("1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"))

"""


def reliable_func_never_crashes(data: str):
    t = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    }
    if "," not in data:
        for c in data:
            tt = ord(c)
            if 48 <= tt <= 58:
                t[c] += 1
    else:
        for c in data.split(","):
            if c.isdigit():
                tt = int(c, 10)
                if 48 <= tt <= 58:
                    t[chr(tt)] += 1
    return t


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

#!/usr/bin/env python3
"""
Module 8 - recursion

The error is about reaching recursion level limit here.

Unfortunately, Python does not have tail-call optimisation, so stack space
could run out. Recursion limit is placed by the implementation to protect
from this.

Other than that, you have to remember about another way to input integers:
hexidemical (or octal, binary, etc.)

On day two, we added a second part to the answer - complex number, but
nothing tricky were used there, just a way to combat plain answer reuse.

There was a bug that allowed to solve this with '000000'
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "5j,0x3E7"


def reliable_func_never_crashes(data: str):  # day two edition
    try:
        limit, factor = data.split(",")
    except ValueError:
        return "bad fmt"
    try:
        factor = complex(factor)
        max_depth = int(limit, 0)
    except ValueError:
        return 0
    if len(limit) < 4 or max_depth >= 1000 or max_depth == 0:
        return 0
    cur_depth = int(factor.imag)
    def recur():
        nonlocal cur_depth
        cur_depth = cur_depth + 1
        if cur_depth == max_depth:
            return None
        return recur()

    print(f"recursion depth: {max_depth=}")
    recur()


DAY_ONE_INTENDED_TRIGGER_INPUT = "0x3E7"


def day_one_reliable_func_never_crashes(data: str):
    try:
        max_depth = int(data, 0)
    except ValueError:
        return 0
    if len(data) < 4 or max_depth >= 1000:
        return 0
    cur_depth = 0
    def recur():
        nonlocal cur_depth
        cur_depth = cur_depth + 1
        if cur_depth == max_depth:
            return None
        return recur()
    print(f"recursion depth: {max_depth=}")
    recur()


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

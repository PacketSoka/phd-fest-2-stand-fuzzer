#!/usr/bin/env python3
"""
Module 21 - float overflow

And you thought only integer could overflow?

In python, big arithmetic is used fot ints, and some integers are just too big
to convert to floats.

To trigger this, you need to remember: there is no '--i' or 'i++' in Python, but
'--' collapses to 'double negation'. Thus, this parser only accumulates the last
number in an input list.

Additionally, we thought about mixing in 'walrus operator operand precedence gotcha',
where 'if i := 10 > 1: print(1)' prints and leaves 'i' equal to True. But it seemed too much.

Day two changes just tried to fix a bug with easy solution
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "1,1,1,1000"


def reliable_func_never_crashes(data: str):  # day two edition
    numbuf = ""
    accumulator = [0, ]
    limit = 1000
    data = data + ","
    for char in data:
        if char == ",":
            try:
                val = int(numbuf)
                val = min(limit, val)
                accumulator.append(val)
                limit = limit - val
            except ValueError:
                pass
            if limit <= 0:
                break
            numbuf = ""
        else:
            numbuf += char
    if len(accumulator) <= 2:
        return "bad input"
    cur = len(accumulator) - 1
    limited_sum = 0
    used = 0
    while accumulator[cur] != 0:
        limited_sum += accumulator[--cur]
        if (used := used + 1) > 5:
            break
    return float(2 ** limited_sum)


DAY_ONE_INTENDED_TRIGGER_INPUT = "1,1,1,1000"


def day_one_reliable_func_never_crashes(data: str):
    numbuf = ""
    accumulator = [0, ]
    limit = 1000
    data = data + ","
    for char in data:
        if char == ",":
            try:
                val = int(numbuf)
                accumulator.append(val)
                limit = limit - val
            except ValueError:
                pass
            if limit <=0:
                break
            numbuf = ""
        else:
            numbuf += char
    if len(accumulator) <= 2:
        return "bad input"
    cur = len(accumulator) - 1
    limited_sum = 0
    used = 0
    while accumulator[cur] != 0:
        limited_sum += accumulator[--cur]
        if (used := used + 1) > 5:
            break
    return float(2 ** limited_sum)


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

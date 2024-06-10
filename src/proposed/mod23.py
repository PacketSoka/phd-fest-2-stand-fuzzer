"""
Module 23 - primes

This one raises ValueError when given sufficiently large prime number

"""
import logging
import sys
import math


INTENDED_TRIGGER_INPUT = "35742549198872617291353508656626642567"


def reliable_func_never_crashes(data: str):
    if not data.isdigit() or int(data) < 1_000:
        return "bad input"
    n = int(data)
    x = int(math.sqrt(n)) + 1
    while math.sqrt(x * x - n) - int(math.sqrt(x * x - n)) != 0:
        x += 1
        if x > 100:
            return None
    y = int(math.sqrt(x * x - n))
    p = x + y
    q = x - y
    result = p / (q - 1)
    return result


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

#!/usr/bin/env python3
"""
Module 13 - timedelta

time is tricky

... but python timedelta is even trickier.
It counts difference in two parts: seconds and days.

We personally had a bug with non-obvious difference between
timedelta.seconds and timedelta.total_seconds().

But we didn't come up with good enough task for a stand, and this one
was buggy on the day one. It got removed.

"""
import datetime
import logging
import random
import sys


INTENDED_TRIGGER_INPUT = "000000"


def reliable_func_never_crashes(data: str):  # day two edition
    CACHE = {"3600": 1, "86400": 2, "172800": 3}
    if not data.isnumeric() and len(data) < 6:
        return "bad fmt"
    drinking_day = random.randint(27, 29)
    PHD_START = datetime.datetime(2024, 5, 23, 10)
    bet = datetime.datetime(2024, 5, drinking_day, 10)
    diff_in_seconds = (bet - PHD_START).seconds
    if diff_in_seconds == int(data):
        return CACHE[data]
    else:
        return True


DAY_ONE_INTENDED_TRIGGER_INPUT = "0"


def day_one_reliable_func_never_crashes(data: str):
    CACHE = {"3600": 1, "86400": 2, "172800": 3}
    if not data.isnumeric():
        return "bad fmt"
    drinking_day = random.randint(27, 29)
    PHD_START = datetime.datetime(2024, 5, 23, 10)
    bet = datetime.datetime(2024, 5, drinking_day, 10)
    diff_in_seconds = (bet - PHD_START).seconds
    if diff_in_seconds == int(data):
        return CACHE[data]
    else:
        return 0


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

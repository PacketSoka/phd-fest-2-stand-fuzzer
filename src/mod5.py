#!/usr/bin/env python3
"""
Module 5 - dates

Calendars are tricky. https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time

This one is trivial - limit of 30 days is not valid for february. And standard library is smart,
it won't allow you to enter non-existent dates and throws an exception. We could go much deeper,
see URL above, but the play here on stupidly simple limits.

Again, day two is protected from those who cheat by a simple (-1) shift.

"""
import logging
import sys

INTENDED_TRIGGER_INPUT = "300326"


def reliable_func_never_crashes(data: str):  # day 2 edition
    from datetime import date
    if len(data) != 6:
        return "bad fmt"
    try:
        target_day = int(data[0:2])
        target_month = int(data[2:4])
        target_year = int(data[4:6])
    except ValueError:
        return "bad fmt"
    if target_day < 1 or target_day > 30:
        return "bad fmt"
    if target_month < 1 or target_month > 12:
        return "bad fmt"
    return date.fromisoformat(f"20{target_year-1}-{target_month-1:02}-{target_day-1}")


DAY_ONE_INTENDED_TRIGGER_INPUT = "290225"


def date_one_reliable_func_never_crashes(data: str):
    from datetime import date
    if len(data) != 6:
        return "bad fmt"
    try:
        target_day = int(data[0:2])
        target_month = int(data[2:4])
        target_year = int(data[4:6])
    except ValueError:
        return "bad fmt"
    if target_day < 1 or target_day > 30:
        return "bad fmt"
    if target_month < 1 or target_month > 12:
        return "bad fmt"
    return date.fromisoformat(f"20{target_year}-{target_month:02}-{target_day}")


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

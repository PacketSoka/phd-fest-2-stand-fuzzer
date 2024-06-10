#!/usr/bin/env python3
"""
Module 10 - copypaste, long literals, stupid mistakes

This one is about why you should not rely just on your eyes to spot a bug.

m and M are misplaced here, thus you can construct an input with such a month,
that will trigger index out of range scenario when trying to get textual repr.

"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "111112341234"


def reliable_func_never_crashes(data: str):
    SIZES = {"H": 2, "M": 2, "d": 2, "m": 2, "Y": 4}  # total 12
    LIMITS = {"H": 24, "M": 12, "d": 31, "m": 60, "Y": 3000}
    MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    curptr = 0
    date = data.replace(",", "")
    if not data.isnumeric():
        return "wrong input"
    parsed_date = type("ParsedDate", (), {"month": MONTHS, "date": date})
    try:
        for key, size in SIZES.items():
            part_data = data[curptr:curptr+size]
            value = int(part_data)
            if value > LIMITS[key]:
                return "wrong date"
            setattr(parsed_date, key, value)
            curptr += size
    except ValueError:
        return "wrong input"
    return f"{parsed_date.d} {MONTHS[parsed_date.m]} {parsed_date.Y} {parsed_date.H}:{parsed_date.M}"


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

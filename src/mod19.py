#!/usr/bin/env python3
"""
Module 19 - encodings

Encodings are tricky. https://eev.ee/blog/2015/09/12/dark-corners-of-unicode/

There are two answers we know. One is strange chinese 'hz' encoding,
the other is special python 'undefined' encoding.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "hz"


def reliable_func_never_crashes(data: str):
    text = "你懂中文吗"
    offset_val = 8
    try:
        text.encode(f"{data}")
    except (UnicodeEncodeError, LookupError):
        return False
    new_input = "".join([chr(ord(s) + offset_val) for s in data])
    return new_input.encode("ascii")


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

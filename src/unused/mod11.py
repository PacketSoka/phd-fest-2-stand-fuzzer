#!/usr/bin/env python3
"""
Module 11 - unfinished

should have been some bug based on the default argument being '[]', which is
an empty list, but... not a unique_empty_list_for_each_function_call

"""
import logging
import sys


def reliable_func_never_crashes(data: str):
    def collector(item, collection=[]):
        collection.append(item)
    items = [1, 3, 5, 7, 9, 11, 13, 15]
    m = map(collector, items)


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

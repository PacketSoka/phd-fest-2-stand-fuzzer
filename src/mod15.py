#!/usr/bin/env python3
"""
Module 15 - IPv4

IP addresses in IPv4 are pieces of 32 bits (or four octets). Some address values are reserved.
Generally you cannot expect that next unsigned integer to your address is also a valid address.
Here, entering last valid address would trigger python stdlib to throw an exception when
we try to 'plus 1' to it.

On the day two, one needed to enter it in octal
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "37777777777"


def reliable_func_never_crashes(data: str):  # day two edition
    import ipaddress
    try:
        int_ip = int(data, 8)
    except ValueError:
        return None
    try:
        correct_ip = ipaddress.IPv4Address(int_ip)
    except ipaddress.AddressValueError:
        return None
    if not correct_ip.is_reserved:
        return None
    prev_ip = correct_ip - 1
    next_ip = correct_ip + 1
    return prev_ip, next_ip


DAY_ONE_INTENDED_TRIGGER_INPUT = "ffffffff"


def day_one_reliable_func_never_crashes(data: str):
    import ipaddress
    try:
        int_ip = int(data)
    except ValueError:
        return None
    try:
        correct_ip = ipaddress.IPv4Address(int_ip)
    except ipaddress.AddressValueError:
        return None
    if not correct_ip.is_reserved:
        return None
    prev_ip = correct_ip - 1
    next_ip = correct_ip + 1
    return prev_ip, next_ip


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

#!/usr/bin/env python3
"""
Module 18 - IPv6

This is just plain math and the fact that python stdlib allows to list all
possible hosts in a given ipv6 subnet.

Between days, only constants have changed.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "114"


def reliable_func_never_crashes(data: str):  # day two edition
    import ipaddress
    NUM_HOST = 17_000
    MAX_HOSTS_LEN = 20_000
    try:
        ipv6network = ipaddress.IPv6Network(f"2001:0::0:0/{int(data)}")
    except ValueError:
        return False
    for _ in ipv6network.hosts():
        MAX_HOSTS_LEN = MAX_HOSTS_LEN - 1
        if MAX_HOSTS_LEN < 0:
            return False
    if MAX_HOSTS_LEN > (20_000 - 16_000):
        return False
    select_host = list(ipv6network.hosts())[NUM_HOST]
    return select_host


DAY_ONE_INTENDED_TRIGGER_INPUT = "118"


def day_one_reliable_func_never_crashes(data: str):
    import ipaddress
    NUM_HOST = 1337
    MAX_HOSTS_LEN = 20_000
    try:
        ipv6network = ipaddress.IPv6Network(f"2001:0::0:0/{int(data)}")
    except ValueError:
        return False
    for _ in ipv6network.hosts():
        MAX_HOSTS_LEN = MAX_HOSTS_LEN - 1
        if MAX_HOSTS_LEN < 0:
            return False
    if MAX_HOSTS_LEN > 19_000:
        return False
    select_host = list(ipv6network.hosts())[NUM_HOST]
    return select_host


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

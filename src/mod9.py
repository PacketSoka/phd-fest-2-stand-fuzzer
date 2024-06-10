#!/usr/bin/env python3
"""
Module 9 - YAML literals

This one was first to use a third-party package, but we think that
PyYAML is so ubiquitous it is 'almost stdlib'. Anyway, nothing
library specific is used to proc an error.

The error is triggering '.lower()' call on a non-str value.

To get there, one need to enter a such value into YAML that
it will be parsed into python 'True'. But you cannot use 'true'
literal.

Fortunately, YAML threats 'yes' or 'on' as 'true'.

On day two a bug was fixed, where unintentionally empty strings also crashed
the module. We also added same character mapping function as an anticheat.

"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "XBG,KW"


def reliable_func_never_crashes(data: str):  # day 2 edition
    def thugshaker_day2(s: str) -> str:
        table = str.maketrans("QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm",
                              "mnbvcxzlkjhgfdsapoiuytrewq0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ")
        return s.translate(table)
    data = thugshaker_day2(data)
    try:
        f_val, s_val, *t_val = data.split(",")
    except ValueError:
        return None
    if not f_val or not s_val or f_val.lower() == s_val.lower():
        return None
    if f_val.lower() == "true":
        return None
    if f_val.isnumeric() or s_val.isnumeric():
        return None
    import yaml
    res = yaml.safe_load(f'''
    event: PHD2
    participant: Guest
    hack_app: {f_val}
    get_prize: {s_val}
    ''')
    if res.get("hack_app") is None or res.get("get_prize") is None:
        return None
    if res.get("hack_app") is True and res.get("get_prize") is True:
        return t_val.lower()


DAY_ONE_INTENDED_TRIGGER_INPUT = "yes,on"


def day_one_reliable_func_never_crashes(data: str):
    try:
        f_val, s_val, *t_val = data.split(",")
    except ValueError:
        return None
    if not f_val or not s_val or f_val == s_val:
        return None
    if f_val.lower() == "true":
        return None

    import yaml
    res = yaml.safe_load(f'''
    event: PHD2
    participant: Guest
    hack_app: {f_val}
    get_prize: {s_val}
    ''')

    if res.get("hack_app") is True and res.get("get_prize") is True:
        return t_val.lower()


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

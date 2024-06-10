#!/usr/bin/env python3
"""
Module 22 - yet another YAML gotcha

Now, intended exception is TypeError when str is concatenated with None.
To get None, you pass special YAML value 'null'.

Day two changes were bug fixes.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "null"


def reliable_func_never_crashes(data: str):  # day two edition
    import yaml
    data = data.replace(",", "")
    if data == "" or data.isnumeric() or data[0].isnumeric():
        return None
    info = yaml.safe_load(f'''
        event: PHD2
        participant: Guest
        ticket: {data}
    ''')

    if type(info["ticket"]) is bool or type(info["ticket"]) is int:
        return "ticket: " + str(info["ticket"])
    return "info_ticket:" + info["ticket"]


DAY_ONE_INTENDED_TRIGGER_INPUT = "null"


def day_one_reliable_func_never_crashes(data: str):
    import yaml
    info = yaml.safe_load(f'''
        event: PHD2
        participant: Guest
        ticket: {data}
    ''')

    if type(info["ticket"]) is bool or type(info["ticket"]) is int:
        return "ticket: " + str(info["ticket"])
    return "info_ticket:" + info["ticket"]


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

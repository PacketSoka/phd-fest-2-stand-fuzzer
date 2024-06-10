#!/usr/bin/env python3
"""
Module 20 - encodings: part 2: resurrection

KOI8-r is a special little encoding, that was constructed in such a way, that
should you ignore the most significant bit, it will end up as a transliteration.
The reason for this is that some hardware terminals at that time used just 7 bits
for a code point (or 'a rune' as Gophers would say).

To trigger division by zero, here you just need to make such a transliteration.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "positiw"


def reliable_func_never_crashes(data: str):
    text = "ПОЗИТИВ"
    offset_val = 0b1000_0000
    byte_raw = (bytes([(ord(s) | offset_val) for s in data]))
    user_text = byte_raw.decode(encoding="koi8-r", errors="ignore")
    if user_text in text:
        per_identy = len(text) / (len(text) - len(user_text))
        return per_identy
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
        sys.exit(1)
    else:
        print(f"retval: {result}")


if __name__ == "__main__":
    main()

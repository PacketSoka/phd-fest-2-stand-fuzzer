#!/usr/bin/env python3
"""
Module 17 - timezones

Timezones are tricky. https://www.zainrizvi.io/blog/falsehoods-programmers-believe-about-time-zones/

Here we exploit a fact that timezone can differ by 15 minutes from another.

But the error we are trying to trigger could not be further from topic of time. The intended
exception is actually OSError when trying to read from a filepath pointing to a directory.
Non-existing index into default dict will end up giving us an empty string. pathlib will use
empty string as a filename to produce a path, and end up with just a directory.

Should note that pytz is another one of third-party packages. But it is just a collection of
timezone definitions. If you try to run this, and it won't crash, maybe timezones changed :)
"""
import logging
import sys
import pytz



INTENDED_TRIGGER_INPUT = "Australia/Eucla"


def reliable_func_never_crashes(data: str):
    import datetime
    from pytz import timezone
    from collections import defaultdict
    from pathlib import Path
    tzname = data.replace(",", "/")
    phd = datetime.datetime(2024, 5, 23, 10, 0)
    phd_tz = timezone('Europe/Moscow')
    try:
        tgt_tz = timezone(tzname)
    except pytz.exceptions.UnknownTimeZoneError:
        return "no such time zone"
    delay = (phd_tz.utcoffset(phd) - tgt_tz.utcoffset(phd)).total_seconds()
    TZ_DIVIDER_M = 30.0
    M2S = 60.0
    ticket_file_index = (delay / (TZ_DIVIDER_M * M2S)) % 4.0
    ticket_dir = Path.cwd()
    print(ticket_file_index)
    phd_tickets = defaultdict(lambda: "", {0.0: "b_1.pdf", 1.0: "b_2.pdf", 2.0: "b_3.pdf", 3.0: "b_4.pdf"})
    ticket = ticket_dir / phd_tickets[ticket_file_index]
    print(ticket)
    if not ticket.exists():
        return None
    return ticket.read_text(encoding="koi8_r", errors="ignore")


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

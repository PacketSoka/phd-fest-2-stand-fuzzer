#!/usr/bin/env python3
"""
Module 4 - NT filesystem

Filesystems are non-trivial things. https://yakking.branchable.com/posts/falsehoods-programmers-believe-about-file-paths/

This one is more of a meme. NT is very much not UNIX-like kernel, so it could not
care less about backward compatibility with filenames like '''l;\4 \x03\x5\r\n'''.
And so, it could set some rules and limits on a filename.

... like, filename cannot be '''CON'''. Yeah, MS does not care about UNIX compatibility,
but MS-DOS compatibility, on the other hand, is very important.

Of course, CON is a console, not a synonymous for a 'nerd' like the meme alleges. PRN
stands for 'printer', COM stands for a serial port (why tho?), LPT is a name for
old parallel peripheral bus. So it is like '/dev/' but pollutes namespaces for
every directory in every filesystem. Yay, go microsoft, so much for 'object-oriented
OS'.

Module run under Linux, so we had to do some fake things to emulate Windows.

Most people who solved that could not explain the crash, so we assumed a foul play.
Next day, a simple character mapping function were added to thwart puny attempts to
reuse someone's answer.
"""
import logging
import sys
import pathlib


def is_forbidden(name) -> bool:
    FORBIDDEN = ["CON", "PRN", "AUX", "NUL"]
    FORBIDDEN += [f"COM{i}" for i in range(0, 10)]
    FORBIDDEN += [f"LPT{i}" for i in range(0, 10)]
    FORBIDDEN += [x.lower() for x in FORBIDDEN]
    return name in FORBIDDEN


class MockStat:
    st_size = 0


class MockWindowsPath(pathlib.PosixPath):
    def stat(self):
        print(self.name)
        result = super().stat()
        print(result)
        if is_forbidden(self.name):
            return MockStat()
        else:
            return result


pathlib.WindowsPath = MockWindowsPath


INTENDED_TRIGGER_INPUT = "tkw"


def reliable_func_never_crashes(data: str):  # day 2 edition
    def thugshaker_day2(s: str) -> str:
        table = str.maketrans("QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm",
                              "mnbvcxzlkjhgfdsapoiuytrewq0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ")
        return s.translate(table)
    data = thugshaker_day2(data)
    import pathlib
    import tempfile
    if not data.isalnum():
        return "bad fmt"
    FS_QUOTA_SIZE = 2 ** 30
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = pathlib.WindowsPath(tmpdir)
            new_file = tmpdir / data.upper()
            new_file.touch()
            test_data = data * 80
            new_file.write_text(test_data)
            stats = new_file.stat()
            count = 15
            while count := count - 1:
                try:
                    test_data_sz = int(FS_QUOTA_SIZE / stats.st_size)
                    test_data = test_data[0] * test_data_sz
                    new_file.write_text(test_data)
                except OSError:
                    break
            print(new_file.stat().st_size)
    except OSError as exc:
        logging.exception(exc)


DAY_ONE_INTENDED_TRIGGER_INPUT = "CON"


def day_one_reliable_func_never_crashes(data: str):
    import pathlib
    import tempfile
    if not data.isalnum():
        return "bad fmt"
    FS_QUOTA_SIZE = 2 ** 30
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = pathlib.WindowsPath(tmpdir)
            new_file = tmpdir / data.upper()
            new_file.touch()
            test_data = data * 80
            new_file.write_text(test_data)
            stats = new_file.stat()
            count = 15
            while count := count - 1:
                try:
                    test_data_sz = int(FS_QUOTA_SIZE / stats.st_size)
                    test_data = test_data[0] * test_data_sz
                    new_file.write_text(test_data)
                except OSError:
                    break
            print(new_file.stat().st_size)
    except OSError as exc:
        logging.exception(exc)


def main():
    logging.basicConfig(level=logging.INFO)
    target_func = reliable_func_never_crashes
    i = input()
    try:
        result = target_func(i)
    except BaseException as exc:
        logging.exception(exc)
        sys.exit(-1)
    else:
        print(f"retval: {result}")


if __name__ == "__main__":
    main()

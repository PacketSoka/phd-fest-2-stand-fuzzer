#!/usr/bin/env python3
"""
Module 3 - POSIX filesystem

Filesystems are non-trivial things. https://yakking.branchable.com/posts/falsehoods-programmers-believe-about-file-paths/

Filenames and filepaths are different things. It appeared on day three that not everyone knows this.
'/path/to/file'
|             |
|-------------| - filepath
|             |
|        |----| - filename

In POSIX, almost any printable character can be a part of a filename, but length of a filename is
limited.

On day two it became apparent that most people just spam big strings when nothing works,
so we added a twist - now, you could construct such a filepath, that creation
would end up hogging all the resources or even trigger a recursion limit error.
This is not a POSIX standard limit, more like python stdlib problem
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "AAAA" * 1000


def reliable_func_never_crashes(data: str):  # day 2 edition
    import pathlib
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        for char in "aeiouy,":
            data = data.replace(char, "/")
        for char in "qwrtpsdfghjklzxcvbnm":
            data = data.replace(char, "")
        for char in "AEIOUY":
            data = data.replace(char, f"/{char}/{char}/")
        for char in "QWRTPSDFGHJKLZXCVBNM":
            char = data.replace(char, char.encode().decode())
        for char in "0123456789":
            data = data.replace(char, "")
        result, cur = "", ""
        for char in data:
            if char == cur:
                continue
            else:
                result += char
                cur = char
        data = "./" + data + "big.bin"
        tmpdir = pathlib.PosixPath(tmpdir)
        new_file = tmpdir / data
        new_file.parent.mkdir(parents=True, exist_ok=True)
        new_file.touch()
        new_file.write_text(data * 80)
        stats = new_file.stat()
        print(stats.st_size / stats.st_blksize)


DAY_ONE_INTENDED_TRIGGER_INPUT = "q" * 300


def day_one_reliable_func_never_crashes(data: str):
    import pathlib
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = pathlib.PosixPath(tmpdir)
        new_file = tmpdir / data
        new_file.touch()
        new_file.write_text(data * 80)
        stats = new_file.stat()
        print(stats.st_size / stats.st_blksize)


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

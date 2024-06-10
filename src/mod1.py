#!/usr/bin/env python3
"""
Module 1 - value and object equivalency

Again, trigger generic 'index out of range - off by one', 'bypass' the
'protection'. 'Protection' check is two-part: 'idx > max' and 'idx is not max'.

Trick is with the difference between '==' and 'is' operations. The latter
answers 'are two names refer to the same object (as in memory addr+size)'.
It is, generally speaking, wrong to use it here, as the intention within
code is to check value equivalency ('==' or better yet, '>=').

On day first, this module was erroneous :) It appears that '_PY_NSMALLPOSINTS' is 257

https://stackoverflow.com/questions/15171695/whats-with-the-integer-cache-maintained-by-the-interpreter

Python is an '''interpreted''' language with a heavy runtime. It would be more
precise to say that it (usually) executes as a bytecode on a virtual machine.
When you 'apt install python'/'winget install python' you actually install
CPython - the most popular distribution. This VM makes many optimisations
to make Py-programs run at least somewhat faster.

One such optimisation is 'Small Integer Caching' which pre-creates and
most importantly reuses the same 'object' for most small (<257) integers.

On the surface, Python does not operate on machine-represented integers,
but on 'PyLong' (previously 'PyInt') objects. This enables transparent 'big arithmetic'
and other cool things, but creation of heap-allocated objects is a costly operation.
Thus, 256 of them are pre-allocated and reused. You can see it in the REPL
console - 'a = 10; b = 10; id(a) == id(b)' is True. Then change 10 for 1000.

Another one of optimisations is caching constants by bytecode-compiler. This
won't work in REPL.
"""
import logging
import sys


INTENDED_TRIGGER_INPUT = "504"


def reliable_func_never_crashes(data: str):  # day two edition
    try:
        index = int(data)
    except ValueError:
        return None
    s1 = "12345678" * 63
    if index > len(s1) and index is not len(s1):
        return None
    print(s1[index])


DAY_ONE_INTENDED_TRIGGER_INPUT = "256"


def day_one_reliable_func_never_crashes(data: str):  # BAD! ERROR!
    try:
        index = int(data)
    except ValueError:
        return None
    s1 = "12345678" * 32
    if index > len(s1) and index is not len(s1):
        return None
    print(s1[index])

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

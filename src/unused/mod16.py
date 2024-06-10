#!/usr/bin/env python3
"""
Module 16 - unfinished

some abstract idea around large integers, unbound variables and sockets

"""
import logging
import sys


class MockSock:
    def send(self, data):
        print(data)


sock = MockSock()


def reliable_func_never_crashes(data: str):
    global sock
    if not data.isnumeric():
        return "bad fmt numeric"
    if len(data) < 10:
        data += "0" * (10 - len(data))
    try:
        x, y = int(data[3:0:-1]), int(data[:3:-1])
    except ValueError as exc:
        return "bad fmt int cast", exc
    if x == 0 or y == 0:
        return "bad fmt zero"
    ALPHA_COEF = 1_000_000
    BETA_COEF = 2_000_000

    def computation_one(n: int, m: int) -> int:
        return ALPHA_COEF * n - BETA_COEF * m

    def computation_two(n: int, m: int) -> int:
        return ALPHA_COEF ** n + BETA_COEF * m

    temp_result = computation_one(x, y)
    sock.send(temp_result)
    result = computation_two(x, temp_result)
    sock.send(result)


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

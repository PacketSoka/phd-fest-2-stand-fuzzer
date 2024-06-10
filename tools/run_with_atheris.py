#!/usr/bin/env python3
"""
run_with_atheris - a script to run current modules on another TV display under fuzzer

Yeah, for some modules, answers were right under (little to the right) your nose :P

THIS WON'T WORK OUT OF THE BOX ON YOUR MACHINE!
"""
import atheris
import sys
import importlib
modname = sys.argv[-1]

print(modname)

PREFIX = "~/phd_stand_final/taskapp/exercises/"
sys.path.append("/home/kiosk/finished")


with atheris.instrument_imports():
    module = importlib.import_module(modname)


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    _data = fdp.ConsumeString(sys.maxsize)
    if len(_data) == 0:
        return -1
    whitelist = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,1234567890"
    for n in _data:
        if n not in whitelist:
            return -1
    try:
        b = data.encode("latin")
    except UnicodeEncodeError as e:
        return -1
    if not data.replace(",", "").isalnum():
        return -1
    print(_data)
    sys.stdout = open("dump.txt", "w+")
    module.reliable_func_never_crashes(_data)

# lf_args = ["-stop_file=/tmp/1", "-stop_file=/tmp/1", "-stop_file=/tmp/1"]
# lf_args = ["-help=1", "-help=1", "-help=1"]
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()

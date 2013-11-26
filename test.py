#!/usr/bin/env python
# Copyright (C) 2013, Cameron White
from pyawk import PyAwk, recordEq
import sys

awk = PyAwk()

@awk.begin
def begin():
    awk.allfiles = 0
    awk.myfiles = 0

@awk.main
@recordEq(3, "cbw")
def main(*args):
    awk.myfiles += 1
    awk.allfiles += 1

@awk.end
def end():
    print("all: " + str(awk.allfiles))
    print("me: " + str(awk.myfiles))
    
awk.run(sys.stdin)

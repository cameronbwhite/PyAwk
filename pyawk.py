#!/usr/bin/env python
# Copyright (C) 2013, Cameron White
import re

class PyAwk:
    
    def __init__(self, **kwargs):
        self.FS = ' '
        self.RS = '\n'

    def begin(self, f):
        self.begin = f

    def main(self, f):
        self.main = f

    def end(self, f):
        self.end = f

    def run(self, input):
        if self.begin:
            self.begin()
         
        record = ''
        fields = [None]
        field  = ''
        for i in input.read():
            if i != self.RS:
                record += i
            else:
                fields.append(field)
                fields[0] = record
                record = ''
                field = ''
                try:
                    self.main(*fields)  
                except Exception:
                    pass
                fields = [None]
                continue
            if i != self.FS:
                field += i
            else:
                fields.append(field)
                field = ''

        if self.end:
            self.end()

class recordEq:

    def __init__(self, field, regEx):
        self._field = field
        self._regEx = regEx

    def __call__(self, function):
        def new_function(*args):
            try:
                if re.match(self._regEx, args[self._field]):
                    function(*args)
            except IndexError:
                pass
        return new_function

class recordNotEq:

    def __init__(self, field, regEx):
        self._field = field
        self._regEx = regEx

    def __call__(self, function):
        def new_function(*args):
            try:
                if not re.match(self._regEx, args[self._field]):
                    function(*args)
            except IndexError:
                pass
        return new_function

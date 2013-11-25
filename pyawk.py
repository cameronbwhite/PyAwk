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
    
    def pattern(self, field, regEx):
        if re.match(regEx, field):
            return True
        else:
            return False

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

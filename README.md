PyAwk
=====

Framework for creating python scripts that work like AWK

## IDEA ##

```python
from pyawk import PyAwk

awk = PyAwk(FS=",")

@awk.begin
def begin(*args, **kargs):
    awk.users = 0
    
@awk
def main(*args, **kargs):
    awk.pattern(args[1], r"user_name")
    awk.print(args[2])
    awk.users++

@awk.end
def end(*args, **kargs):
    awk.print("Number of users: ", awk.users)
    
awk.read(stdin)
```

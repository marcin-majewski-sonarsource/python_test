try:
    open("foo.txt", "r")
except SystemExit:  # Noncompliant
    pass
except KeyboardInterrupt:  # No issue raised but be careful when you do this
    pass

try:
    open("bar.txt", "r")
except BaseException:  # Noncompliant
    pass
except:  # Noncompliant
    pass

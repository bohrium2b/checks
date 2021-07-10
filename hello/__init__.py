import check50.*
import check50

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")


@check50.check()
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c")


@check50.check(compiles)
def printhello():
    """running ./hello returns "Hello, world" """
    check50.run("./hello").stdout("[Hh]ello[,]? [Ww]orld!?\n", regex=True).exit(0)

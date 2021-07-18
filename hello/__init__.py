import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")


@check50.check()
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)


@check50.check(compiles)
def anna():
    """Hello responds to name Anna"""
    check50.run("./hello").stdin("Anna").stdout("[Hh]ello,? Anna.?(\n)?", regex=True)

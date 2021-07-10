import check50
import check50.c

@check50.check()
def exists():
    """add2.c exists"""
    check50.exists("add2.c")

@check50.check(exists)
def compiles():
    """add2.c compiles"""
    check50.c.compile("add2.c")
    

@check50.check(compiles)
def adds24():
    """Adds 2 and 4 correctly"""
    check50.run.stdin("2").stdin("4").stdout("6\n").exit()

@check50.check(compiles)
def adds36():
    """Adds 3 and 6 correctly (prints 9)"""
    check50.run.stdin("3").stdin("6").stdout("9\n").exit()
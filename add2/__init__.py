import check50
import check50.c
from random import *

@check50.check()
def exists():
    """add2.c exists"""
    check50.exists("add2.c")

@check50.check(exists)
def compiles():
    """add2.c compiles"""
    check50.c.compile("add2.c", lcs50=True)
    

@check50.check(compiles)
def adds24():
    """Adds 2 and 4 correctly"""
    check50.run("./add2").stdin("2").stdin("4").stdout("6\n").exit()

@check50.check(compiles)
def adds36():
    """Adds 3 and 6 correctly (prints 9)"""
    check50.run("./add2").stdin("3").stdin("6").stdout("9\n").exit()

@check50.check(compiles)
def adds43():
    """Adds 4 and 3 correctly (prints 7)"""
    check50.run("./add2").stdin("4").stdin("3").stdout("7\n").exit()
    
@check50.check(compiles)
def adds21():
    """Adds 2 and 1 correctly (prints 3)"""
    check50.run("./add2").stdin("2").stdin("1").stdout("3\n").exit()
    
@check50.check(compiles)
def addrand():
    """Adds 2 random numbers correctly"""
    int1 = randint(1, 20)
    int2 = randint(1, 20)
    total = int1 + int2
    check50.run("./add2").stdin(int1).stdin(int2).stdout(total + "\n").exit()
    

import check50
import check50.c
import re

@check50.check()
def exists():
    """odd.c exists"""
    check50.exists("odd.c")
    check50.include("testing.c")


@check50.check(exists)
def compiles():
    """odd compiles"""
    check50.c.compile("odd.c", lcs50=True)
    odd = re.sub("int\s+main", "int distro_main", open("odd.c").read())
    testing = open("testing.c").read()
    with open("odd_test.c", "w") as f:
        f.write(odd)
        f.write("\ \ \ \ return 0;\n")
        f.write("\n")
        f.write(testing)
    check50.c.compile("odd_test.c", lcs50=True)

@check50.check(compiles)
def returns_odd_5():
    """isodd returns odd when ran on 5"""
    check50.run("./odd_test 5").stdout("[Oo]dd ?(\n)?", regex=True).exit()

@check50.check(compiles)
def returns_even_4():
    """isodd returns even when ran on 8"""
    check50.run("./odd_test 8").stdout("[Ee]ven( )?(\n)?", regex=True).exit()

@check50.check(compiles)
def returns_odd_9():
    """isodd returns odd when ran on 9"""
    check50.run("./odd_test 9").stdout("[Oo]dd( )?(\n)?", regex=True).exit()

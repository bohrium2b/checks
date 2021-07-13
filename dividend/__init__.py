import check50
import check50.c


@check50.check()
def exists():
    """divisible.c exists"""
    check50.exists("divisible.c")
    check50.include("out.txt")


@check50.check(exists)
def compiles():
    """divisible.c compiles"""
    check50.c.compile("divisible.c")


@check50.check(compiles)
def returns_correct_output():
    """divisible.c returns the correct output"""
    output = check50.run("./divisible").stdout()
    check_out(output, open("out.txt").read())


def check_out(output, correct):
    if output == correct:
        return
    else:
        raise check50.mismatch(correct, output, help=None)

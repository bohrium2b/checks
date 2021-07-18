import check50
import check50.c
from re import *


@check50.check()
def exists():
    """zodiac.c exists"""
    check50.exists("zodiac.c")

@check50.check(exists)
def compiles():
    """zodiac.c compiles"""
    check50.c.compile("zodiac.c", lcs50=True)


@check50.check(compiles)
def returns1924rat():
  """Zodiac returns a zodiac sign of rat when given 1924."""
  expected = "(Your zodiac sign is the)? [Rr]at.?\n?"
  actual = check50.run("./zodiac").stdin("1924").stdout()
  if not match(expected, actual):
    help = None
    raise check50.Mismatch("Your zodiac sign is the Rat\n", actual)


@check50.check(compiles)
def returnsdog():
  """Zodiac returns a zodiac sign of dog when given 2006"""
  check50.run("./zodiac").stdin("2006").stdout("(Your zodiac sign is the)? [Dd]og.?\n?")

@check50.check(compiles)
def returnsgoat():
  """Zodiac returns a zodiac sign of goat when given 1943"""
  check50.run("./zodiac").stdin("1943").stdout("(Your zodiac sign is the)? [Gg]oat.?\n?")

@check50.check(compiles)
def returnshorse():
  """Zodiac returns a zodiac sign of horse when given 1930"""
  check50.run("./zodiac").stdin("1930").stdout("(Your zodiac sign is the)? [Hh]orse.?\n?")


@check50.check(compiles)
def returnsmonkey():
  """Zodiac returns a zodiac sign of monkey when given 1992"""
  check50.run("./zodiac").stdin("1992").stdout("(Your zodiac sign is the)? [Mm]onkey.?\n?")

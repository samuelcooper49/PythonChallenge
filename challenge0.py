#!/usr/bin/env python3

# Solution to Python Challenge Part 0: http://www.pythonchallenge.com/pc/def/0.html

def exponentiate(a,b):
    """
    Exponentiate a with be, i.e. a^b
    inputs:
       a,b : Integers
    Outputs:
       int : Exponentiated value
    Failure:
       Exception
    """
    return(a**b)

if __name__ == "__main__":
    print(exponentiate(2,38))

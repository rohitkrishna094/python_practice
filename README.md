### Python - Intro to Algorithms
---
#### Numbers
- Integers
    - (999).bit_length() gives us the number of bytes held in an integer
    - Cast string to int - int(s, base) => example: d = int(s, 2); If string cannot be represented, this method raises a ValueError exception
- Floats
    - Single Precision: 32 bit float = 1 bit for sign + 23 bits for significant digits or mantissa + 8 buts for exponent.
    - Never compare floats for equality. Use something like this to do it only

            def () a(x, y, places = 7):
                return round(abs(x-y), places) == 0
    - Division operator / always returns a float. Floor division can be made using operator //. Modulus can be done using % operator.
    - divmod(x, y) returns both quotient and remainder when we do x/y. For example, divmod(45, 6) returns (7, 3)
    - round(x, n) returns x rounded to n intergral digits if n is negative or n decimal places if n is positive.
    - as_integer_ratio() gives integer fractional representation of a float.

            2.75.as_integer_ratio() returns (11, 4)
- Complex Numbers
    - imported from cmath module.
    - Has functions for trigonometric and logarithmic functoins + some complex number functions such as phase(), rect(), etc
- Fraction Module
    -     from fractions import Fraction
    -     Fraction(number.as_integer_ratio()) converts float to fraction
    -     Fraction(x,y).denominator gives denominator
    -     Fraction(x,y).numerator gives numerator
- Decimal Module
    -     sum(0.1 for in range(10)) == 1.0 returns False
    -
          from decimal import Decimal
          sum(Decimal ("0.1") for i in range(10)) == Decimal("1.0")
- Other Representations
    - bin(999) returns '0b1111100111
    - hex(999) returns '0x3e7'
    - oct(999) returns '0o1747'
- Random Module
    - example:
        import random
        values = [1,2,3,4]
        print(random.choice(values))
        random.shuffle(values)
        print(values)
        print(random.randint(0,10))
- Numpy package
    - example:
        import numpy as np
        np.array(((11,12,13),(21,22,23),(31,32,33))) - will create an array of array like this
        [
            [11 12 13]
            [21 22 23]
            [31 32 33]
        ]
    -
    x = np.array(...)
    x.ndim returns number of dimensions of array which will be 2 for previous example

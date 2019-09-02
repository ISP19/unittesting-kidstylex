## Unit Testing Assignment

by Arisa Pangpeng


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| two items              |  2 items list       |
| two items many times   |  2 items list       |
| many items list        | list with all items with out duplicates |
| list in list | list with n items and n list |
| many lists in list |  list with n items and n list |
| large list | all items with out duplicates |
| type not a list | raise TypeError |
| empty list| empty list|
## Test Cases for Fraction

Test innit

| Test case              |  Expected Result    |
|------------------------|---------------------|
| int numerator and denominator       |  Fraction(numerator, denominator)   |
| non int numerator   |  TypeError  |
| non int denominator             |  TypeError       |
| non int numerator with int numerator             |  TypeError       |
| int deniminator with non int denominator             |  TypeError       |
| non int numerator and denominator             |  TypeError       |
| positive numerator with denominator = 0   |  numerator is 1  |
| negative numerator with denominator = 0     | numerator is -1 |
| positive numerator with denominator less than 0   | negative numerator |
| negative numerator with denominator less than 0   | positive numerator |

Test str

| Test case              |  Expected Result    |
|------------------------|---------------------|
| numerator = 0 | str of 0 |
| positive numerator| str of positive numerator|
| positive numerator with negative denominator| negative str of Fraction(numeralor / denominator)|
| positive numerator and positive denominator| positive str of Fraction(numerator, denominator) |
| negative numerator and denominator| negative str of Fraction(numerator, denominator) |

Test add

| Test case              |  Expected Result    |
|------------------------|---------------------|
| plus with 2 positive fraction   | positive |
| plus with 2 negative fraction   | negative |
| plus with positive fraction < negative fraction   | negative |
| plus with positive fraction > negative fraction   | positive |
| plus with fraction that denominator = 0 and numerator > 0   | 1/0 |
| plus with fraction that denominator = 0 and numerator < 0   | -1/0 |

Test multiply

| Test case              |  Expected Result    |
|------------------------|---------------------|
| mul with 2 positive fraction   | positive |
| mul with 2 negative fraction   | positive |
| mul with positive and negative fraction   | negative |
| mul with fraction that denominator = 0 and numerator > 0   | 1/0 |
| mul with fraction that denominator = 0 and numerator < 0   | -1/0 |

Test sub

| Test case              |  Expected Result    |
|------------------------|---------------------|
| minus with fraction1 > fraction2   | positive |
| minus with fraction1 < fraction2   | negative |
| minus with fraction that denominator = 0 and numerator > 0   | 1/0 |
| minus with fraction that denominator = 0 and numerator < 0   | -1/0 |

Test eq

| Test case              |  Expected Result    |
|------------------------|---------------------|
| equal fraction | True |
| non equal fraction | False |

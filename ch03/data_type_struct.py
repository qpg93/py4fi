# data types
A = 10
print('type of A:', type(A))
print('bit length of A:', A.bit_length())

GOOGOL = 10 ** 100
print('bit length of GOOGOL:', GOOGOL.bit_length())

# Float objects are internally represented in binary format;
# A decimal number 0 < n < 1 is represented b a series of the form
#     n = x/2 + y/4 + z/8 + ...
# For certain floating-point numbers the binary representation might involve
# a large number of elements or might even be an infinite series.
# A fixed number of bits representing such a number will cause inaccuracies.
B = 0.35
print('B+0.1 =', B + 0.1)

C = 0.5
print('C as integer ratio:', C.as_integer_ratio())
print('B as integer ratio:', B.as_integer_ratio())

import decimal
from decimal import Decimal

print('Decimal context:', decimal.getcontext())
D = Decimal(1) / Decimal(11)
print('D:', D)

decimal.getcontext().prec = 4
E = Decimal(1) / Decimal(11)
print('E:', E)

decimal.getcontext().prec = 50
F = Decimal(1) / Decimal(11)
print('F:', F)

G = D + E + F
print('G:', G)


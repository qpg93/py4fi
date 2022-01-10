""" data types """
import decimal
from decimal import Decimal
import re
from datetime import datetime

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

print('int(True):', int(True))
print('int(False):', int(False))
print('float(True):', float(True))
print('float(False):', float(False))
print('bool(0):', bool(0))
print('bool(0.0):', bool(0.0))
print('bool(1):', bool(1))
print('bool(10.5):', bool(10.5))
print('bool(-2):', bool(-2))

T = 'this is a string object'
print('T capitalize:', T.capitalize())
print('T split:', T.split())
print('T find string:', T.find('string'))
print('T find python:', T.find('Python'))
print('T replace:', T.replace(' ', '|'))

URL = 'http://www.python.org'
print('URL:', URL.strip('htp:/'))

print(f'this is an integer {15:d}')
print(f'this is an integer {15:4d}')
print(f'this is an integer {15:04d}')
print(f'this is an integer {15.3456:f}')
print(f'this is an integer {15.3456:.2f}')
print(f'this is an integer {15.3456:8f}')
print(f'this is an integer {15.3456:8.2f}')
print(f'this is an integer {15.3456:08.2f}')
print(f'this is an integer {"Python":s}.')
print(f'this is an integer {"Python":10s}.')

SERIES = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd';
"""
DT = re.compile(r"'[0-9/:\s]+'")
result = DT.findall(SERIES)
print('result:', result)

pydt = datetime.strptime(result[0].replace("'", ""),
                         "%m/%d/%Y %H:%M:%S")
print(pydt, type(pydt))

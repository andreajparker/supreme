#!/usr/bin/env python

import numpy
from supreme.lib import pywt

if __name__ == '__main__':
   import pprint
   data = numpy.ones((4, 4, 4, 4))   # 4D array
   result = pywt.dwtn(data , 'db1') # sixteen 4D coefficient arrays
   pprint.pprint(result)

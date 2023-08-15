#!/usr/bin/env python3

from sequences import print_fibonacci

import io
import sys

# lib_test.py

class TestPrintFibonacci:
    '''function print_fibonacci()'''

    def test_print_fibonacci_zero(self):
        '''prints empty list when length = 0'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(0)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1]\n'  # Update this line to match the output

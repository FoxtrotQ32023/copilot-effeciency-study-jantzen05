import filecmp
import pytest
import unittest

class TestAss2(unittest.TestCase):
    def test_ass(self):
        self.assertTrue(filecmp.cmp("./stringmultimatching.ans", "./result_test.txt", shallow=False))
import filecmp
import pytest
import unittest

class TestAss2(unittest.TestCase):
    def test_ass(self):
        self.assertTrue(filecmp.cmp("./airlinehub.ans", "./result_ass1.txt", shallow=False))

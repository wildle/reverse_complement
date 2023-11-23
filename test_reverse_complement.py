from unittest import TestCase
from main import reverse_complement

class Test_reverse_complement(TestCase):
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("CGAT"), "ATCG")
        self.assertEqual(reverse_complement("CGzAT"), "AT_CG")
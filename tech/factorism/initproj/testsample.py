import unittest
from solution import *


class Test(unittest.TestCase):

    def test_1(self):
        fh = FactorHandler()
        fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
        fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
        fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
        fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)
        answer = fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10")
        self.assertEqual(answer, 60)

    def test_2(self):
        fh = FactorHandler()
        fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
        fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
        fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
        fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)
        fh.remove_all_factors("mm/dd/yyyy", "10/03/2019")
        answer = fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/05/10")
        self.assertEqual(answer, 15)

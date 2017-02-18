from library_fine import calculate_fine
from library_fine import Date
import unittest

class TestLibraryFine(unittest.TestCase):
    def test_no_fine_charged(self):
        dates = [
                    (Date(6 ,6, 2015), Date(9, 6, 2015), 0),
                    (Date(9 ,6, 2015), Date(9, 6, 2015), 0),
                    (Date(10 ,6, 2014), Date(9, 6, 2015), 0),

                ]
        for ret_day, due_date, fine in dates:
            self.assertEqual(calculate_fine(due_date=due_date, ret_day=ret_day), fine)
if __name__ == '__main__':
    unittest.main()
from library_fine import calculate_fine
from library_fine import Date
import unittest

class TestLibraryFine(unittest.TestCase):
    def dates_test(self, dates):
        for ret_date, due_date, fine in dates:
            self.assertEqual(
                calculate_fine(
                    due_date=due_date, ret_date=ret_date),
                    fine,
                    "\nreturn date: {},\ndue date: {},\nexpected fine: {}.".format(ret_date, due_date, fine))

    def test_no_fine_charged(self):
        dates = [
                    # return date, due date, fine
                    (Date(6 ,6, 2015), Date(9, 6, 2015), 0),
                    (Date(9 ,6, 2015), Date(9, 6, 2015), 0),
                    (Date(10 ,6, 2014), Date(9, 6, 2015), 0),
                    (Date(10 ,2, 2015), Date(9, 6, 2015), 0),
                ]
        self.dates_test(dates)

    def test_fine_charged_in_days(self):
        dates = [
                    # return date, due date, fine
                    (Date(10 ,6, 2015), Date(9, 6, 2015), 1*15),
                    (Date(29 ,6, 2015), Date(9, 6, 2015), 20*15),
                ]
        self.dates_test(dates)

    def test_fine_charged_in_month(self):
        dates = [
                    # return date, due date, fine
                    (Date(10 ,7, 2015), Date(9, 6, 2015), 1*500),
                    (Date(29 ,12, 2015), Date(9, 6, 2015), 6*500),
                ]
        self.dates_test(dates)

    def test_fine_charged_in_years(self):
        dates = [
                    # return date, due date, fine
                    (Date(10 ,6, 2016), Date(9, 6, 2015), 10000),
                    (Date(29 ,6, 2017), Date(9, 6, 2015), 10000),
                ]
        self.dates_test(dates)
if __name__ == '__main__':
    unittest.main()
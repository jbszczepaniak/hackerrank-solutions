import unittest
from append_and_delete import is_convertable_in_k_steps

class TestAppendAndDelete(unittest.TestCase):
    def test_basic_input(self):
        tests = [
                    ('hackerhappy', 'hackerrank', 9, True),
                    ('hackerhappy', 'hackerrank', 10, False),
                    ('hackerhappy', 'hackerrank', 11, True),
                    ('alalala', 'alalala', 3, False),
                    ('alalala', 'alalala', 7, True),
                    ('alalala', 'alalala', 8, False),
                    ('alalala', 'alalala', 9, True),
                    ('abcde', 'abcdf', 1, False),
                    ('abcde', 'abcdf', 2, True),
                ]
        for s,t,k, expected in tests:
            self.assertEqual(is_convertable_in_k_steps(s,t,k),expected)

if __name__ == '__main__':
    unittest.main()

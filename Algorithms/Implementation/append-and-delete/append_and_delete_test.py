import unittest
from append_and_delete import is_convertable

class TestAppendAndDelete(unittest.TestCase):
    def test_basic_input(self):
        tests = [
                    ('hackerhappy', 'hackerrank', 9, True),
                    ('hackerhappy', 'hackerrank', 10, False),
                    ('hackerhappy', 'hackerrank', 11, True),

                    ('alalala', 'alalala', 0, True),
                    ('alalala', 'alalala', 3, False),
                    ('alalala', 'alalala', 7, False),
                    ('alalala', 'alalala', 8, True),
                    ('alalala', 'alalala', 9, False),

                    ('alalala', 'alalala', 14, True),   #From len(s) + len(t) steps, odd and even number of steps are possible
                    ('alalala', 'alalala', 15, True),

                    ('abcde', 'abcdf', 1, False),
                    ('abcde', 'abcdf', 2, True),

                ]
        for s,t,k, expected in tests:
            self.assertEqual(is_convertable(s,t,steps=k), expected, 'convertion {} -> {} in {}, steps'.format(s,t,k))

if __name__ == '__main__':
    unittest.main()

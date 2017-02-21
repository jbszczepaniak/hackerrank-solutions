from jumping_on_the_clouds import min_jumps
import unittest

class TestJumpingOnTheClouds(unittest.TestCase):
    def test_shortest_possibility(self):
        clouds = [0, 1, 0]
        self.assertEqual(min_jumps(clouds), 1)

    def test_4_clouds(self):
        clouds = [0,1,0,0]
        self.assertEqual(min_jumps(clouds), 2)
        clouds = [0,0,1,0]
        self.assertEqual(min_jumps(clouds), 2)


if __name__ == '__main__':
    unittest.main()
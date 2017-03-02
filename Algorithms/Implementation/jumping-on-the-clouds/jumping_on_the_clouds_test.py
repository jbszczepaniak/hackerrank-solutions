from jumping_on_the_clouds import min_jumps
import unittest

class TestJumpingOnTheClouds(unittest.TestCase):
    cloud_sets = [
        ([0, 1, 0], 1),
        ([0,1,0,0], 2),
        ([0,0,1,0], 2),
        ([0,0,0,0], 2),
        ([0,0,0,0,0], 2),
        ([0,0,1,0,0,1,0], 4),
        ([0,0,0,0,1,0], 3)
      ]

    def test_all_cloud_sets(self):
        for clouds, jumps in self.cloud_sets:
          self.assertEqual(min_jumps(clouds), jumps, "{} of jumps is not correct for {}".format(jumps, clouds))

if __name__ == '__main__':
    unittest.main()